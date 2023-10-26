# Authors: Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Lars Buitinck
#          Robert Layton <robertlayton@gmail.com>
#          Jochen Wersdörfer <jochen@wersdoerfer.de>
#          Roman Sinayev <roman.sinayev@gmail.com>
#
# License: BSD 3 clause
"""
The :mod:`sklearn.feature_extraction.text` submodule gathers utilities to
build feature vectors from text documents.
"""

import array
from collections import defaultdict
from collections.abc import Mapping
from functools import partial
from numbers import Integral, Real
from operator import itemgetter
import re
import unicodedata
import warnings

import numpy as np
import scipy.sparse as sp

from ..base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from ..preprocessing import normalize
from ._hash import FeatureHasher
from ._stop_words import ENGLISH_STOP_WORDS
from ..utils.validation import check_is_fitted, check_array, FLOAT_DTYPES
from ..utils import _IS_32BIT
from ..exceptions import NotFittedError
from ..utils._param_validation import StrOptions, Interval, HasMethods


__all__ = [
    "HashingVectorizer",
    "CountVectorizer",
    "ENGLISH_STOP_WORDS",
    "TfidfTransformer",
    "TfidfVectorizer",
    "strip_accents_ascii",
    "strip_accents_unicode",
    "strip_tags",
]


def _preprocess(doc, accent_function=None, lower=False):
    """Chain together an optional series of text preprocessing steps to
    apply to a document.

    Parameters
    ----------
    doc: str
        The string to preprocess
    accent_function: callable, default=None
        Function for handling accented characters. Common strategies include
        normalizing and removing.
    lower: bool, default=False
        Whether to use str.lower to lowercase all of the text

    Returns
    -------
    doc: str
        preprocessed string
    """
    if lower:
        doc = doc.lower()
    if accent_function is not None:
        doc = accent_function(doc)
    return doc


def _analyze(
    doc,
    analyzer=None,
    tokenizer=None,
    ngrams=None,
    preprocessor=None,
    decoder=None,
    stop_words=None,
):
    """Chain together an optional series of text processing steps to go from
    a single document to ngrams, with or without tokenizing or preprocessing.

    If analyzer is used, only the decoder argument is used, as the analyzer is
    intended to replace the preprocessor, tokenizer, and ngrams steps.

    Parameters
    ----------
    analyzer: callable, default=None
    tokenizer: callable, default=None
    ngrams: callable, default=None
    preprocessor: callable, default=None
    decoder: callable, default=None
    stop_words: list, default=None

    Returns
    -------
    ngrams: list
        A sequence of tokens, possibly with pairs, triples, etc.
    """

    if decoder is not None:
        doc = decoder(doc)
    if analyzer is not None:
        doc = analyzer(doc)
    else:
        if preprocessor is not None:
            doc = preprocessor(doc)
        if tokenizer is not None:
            doc = tokenizer(doc)
        if ngrams is not None:
            if stop_words is not None:
                doc = ngrams(doc, stop_words)
            else:
                doc = ngrams(doc)
    return doc


def strip_accents_unicode(s):
    """Transform accentuated unicode symbols into their simple counterpart.

    Warning: the python-level loop and join operations make this
    implementation 20 times slower than the strip_accents_ascii basic
    normalization.

    Parameters
    ----------
    s : str
        The string to strip.

    Returns
    -------
    s : str
        The stripped string.

    See Also
    --------
    strip_accents_ascii : Remove accentuated char for any unicode symbol that
        has a direct ASCII equivalent.
    """
    try:
        # If `s` is ASCII-compatible, then it does not contain any accented
        # characters and we can avoid an expensive list comprehension
        s.encode("ASCII", errors="strict")
        return s
    except UnicodeEncodeError:
        normalized = unicodedata.normalize("NFKD", s)
        return "".join([c for c in normalized if not unicodedata.combining(c)])


def strip_accents_ascii(s):
    """Transform accentuated unicode symbols into ascii or nothing.

    Warning: this solution is only suited for languages that have a direct
    transliteration to ASCII symbols.

    Parameters
    ----------
    s : str
        The string to strip.

    Returns
    -------
    s : str
        The stripped string.

    See Also
    --------
    strip_accents_unicode : Remove accentuated char for any unicode symbol.
    """
    nkfd_form = unicodedata.normalize("NFKD", s)
    return nkfd_form.encode("ASCII", "ignore").decode("ASCII")


def strip_tags(s):
    """Basic regexp based HTML / XML tag stripper function.

    For serious HTML/XML preprocessing you should rather use an external
    library such as lxml or BeautifulSoup.

    Parameters
    ----------
    s : str
        The string to strip.

    Returns
    -------
    s : str
        The stripped string.
    """
    return re.compile(r"<([^>]+)>", flags=re.UNICODE).sub(" ", s)


def _check_stop_list(stop):
    if stop == "english":
        return ENGLISH_STOP_WORDS
    elif isinstance(stop, str):
        raise ValueError("not a built-in stop list: %s" % stop)
    elif stop is None:
        return None
    else:  # assume it's a collection
        return frozenset(stop)


class _VectorizerMixin:
    """Provides common code for text vectorizers (tokenization logic)."""

    _white_spaces = re.compile(r"\s\s+")

    def decode(self, doc):
        """Decode the input into a string of unicode symbols.

        The decoding strategy depends on the vectorizer parameters.

        Parameters
        ----------
        doc : bytes or str
            The string to decode.

        Returns
        -------
        doc: str
            A string of unicode symbols.
        """
        if self.input == "filename":
            with open(doc, "rb") as fh:
                doc = fh.read()

        elif self.input == "file":
            doc = doc.read()

        if isinstance(doc, bytes):
            doc = doc.decode(self.encoding, self.decode_error)

        if doc is np.nan:
            raise ValueError(
                "np.nan is an invalid document, expected byte or unicode string."
            )

        return doc

    def _word_ngrams(self, tokens, stop_words=None):
        """Turn tokens into a sequence of n-grams after stop words filtering"""
        # handle stop words
        if stop_words is not None:
            tokens = [w for w in tokens if w not in stop_words]

        # handle token n-grams
        min_n, max_n = self.ngram_range
        if max_n != 1:
            original_tokens = tokens
            if min_n == 1:
                # no need to do any slicing for unigrams
                # just iterate through the original tokens
                tokens = list(original_tokens)
                min_n += 1
            else:
                tokens = []

            n_original_tokens = len(original_tokens)

            # bind method outside of loop to reduce overhead
            tokens_append = tokens.append
            space_join = " ".join

            for n in range(min_n, min(max_n + 1, n_original_tokens + 1)):
                for i in range(n_original_tokens - n + 1):
                    tokens_append(space_join(original_tokens[i : i + n]))

        return tokens

    def _char_ngrams(self, text_document):
        """Tokenize text_document into a sequence of character n-grams"""
        # normalize white spaces
        text_document = self._white_spaces.sub(" ", text_document)

        text_len = len(text_document)
        min_n, max_n = self.ngram_range
        if min_n == 1:
            # no need to do any slicing for unigrams
            # iterate through the string
            ngrams = list(text_document)
            min_n += 1
        else:
            ngrams = []

        # bind method outside of loop to reduce overhead
        ngrams_append = ngrams.append

        for n in range(min_n, min(max_n + 1, text_len + 1)):
            for i in range(text_len - n + 1):
                ngrams_append(text_document[i : i + n])
        return ngrams

    def _char_wb_ngrams(self, text_document):
        """Whitespace sensitive char-n-gram tokenization.

        Tokenize text_document into a sequence of character n-grams
        operating only inside word boundaries. n-grams at the edges
        of words are padded with space."""
        # normalize white spaces
        text_document = self._white_spaces.sub(" ", text_document)

        min_n, max_n = self.ngram_range
        ngrams = []

        # bind method outside of loop to reduce overhead
        ngrams_append = ngrams.append

        for w in text_document.split():
            w = " " + w + " "
            w_len = len(w)
            for n in range(min_n, max_n + 1):
                offset = 0
                ngrams_append(w[offset : offset + n])
                while offset + n < w_len:
                    offset += 1
                    ngrams_append(w[offset : offset + n])
                if offset == 0:  # count a short word (w_len < n) only once
                    break
        return ngrams

    def build_preprocessor(self):
        """Return a function to preprocess the text before tokenization.

        Returns
        -------
        preprocessor: callable
              A function to preprocess the text before tokenization.
        """
        if self.preprocessor is not None:
            return self.preprocessor

        # accent stripping
        if not self.strip_accents:
            strip_accents = None
        elif callable(self.strip_accents):
            strip_accents = self.strip_accents
        elif self.strip_accents == "ascii":
            strip_accents = strip_accents_ascii
        elif self.strip_accents == "unicode":
            strip_accents = strip_accents_unicode
        else:
            raise ValueError(
                'Invalid value for "strip_accents": %s' % self.strip_accents
            )

        return partial(_preprocess, accent_function=strip_accents, lower=self.lowercase)

    def build_tokenizer(self):
        """Return a function that splits a string into a sequence of tokens.

        Returns
        -------
        tokenizer: callable
              A function to split a string into a sequence of tokens.
        """
        if self.tokenizer is not None:
            return self.tokenizer
        token_pattern = re.compile(self.token_pattern)

        if token_pattern.groups > 1:
            raise ValueError(
                "More than 1 capturing group in token pattern. Only a single "
                "group should be captured."
            )

        return token_pattern.findall

    def get_stop_words(self):
        """Build or fetch the effective stop words list.

        Returns
        -------
        stop_words: list or None
                A list of stop words.
        """
        return _check_stop_list(self.stop_words)

    def _check_stop_words_consistency(self, stop_words, preprocess, tokenize):
        """Check if stop words are consistent

        Returns
        -------
        is_consistent : True if stop words are consistent with the preprocessor
                        and tokenizer, False if they are not, None if the check
                        was previously performed, "error" if it could not be
                        performed (e.g. because of the use of a custom
                        preprocessor / tokenizer)
        """
        if id(self.stop_words) == getattr(self, "_stop_words_id", None):
            # Stop words are were previously validated
            return None

        # NB: stop_words is validated, unlike self.stop_words
        try:
            inconsistent = set()
            for w in stop_words or ():
                tokens = list(tokenize(preprocess(w)))
                for token in tokens:
                    if token not in stop_words:
                        inconsistent.add(token)
            self._stop_words_id = id(self.stop_words)

            if inconsistent:
                warnings.warn(
                    "Your stop_words may be inconsistent with "
                    "your preprocessing. Tokenizing the stop "
                    "words generated tokens %r not in "
                    "stop_words."
                    % sorted(inconsistent)
                )
            return not inconsistent
        except Exception:
            # Failed to check stop words consistency (e.g. because a custom
            # preprocessor or tokenizer was used)
            self._stop_words_id = id(self.stop_words)
            return "error"

    def build_analyzer(self):
        """Return a callable to process input data.

        The callable handles preprocessing, tokenization, and n-grams generation.

        Returns
        -------
        analyzer: callable
            A function to handle preprocessing, tokenization
            and n-grams generation.
        """

        if callable(self.analyzer):
            return partial(_analyze, analyzer=self.analyzer, decoder=self.decode)

        preprocess = self.build_preprocessor()

        if self.analyzer == "char":
            return partial(
                _analyze,
                ngrams=self._char_ngrams,
                preprocessor=preprocess,
                decoder=self.decode,
            )

        elif self.analyzer == "char_wb":

            return partial(
                _analyze,
                ngrams=self._char_wb_ngrams,
                preprocessor=preprocess,
                decoder=self.decode,
            )

        elif self.analyzer == "word":
            stop_words = self.get_stop_words()
            tokenize = self.build_tokenizer()
            self._check_stop_words_consistency(stop_words, preprocess, tokenize)
            return partial(
                _analyze,
                ngrams=self._word_ngrams,
                tokenizer=tokenize,
                preprocessor=preprocess,
                decoder=self.decode,
                stop_words=stop_words,
            )

        else:
            raise ValueError(
                "%s is not a valid tokenization scheme/analyzer" % self.analyzer
            )

    def _validate_vocabulary(self):
        vocabulary = self.vocabulary
        if vocabulary is not None:
            if isinstance(vocabulary, set):
                vocabulary = sorted(vocabulary)
            if not isinstance(vocabulary, Mapping):
                vocab = {}
                for i, t in enumerate(vocabulary):
                    if vocab.setdefault(t, i) != i:
                        msg = "Duplicate term in vocabulary: %r" % t
                        raise ValueError(msg)
                vocabulary = vocab
            else:
                indices = set(vocabulary.values())
                if len(indices) != len(vocabulary):
                    raise ValueError("Vocabulary contains repeated indices.")
                for i in range(len(vocabulary)):
                    if i not in indices:
                        msg = "Vocabulary of size %d doesn't contain index %d." % (
                            len(vocabulary),
                            i,
                        )
                        raise ValueError(msg)
            if not vocabulary:
                raise ValueError("empty vocabulary passed to fit")
            self.fixed_vocabulary_ = True
            self.vocabulary_ = dict(vocabulary)
        else:
            self.fixed_vocabulary_ = False

    def _check_vocabulary(self):
        """Check if vocabulary is empty or missing (not fitted)"""
        if not hasattr(self, "vocabulary_"):
            self._validate_vocabulary()
            if not self.fixed_vocabulary_:
                raise NotFittedError("Vocabulary not fitted or provided")

        if len(self.vocabulary_) == 0:
            raise ValueError("Vocabulary is empty")

    def _validate_ngram_range(self):
        """Check validity of ngram_range parameter"""
        min_n, max_m = self.ngram_range
        if min_n > max_m:
            raise ValueError(
                "Invalid value for ngram_range=%s "
                "lower boundary larger than the upper boundary."
                % str(self.ngram_range)
            )

    def _warn_for_unused_params(self):

        if self.tokenizer is not None and self.token_pattern is not None:
            warnings.warn(
                "The parameter 'token_pattern' will not be used"
                " since 'tokenizer' is not None'"
            )

        if self.preprocessor is not None and callable(self.analyzer):
            warnings.warn(
                "The parameter 'preprocessor' will not be used"
                " since 'analyzer' is callable'"
            )

        if (
            self.ngram_range != (1, 1)
            and self.ngram_range is not None
            and callable(self.analyzer)
        ):
            warnings.warn(
                "The parameter 'ngram_range' will not be used"
                " since 'analyzer' is callable'"
            )
        if self.analyzer != "word" or callable(self.analyzer):
            if self.stop_words is not None:
                warnings.warn(
                    "The parameter 'stop_words' will not be used"
                    " since 'analyzer' != 'word'"
                )
            if (
                self.token_pattern is not None
                and self.token_pattern != r"(?u)\b\w\w+\b"
            ):
                warnings.warn(
                    "The parameter 'token_pattern' will not be used"
                    " since 'analyzer' != 'word'"
                )
            if self.tokenizer is not None:
                warnings.warn(
                    "The parameter 'tokenizer' will not be used"
                    " since 'analyzer' != 'word'"
                )


class HashingVectorizer(
    TransformerMixin, _VectorizerMixin, BaseEstimator, auto_wrap_output_keys=None
):
    r"""Convert a collection of text documents to a matrix of token occurrences.

    It turns a collection of text documents into a scipy.sparse matrix holding
    token occurrence counts (or binary occurrence information), possibly
    normalized as token frequencies if norm='l1' or projected on the euclidean
    unit sphere if norm='l2'.

    This text vectorizer implementation uses the hashing trick to find the
    token string name to feature integer index mapping.

    This strategy has several advantages:

    - it is very low memory scalable to large datasets as there is no need to
      store a vocabulary dictionary in memory.

    - it is fast to pickle and un-pickle as it holds no state besides the
      constructor parameters.

    - it can be used in a streaming (partial fit) or parallel pipeline as there
      is no state computed during fit.

    There are also a couple of cons (vs using a CountVectorizer with an
    in-memory vocabulary):

    - there is no way to compute the inverse transform (from feature indices to
      string feature names) which can be a problem when trying to introspect
      which features are most important to a model.

    - there can be collisions: distinct tokens can be mapped to the same
      feature index. However in practice this is rarely an issue if n_features
      is large enough (e.g. 2 ** 18 for text classification problems).

    - no IDF weighting as this would render the transformer stateful.

    The hash function employed is the signed 32-bit version of Murmurhash3.

    Read more in the :ref:`User Guide <text_feature_extraction>`.

    Parameters
    ----------
    input : {'filename', 'file', 'content'}, default='content'
        - If `'filename'`, the sequence passed as an argument to fit is
          expected to be a list of filenames that need reading to fetch
          the raw content to analyze.

        - If `'file'`, the sequence items must have a 'read' method (file-like
          object) that is called to fetch the bytes in memory.

        - If `'content'`, the input is expected to be a sequence of items that
          can be of type string or byte.

    encoding : str, default='utf-8'
        If bytes or files are given to analyze, this encoding is used to
        decode.

    decode_error : {'strict', 'ignore', 'replace'}, default='strict'
        Instruction on what to do if a byte sequence is given to analyze that
        contains characters not of the given `encoding`. By default, it is
        'strict', meaning that a UnicodeDecodeError will be raised. Other
        values are 'ignore' and 'replace'.

    strip_accents : {'ascii', 'unicode'} or callable, default=None
        Remove accents and perform other character normalization
        during the preprocessing step.
        'ascii' is a fast method that only works on characters that have
        a direct ASCII mapping.
        'unicode' is a slightly slower method that works on any character.
        None (default) does nothing.

        Both 'ascii' and 'unicode' use NFKD normalization from
        :func:`unicodedata.normalize`.

    lowercase : bool, default=True
        Convert all characters to lowercase before tokenizing.

    preprocessor : callable, default=None
        Override the preprocessing (string transformation) stage while
        preserving the tokenizing and n-grams generation steps.
        Only applies if ``analyzer`` is not callable.

    tokenizer : callable, default=None
        Override the string tokenization step while preserving the
        preprocessing and n-grams generation steps.
        Only applies if ``analyzer == 'word'``.

    stop_words : {'english'}, list, default=None
        If 'english', a built-in stop word list for English is used.
        There are several known issues with 'english' and you should
        consider an alternative (see :ref:`stop_words`).

        If a list, that list is assumed to contain stop words, all of which
        will be removed from the resulting tokens.
        Only applies if ``analyzer == 'word'``.

    token_pattern : str or None, default=r"(?u)\\b\\w\\w+\\b"
        Regular expression denoting what constitutes a "token", only used
        if ``analyzer == 'word'``. The default regexp selects tokens of 2
        or more alphanumeric characters (punctuation is completely ignored
        and always treated as a token separator).

        If there is a capturing group in token_pattern then the
        captured group content, not the entire match, becomes the token.
        At most one capturing group is permitted.

    ngram_range : tuple (min_n, max_n), default=(1, 1)
        The lower and upper boundary of the range of n-values for different
        n-grams to be extracted. All values of n such that min_n <= n <= max_n
        will be used. For example an ``ngram_range`` of ``(1, 1)`` means only
        unigrams, ``(1, 2)`` means unigrams and bigrams, and ``(2, 2)`` means
        only bigrams.
        Only applies if ``analyzer`` is not callable.

    analyzer : {'word', 'char', 'char_wb'} or callable, default='word'
        Whether the feature should be made of word or character n-grams.
        Option 'char_wb' creates character n-grams only from text inside
        word boundaries; n-grams at the edges of words are padded with space.

        If a callable is passed it is used to extract the sequence of features
        out of the raw, unprocessed input.

        .. versionchanged:: 0.21
            Since v0.21, if ``input`` is ``'filename'`` or ``'file'``, the data
            is first read from the file and then passed to the given callable
            analyzer.

    n_features : int, default=(2 ** 20)
        The number of features (columns) in the output matrices. Small numbers
        of features are likely to cause hash collisions, but large numbers
        will cause larger coefficient dimensions in linear learners.

    binary : bool, default=False
        If True, all non zero counts are set to 1. This is useful for discrete
        probabilistic models that model binary events rather than integer
        counts.

    norm : {'l1', 'l2'}, default='l2'
        Norm used to normalize term vectors. None for no normalization.

    alternate_sign : bool, default=True
        When True, an alternating sign is added to the features as to
        approximately conserve the inner product in the hashed space even for
        small n_features. This approach is similar to sparse random projection.

        .. versionadded:: 0.19

    dtype : type, default=np.float64
        Type of the matrix returned by fit_transform() or transform().

    See Also
    --------
    CountVectorizer : Convert a collection of text documents to a matrix of
        token counts.
    TfidfVectorizer : Convert a collection of raw documents to a matrix of
        TF-IDF features.

    Notes
    -----
    This estimator is :term:`stateless` and does not need to be fitted.
    However, we recommend to call :meth:`fit_transform` instead of
    :meth:`transform`, as parameter validation is only performed in
    :meth:`fit`.

    Examples
    --------
    >>> from sklearn.feature_extraction.text import HashingVectorizer
    >>> corpus = [
    ...     'This is the first document.',
    ...     'This document is the second document.',
    ...     'And this is the third one.',
    ...     'Is this the first document?',
    ... ]
    >>> vectorizer = HashingVectorizer(n_features=2**4)
    >>> X = vectorizer.fit_transform(corpus)
    >>> print(X.shape)
    (4, 16)
    """

    _parameter_constraints: dict = {
        "input": [StrOptions({"filename", "file", "content"})],
        "encoding": [str],
        "decode_error": [StrOptions({"strict", "ignore", "replace"})],
        "strip_accents": [StrOptions({"ascii", "unicode"}), None, callable],
        "lowercase": ["boolean"],
        "preprocessor": [callable, None],
        "tokenizer": [callable, None],
        "stop_words": [StrOptions({"english"}), list, None],
        "token_pattern": [str, None],
        "ngram_range": [tuple],
        "analyzer": [StrOptions({"word", "char", "char_wb"}), callable],
        "n_features": [Interval(Integral, 1, np.iinfo(np.int32).max, closed="left")],
        "binary": ["boolean"],
        "norm": [StrOptions({"l1", "l2"}), None],
        "alternate_sign": ["boolean"],
        "dtype": "no_validation",  # delegate to numpy
    }

    def __init__(
        self,
        *,
        input="content",
        encoding="utf-8",
        decode_error="strict",
        strip_accents=None,
        lowercase=True,
        preprocessor=None,
        tokenizer=None,
        stop_words=None,
        token_pattern=r"(?u)\b\w\w+\b",
        ngram_range=(1, 1),
        analyzer="word",
        n_features=(2**20),
        binary=False,
        norm="l2",
        alternate_sign=True,
        dtype=np.float64,
    ):
        self.input = input
        self.encoding = encoding
        self.decode_error = decode_error
        self.strip_accents = strip_accents
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer
        self.analyzer = analyzer
        self.lowercase = lowercase
        self.token_pattern = token_pattern
        self.stop_words = stop_words
        self.n_features = n_features
        self.ngram_range = ngram_range
        self.binary = binary
        self.norm = norm
        self.alternate_sign = alternate_sign
        self.dtype = dtype

    def partial_fit(self, X, y=None):
        """Only validates estimator's parameters.

        This method allows to: (i) validate the estimator's parameters and
        (ii) be consistent with the scikit-learn transformer API.

        Parameters
        ----------
        X : ndarray of shape [n_samples, n_features]
            Training data.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            HashingVectorizer instance.
        """
        # TODO: only validate during the first call
        self._validate_params()
        return self

    def fit(self, X, y=None):
        """Only validates estimator's parameters.

        This method allows to: (i) validate the estimator's parameters and
        (ii) be consistent with the scikit-learn transformer API.

        Parameters
        ----------
        X : ndarray of shape [n_samples, n_features]
            Training data.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            HashingVectorizer instance.
        """
        self._validate_params()

        # triggers a parameter validation
        if isinstance(X, str):
            raise ValueError(
                "Iterable over raw text documents expected, string object received."
            )

        self._warn_for_unused_params()
        self._validate_ngram_range()

        self._get_hasher().fit(X, y=y)
        return self

    def transform(self, X):
        """Transform a sequence of documents to a document-term matrix.

        Parameters
        ----------
        X : iterable over raw text documents, length = n_samples
            Samples. Each sample must be a text document (either bytes or
            unicode strings, file name or file object depending on the
            constructor argument) which will be tokenized and hashed.

        Returns
        -------
        X : sparse matrix of shape (n_samples, n_features)
            Document-term matrix.
        """
        if isinstance(X, str):
            raise ValueError(
                "Iterable over raw text documents expected, string object received."
            )

        self._validate_ngram_range()

        analyzer = self.build_analyzer()
        X = self._get_hasher().transform(analyzer(doc) for doc in X)
        if self.binary:
            X.data.fill(1)
        if self.norm is not None:
            X = normalize(X, norm=self.norm, copy=False)
        return X

    def fit_transform(self, X, y=None):
        """Transform a sequence of documents to a document-term matrix.

        Parameters
        ----------
        X : iterable over raw text documents, length = n_samples
            Samples. Each sample must be a text document (either bytes or
            unicode strings, file name or file object depending on the
            constructor argument) which will be tokenized and hashed.
        y : any
            Ignored. This parameter exists only for compatibility with
            sklearn.pipeline.Pipeline.

        Returns
        -------
        X : sparse matrix of shape (n_samples, n_features)
            Document-term matrix.
        """
        return self.fit(X, y).transform(X)

    def _get_hasher(self):
        return FeatureHasher(
            n_features=self.n_features,
            input_type="string",
            dtype=self.dtype,
            alternate_sign=self.alternate_sign,
        )

    def _more_tags(self):
        return {"X_types": ["string"]}


def _document_frequency(X):
    """Count the number of non-zero values for each feature in sparse X."""
    if sp.isspmatrix_csr(X):
        return np.bincount(X.indices, minlength=X.shape[1])
    else:
        return np.diff(X.indptr)


class CountVectorizer(_VectorizerMixin, BaseEstimator):
    r"""Convert a collection of text documents to a matrix of token counts.

    This implementation produces a sparse representation of the counts using
    scipy.sparse.csr_matrix.

    If you do not provide an a-priori dictionary and you do not use an analyzer
    that does some kind of feature selection then the number of features will
    be equal to the vocabulary size found by analyzing the data.

    Read more in the :ref:`User Guide <text_feature_extraction>`.

    Parameters
    ----------
    input : {'filename', 'file', 'content'}, default='content'
        - If `'filename'`, the sequence passed as an argument to fit is
          expected to be a list of filenames that need reading to fetch
          the raw content to analyze.

        - If `'file'`, the sequence items must have a 'read' method (file-like
          object) that is called to fetch the bytes in memory.

        - If `'content'`, the input is expected to be a sequence of items that
          can be of type string or byte.

    encoding : str, default='utf-8'
        If bytes or files are given to analyze, this encoding is used to
        decode.

    decode_error : {'strict', 'ignore', 'replace'}, default='strict'
        Instruction on what to do if a byte sequence is given to analyze that
        contains characters not of the given `encoding`. By default, it is
        'strict', meaning that a UnicodeDecodeError will be raised. Other
        values are 'ignore' and 'replace'.

    strip_accents : {'ascii', 'unicode'} or callable, default=None
        Remove accents and perform other character normalization
        during the preprocessing step.
        'ascii' is a fast method that only works on characters that have
        a direct ASCII mapping.
        'unicode' is a slightly slower method that works on any characters.
        None (default) does nothing.

        Both 'ascii' and 'unicode' use NFKD normalization from
        :func:`unicodedata.normalize`.

    lowercase : bool, default=True
        Convert all characters to lowercase before tokenizing.

    preprocessor : callable, default=None
        Override the preprocessing (strip_accents and lowercase) stage while
        preserving the tokenizing and n-grams generation steps.
        Only applies if ``analyzer`` is not callable.

    tokenizer : callable, default=None
        Override the string tokenization step while preserving the
        preprocessing and n-grams generation steps.
        Only applies if ``analyzer == 'word'``.

    stop_words : {'english'}, list, default=None
        If 'english', a built-in stop word list for English is used.
        There are several known issues with 'english' and you should
        consider an alternative (see :ref:`stop_words`).

        If a list, that list is assumed to contain stop words, all of which
        will be removed from the resulting tokens.
        Only applies if ``analyzer == 'word'``.

        If None, no stop words will be used. In this case, setting `max_df`
        to a higher value, such as in the range (0.7, 1.0), can automatically detect
        and filter stop words based on intra corpus document frequency of terms.

    token_pattern : str or None, default=r"(?u)\\b\\w\\w+\\b"
        Regular expression denoting what constitutes a "token", only used
        if ``analyzer == 'word'``. The default regexp select tokens of 2
        or more alphanumeric characters (punctuation is completely ignored
        and always treated as a token separator).

        If there is a capturing group in token_pattern then the
        captured group content, not the entire match, becomes the token.
        At most one capturing group is permitted.

    ngram_range : tuple (min_n, max_n), default=(1, 1)
        The lower and upper boundary of the range of n-values for different
        word n-grams or char n-grams to be extracted. All values of n such
        such that min_n <= n <= max_n will be used. For example an
        ``ngram_range`` of ``(1, 1)`` means only unigrams, ``(1, 2)`` means
        unigrams and bigrams, and ``(2, 2)`` means only bigrams.
        Only applies if ``analyzer`` is not callable.

    analyzer : {'word', 'char', 'char_wb'} or callable, default='word'
        Whether the feature should be made of word n-gram or character
        n-grams.
        Option 'char_wb' creates character n-grams only from text inside
        word boundaries; n-grams at the edges of words are padded with space.

        If a callable is passed it is used to extract the sequence of features
        out of the raw, unprocessed input.

        .. versionchanged:: 0.21

        Since v0.21, if ``input`` is ``filename`` or ``file``, the data is
        first read from the file and then passed to the given callable
        analyzer.

    max_df : float in range [0.0, 1.0] or int, default=1.0
        When building the vocabulary ignore terms that have a document
        frequency strictly higher than the given threshold (corpus-specific
        stop words).
        If float, the parameter represents a proportion of documents, integer
        absolute counts.
        This parameter is ignored if vocabulary is not None.

    min_df : float in range [0.0, 1.0] or int, default=1
        When building the vocabulary ignore terms that have a document
        frequency strictly lower than the given threshold. This value is also
        called cut-off in the literature.
        If float, the parameter represents a proportion of documents, integer
        absolute counts.
        This parameter is ignored if vocabulary is not None.

    max_features : int, default=None
        If not None, build a vocabulary that only consider the top
        `max_features` ordered by term frequency across the corpus.
        Otherwise, all features are used.

        This parameter is ignored if vocabulary is not None.

    vocabulary : Mapping or iterable, default=None
        Either a Mapping (e.g., a dict) where keys are terms and values are
        indices in the feature matrix, or an iterable over terms. If not
        given, a vocabulary is determined from the input documents. Indices
        in the mapping should not be repeated and should not have any gap
        between 0 and the largest index.

    binary : bool, default=False
        If True, all non zero counts are set to 1. This is useful for discrete
        probabilistic models that model binary events rather than integer
        counts.

    dtype : dtype, default=np.int64
        Type of the matrix returned by fit_transform() or transform().

    Attributes
    ----------
    vocabulary_ : dict
        A mapping of terms to feature indices.

    fixed_vocabulary_ : bool
        True if a fixed vocabulary of term to indices mapping
        is provided by the user.

    stop_words_ : set
        Terms that were ignored because they either:

          - occurred in too many documents (`max_df`)
          - occurred in too few documents (`min_df`)
          - were cut off by feature selection (`max_features`).

        This is only available if no vocabulary was given.

    See Also
    --------
    HashingVectorizer : Convert a collection of text documents to a
        matrix of token counts.

    TfidfVectorizer : Convert a collection of raw documents to a matrix
        of TF-IDF features.

    Notes
    -----
    The ``stop_words_`` attribute can get large and increase the model size
    when pickling. This attribute is provided only for introspection and can
    be safely removed using delattr or set to None before pickling.

    Examples
    --------
    >>> from sklearn.feature_extraction.text import CountVectorizer
    >>> corpus = [
    ...     'This is the first document.',
    ...     'This document is the second document.',
    ...     'And this is the third one.',
    ...     'Is this the first document?',
    ... ]
    >>> vectorizer = CountVectorizer()
    >>> X = vectorizer.fit_transform(corpus)
    >>> vectorizer.get_feature_names_out()
    array(['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',
           'this'], ...)
    >>> print(X.toarray())
    [[0 1 1 1 0 0 1 0 1]
     [0 2 0 1 0 1 1 0 1]
     [1 0 0 1 1 0 1 1 1]
     [0 1 1 1 0 0 1 0 1]]
    >>> vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
    >>> X2 = vectorizer2.fit_transform(corpus)
    >>> vectorizer2.get_feature_names_out()
    array(['and this', 'document is', 'first document', 'is the', 'is this',
           'second document', 'the first', 'the second', 'the third', 'third one',
           'this document', 'this is', 'this the'], ...)
     >>> print(X2.toarray())
     [[0 0 1 1 0 0 1 0 0 0 0 1 0]
     [0 1 0 1 0 1 0 1 0 0 1 0 0]
     [1 0 0 1 0 0 0 0 1 1 0 1 0]
     [0 0 1 0 1 0 1 0 0 0 0 0 1]]
    """

    _parameter_constraints: dict = {
        "input": [StrOptions({"filename", "file", "content"})],
        "encoding": [str],
        "decode_error": [StrOptions({"strict", "ignore", "replace"})],
        "strip_accents": [StrOptions({"ascii", "unicode"}), None, callable],
        "lowercase": ["boolean"],
        "preprocessor": [callable, None],
        "tokenizer": [callable, None],
        "stop_words": [StrOptions({"english"}), list, None],
        "token_pattern": [str, None],
        "ngram_range": [tuple],
        "analyzer": [StrOptions({"word", "char", "char_wb"}), callable],
        "max_df": [
            Interval(Real, 0, 1, closed="both"),
            Interval(Integral, 1, None, closed="left"),
        ],
        "min_df": [
            Interval(Real, 0, 1, closed="both"),
            Interval(Integral, 1, None, closed="left"),
        ],
        "max_features": [Interval(Integral, 1, None, closed="left"), None],
        "vocabulary": [Mapping, HasMethods("__iter__"), None],
        "binary": ["boolean"],
        "dtype": "no_validation",  # delegate to numpy
    }

    def __init__(
        self,
        *,
        input="content",
        encoding="utf-8",
        decode_error="strict",
        strip_accents=None,
        lowercase=True,
        preprocessor=None,
        tokenizer=None,
        stop_words=None,
        token_pattern=r"(?u)\b\w\w+\b",
        ngram_range=(1, 1),
        analyzer="word",
        max_df=1.0,
        min_df=1,
        max_features=None,
        vocabulary=None,
        binary=False,
        dtype=np.int64,
    ):
        self.input = input
        self.encoding = encoding
        self.decode_error = decode_error
        self.strip_accents = strip_accents
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer
        self.analyzer = analyzer
        self.lowercase = lowercase
        self.token_pattern = token_pattern
        self.stop_words = stop_words
        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features
        self.ngram_range = ngram_range
        self.vocabulary = vocabulary
        self.binary = binary
        self.dtype = dtype

    def _sort_features(self, X, vocabulary):
        """Sort features by name

        Returns a reordered matrix and modifies the vocabulary in place
        """
        sorted_features = sorted(vocabulary.items())
        map_index = np.empty(len(sorted_features), dtype=X.indices.dtype)
        for new_val, (term, old_val) in enumerate(sorted_features):
            vocabulary[term] = new_val
            map_index[old_val] = new_val

        X.indices = map_index.take(X.indices, mode="clip")
        return X

    def _limit_features(self, X, vocabulary, high=None, low=None, limit=None):
        """Remove too rare or too common features.

        Prune features that are non zero in more samples than high or less
        documents than low, modifying the vocabulary, and restricting it to
        at most the limit most frequent.

        This does not prune samples with zero features.
        """
        if high is None and low is None and limit is None:
            return X, set()

        # Calculate a mask based on document frequencies
        dfs = _document_frequency(X)
        mask = np.ones(len(dfs), dtype=bool)
        if high is not None:
            mask &= dfs <= high
        if low is not None:
            mask &= dfs >= low
        if limit is not None and mask.sum() > limit:
            tfs = np.asarray(X.sum(axis=0)).ravel()
            mask_inds = (-tfs[mask]).argsort()[:limit]
            new_mask = np.zeros(len(dfs), dtype=bool)
            new_mask[np.where(mask)[0][mask_inds]] = True
            mask = new_mask

        new_indices = np.cumsum(mask) - 1  # maps old indices to new
        removed_terms = set()
        for term, old_index in list(vocabulary.items()):
            if mask[old_index]:
                vocabulary[term] = new_indices[old_index]
            else:
                del vocabulary[term]
                removed_terms.add(term)
        kept_indices = np.where(mask)[0]
        if len(kept_indices) == 0:
            raise ValueError(
                "After pruning, no terms remain. Try a lower min_df or a higher max_df."
            )
        return X[:, kept_indices], removed_terms

    def _count_vocab(self, raw_documents, fixed_vocab):
        """Create sparse feature matrix, and vocabulary where fixed_vocab=False"""
        if fixed_vocab:
            vocabulary = self.vocabulary_
        else:
            # Add a new value when a new vocabulary item is seen
            vocabulary = defaultdict()
            vocabulary.default_factory = vocabulary.__len__

        analyze = self.build_analyzer()
        j_indices = []
        indptr = []

        values = _make_int_array()
        indptr.append(0)
        for doc in raw_documents:
            feature_counter = {}
            for feature in analyze(doc):
                try:
                    feature_idx = vocabulary[feature]
                    if feature_idx not in feature_counter:
                        feature_counter[feature_idx] = 1
                    else:
                        feature_counter[feature_idx] += 1
                except KeyError:
                    # Ignore out-of-vocabulary items for fixed_vocab=True
                    continue

            j_indices.extend(feature_counter.keys())
            values.extend(feature_counter.values())
            indptr.append(len(j_indices))

        if not fixed_vocab:
            # disable defaultdict behaviour
            vocabulary = dict(vocabulary)
            if not vocabulary:
                raise ValueError(
                    "empty vocabulary; perhaps the documents only contain stop words"
                )

        if indptr[-1] > np.iinfo(np.int32).max:  # = 2**31 - 1
            if _IS_32BIT:
                raise ValueError(
                    (
                        "sparse CSR array has {} non-zero "
                        "elements and requires 64 bit indexing, "
                        "which is unsupported with 32 bit Python."
                    ).format(indptr[-1])
                )
            indices_dtype = np.int64

        else:
            indices_dtype = np.int32
        j_indices = np.asarray(j_indices, dtype=indices_dtype)
        indptr = np.asarray(indptr, dtype=indices_dtype)
        values = np.frombuffer(values, dtype=np.intc)

        X = sp.csr_matrix(
            (values, j_indices, indptr),
            shape=(len(indptr) - 1, len(vocabulary)),
            dtype=self.dtype,
        )
        X.sort_indices()
        return vocabulary, X

    def fit(self, raw_documents, y=None):
        """Learn a vocabulary dictionary of all tokens in the raw documents.

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        y : None
            This parameter is ignored.

        Returns
        -------
        self : object
            Fitted vectorizer.
        """
        self.fit_transform(raw_documents)
        return self

    def fit_transform(self, raw_documents, y=None):
        """Learn the vocabulary dictionary and return document-term matrix.

        This is equivalent to fit followed by transform, but more efficiently
        implemented.

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        y : None
            This parameter is ignored.

        Returns
        -------
        X : array of shape (n_samples, n_features)
            Document-term matrix.
        """
        # We intentionally don't call the transform method to make
        # fit_transform overridable without unwanted side effects in
        # TfidfVectorizer.
        if isinstance(raw_documents, str):
            raise ValueError(
                "Iterable over raw text documents expected, string object received."
            )

        self._validate_params()
        self._validate_ngram_range()
        self._warn_for_unused_params()
        self._validate_vocabulary()
        max_df = self.max_df
        min_df = self.min_df
        max_features = self.max_features

        if self.fixed_vocabulary_ and self.lowercase:
            for term in self.vocabulary:
                if any(map(str.isupper, term)):
                    warnings.warn(
                        "Upper case characters found in"
                        " vocabulary while 'lowercase'"
                        " is True. These entries will not"
                        " be matched with any documents"
                    )
                    break

        vocabulary, X = self._count_vocab(raw_documents, self.fixed_vocabulary_)

        if self.binary:
            X.data.fill(1)

        if not self.fixed_vocabulary_:
            n_doc = X.shape[0]
            max_doc_count = max_df if isinstance(max_df, Integral) else max_df * n_doc
            min_doc_count = min_df if isinstance(min_df, Integral) else min_df * n_doc
            if max_doc_count < min_doc_count:
                raise ValueError("max_df corresponds to < documents than min_df")
            if max_features is not None:
                X = self._sort_features(X, vocabulary)
            X, self.stop_words_ = self._limit_features(
                X, vocabulary, max_doc_count, min_doc_count, max_features
            )
            if max_features is None:
                X = self._sort_features(X, vocabulary)
            self.vocabulary_ = vocabulary

        return X

    def transform(self, raw_documents):
        """Transform documents to document-term matrix.

        Extract token counts out of raw text documents using the vocabulary
        fitted with fit or the one provided to the constructor.

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        Returns
        -------
        X : sparse matrix of shape (n_samples, n_features)
            Document-term matrix.
        """
        if isinstance(raw_documents, str):
            raise ValueError(
                "Iterable over raw text documents expected, string object received."
            )
        self._check_vocabulary()

        # use the same matrix-building strategy as fit_transform
        _, X = self._count_vocab(raw_documents, fixed_vocab=True)
        if self.binary:
            X.data.fill(1)
        return X

    def inverse_transform(self, X):
        """Return terms per document with nonzero entries in X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document-term matrix.

        Returns
        -------
        X_inv : list of arrays of shape (n_samples,)
            List of arrays of terms.
        """
        self._check_vocabulary()
        # We need CSR format for fast row manipulations.
        X = check_array(X, accept_sparse="csr")
        n_samples = X.shape[0]

        terms = np.array(list(self.vocabulary_.keys()))
        indices = np.array(list(self.vocabulary_.values()))
        inverse_vocabulary = terms[np.argsort(indices)]

        if sp.issparse(X):
            return [
                inverse_vocabulary[X[i, :].nonzero()[1]].ravel()
                for i in range(n_samples)
            ]
        else:
            return [
                inverse_vocabulary[np.flatnonzero(X[i, :])].ravel()
                for i in range(n_samples)
            ]

    def get_feature_names_out(self, input_features=None):
        """Get output feature names for transformation.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Not used, present here for API consistency by convention.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        """
        self._check_vocabulary()
        return np.asarray(
            [t for t, i in sorted(self.vocabulary_.items(), key=itemgetter(1))],
            dtype=object,
        )

    def _more_tags(self):
        return {"X_types": ["string"]}


def _make_int_array():
    """Construct an array.array of a type suitable for scipy.sparse indices."""
    return array.array(str("i"))


class TfidfTransformer(
    OneToOneFeatureMixin, TransformerMixin, BaseEstimator, auto_wrap_output_keys=None
):
    """Transform a count matrix to a normalized tf or tf-idf representation.

    Tf means term-frequency while tf-idf means term-frequency times inverse
    document-frequency. This is a common term weighting scheme in information
    retrieval, that has also found good use in document classification.

    The goal of using tf-idf instead of the raw frequencies of occurrence of a
    token in a given document is to scale down the impact of tokens that occur
    very frequently in a given corpus and that are hence empirically less
    informative than features that occur in a small fraction of the training
    corpus.

    The formula that is used to compute the tf-idf for a term t of a document d
    in a document set is tf-idf(t, d) = tf(t, d) * idf(t), and the idf is
    computed as idf(t) = log [ n / df(t) ] + 1 (if ``smooth_idf=False``), where
    n is the total number of documents in the document set and df(t) is the
    document frequency of t; the document frequency is the number of documents
    in the document set that contain the term t. The effect of adding "1" to
    the idf in the equation above is that terms with zero idf, i.e., terms
    that occur in all documents in a training set, will not be entirely
    ignored.
    (Note that the idf formula above differs from the standard textbook
    notation that defines the idf as
    idf(t) = log [ n / (df(t) + 1) ]).

    If ``smooth_idf=True`` (the default), the constant "1" is added to the
    numerator and denominator of the idf as if an extra document was seen
    containing every term in the collection exactly once, which prevents
    zero divisions: idf(t) = log [ (1 + n) / (1 + df(t)) ] + 1.

    Furthermore, the formulas used to compute tf and idf depend
    on parameter settings that correspond to the SMART notation used in IR
    as follows:

    Tf is "n" (natural) by default, "l" (logarithmic) when
    ``sublinear_tf=True``.
    Idf is "t" when use_idf is given, "n" (none) otherwise.
    Normalization is "c" (cosine) when ``norm='l2'``, "n" (none)
    when ``norm=None``.

    Read more in the :ref:`User Guide <text_feature_extraction>`.

    Parameters
    ----------
    norm : {'l1', 'l2'} or None, default='l2'
        Each output row will have unit norm, either:

        - 'l2': Sum of squares of vector elements is 1. The cosine
          similarity between two vectors is their dot product when l2 norm has
          been applied.
        - 'l1': Sum of absolute values of vector elements is 1.
          See :func:`preprocessing.normalize`.
        - None: No normalization.

    use_idf : bool, default=True
        Enable inverse-document-frequency reweighting. If False, idf(t) = 1.

    smooth_idf : bool, default=True
        Smooth idf weights by adding one to document frequencies, as if an
        extra document was seen containing every term in the collection
        exactly once. Prevents zero divisions.

    sublinear_tf : bool, default=False
        Apply sublinear tf scaling, i.e. replace tf with 1 + log(tf).

    Attributes
    ----------
    idf_ : array of shape (n_features)
        The inverse document frequency (IDF) vector; only defined
        if  ``use_idf`` is True.

        .. versionadded:: 0.20

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 1.0

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    CountVectorizer : Transforms text into a sparse matrix of n-gram counts.

    TfidfVectorizer : Convert a collection of raw documents to a matrix of
        TF-IDF features.

    HashingVectorizer : Convert a collection of text documents to a matrix
        of token occurrences.

    References
    ----------
    .. [Yates2011] R. Baeza-Yates and B. Ribeiro-Neto (2011). Modern
                   Information Retrieval. Addison Wesley, pp. 68-74.

    .. [MRS2008] C.D. Manning, P. Raghavan and H. Schütze  (2008).
                   Introduction to Information Retrieval. Cambridge University
                   Press, pp. 118-120.

    Examples
    --------
    >>> from sklearn.feature_extraction.text import TfidfTransformer
    >>> from sklearn.feature_extraction.text import CountVectorizer
    >>> from sklearn.pipeline import Pipeline
    >>> corpus = ['this is the first document',
    ...           'this document is the second document',
    ...           'and this is the third one',
    ...           'is this the first document']
    >>> vocabulary = ['this', 'document', 'first', 'is', 'second', 'the',
    ...               'and', 'one']
    >>> pipe = Pipeline([('count', CountVectorizer(vocabulary=vocabulary)),
    ...                  ('tfid', TfidfTransformer())]).fit(corpus)
    >>> pipe['count'].transform(corpus).toarray()
    array([[1, 1, 1, 1, 0, 1, 0, 0],
           [1, 2, 0, 1, 1, 1, 0, 0],
           [1, 0, 0, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 0, 0]])
    >>> pipe['tfid'].idf_
    array([1.        , 1.22314355, 1.51082562, 1.        , 1.91629073,
           1.        , 1.91629073, 1.91629073])
    >>> pipe.transform(corpus).shape
    (4, 8)
    """

    _parameter_constraints: dict = {
        "norm": [StrOptions({"l1", "l2"}), None],
        "use_idf": ["boolean"],
        "smooth_idf": ["boolean"],
        "sublinear_tf": ["boolean"],
    }

    def __init__(self, *, norm="l2", use_idf=True, smooth_idf=True, sublinear_tf=False):
        self.norm = norm
        self.use_idf = use_idf
        self.smooth_idf = smooth_idf
        self.sublinear_tf = sublinear_tf

    def fit(self, X, y=None):
        """Learn the idf vector (global term weights).

        Parameters
        ----------
        X : sparse matrix of shape n_samples, n_features)
            A matrix of term/token counts.

        y : None
            This parameter is not needed to compute tf-idf.

        Returns
        -------
        self : object
            Fitted transformer.
        """
        self._validate_params()

        # large sparse data is not supported for 32bit platforms because
        # _document_frequency uses np.bincount which works on arrays of
        # dtype NPY_INTP which is int32 for 32bit platforms. See #20923
        X = self._validate_data(
            X, accept_sparse=("csr", "csc"), accept_large_sparse=not _IS_32BIT
        )
        if not sp.issparse(X):
            X = sp.csr_matrix(X)
        dtype = X.dtype if X.dtype in FLOAT_DTYPES else np.float64

        if self.use_idf:
            n_samples, n_features = X.shape
            df = _document_frequency(X)
            df = df.astype(dtype, copy=False)

            # perform idf smoothing if required
            df += int(self.smooth_idf)
            n_samples += int(self.smooth_idf)

            # log+1 instead of log makes sure terms with zero idf don't get
            # suppressed entirely.
            idf = np.log(n_samples / df) + 1
            self._idf_diag = sp.diags(
                idf,
                offsets=0,
                shape=(n_features, n_features),
                format="csr",
                dtype=dtype,
            )

        return self

    def transform(self, X, copy=True):
        """Transform a count matrix to a tf or tf-idf representation.

        Parameters
        ----------
        X : sparse matrix of (n_samples, n_features)
            A matrix of term/token counts.

        copy : bool, default=True
            Whether to copy X and operate on the copy or perform in-place
            operations.

        Returns
        -------
        vectors : sparse matrix of shape (n_samples, n_features)
            Tf-idf-weighted document-term matrix.
        """
        X = self._validate_data(
            X, accept_sparse="csr", dtype=FLOAT_DTYPES, copy=copy, reset=False
        )
        if not sp.issparse(X):
            X = sp.csr_matrix(X, dtype=np.float64)

        if self.sublinear_tf:
            np.log(X.data, X.data)
            X.data += 1

        if self.use_idf:
            # idf_ being a property, the automatic attributes detection
            # does not work as usual and we need to specify the attribute
            # name:
            check_is_fitted(self, attributes=["idf_"], msg="idf vector is not fitted")

            # *= doesn't work
            X = X * self._idf_diag

        if self.norm is not None:
            X = normalize(X, norm=self.norm, copy=False)

        return X

    @property
    def idf_(self):
        """Inverse document frequency vector, only defined if `use_idf=True`.

        Returns
        -------
        ndarray of shape (n_features,)
        """
        # if _idf_diag is not set, this will raise an attribute error,
        # which means hasattr(self, "idf_") is False
        return np.ravel(self._idf_diag.sum(axis=0))

    @idf_.setter
    def idf_(self, value):
        value = np.asarray(value, dtype=np.float64)
        n_features = value.shape[0]
        self._idf_diag = sp.spdiags(
            value, diags=0, m=n_features, n=n_features, format="csr"
        )

    def _more_tags(self):
        return {"X_types": ["2darray", "sparse"]}


class TfidfVectorizer(CountVectorizer):
    r"""Convert a collection of raw documents to a matrix of TF-IDF features.

    Equivalent to :class:`CountVectorizer` followed by
    :class:`TfidfTransformer`.

    Read more in the :ref:`User Guide <text_feature_extraction>`.

    Parameters
    ----------
    input : {'filename', 'file', 'content'}, default='content'
        - If `'filename'`, the sequence passed as an argument to fit is
          expected to be a list of filenames that need reading to fetch
          the raw content to analyze.

        - If `'file'`, the sequence items must have a 'read' method (file-like
          object) that is called to fetch the bytes in memory.

        - If `'content'`, the input is expected to be a sequence of items that
          can be of type string or byte.

    encoding : str, default='utf-8'
        If bytes or files are given to analyze, this encoding is used to
        decode.

    decode_error : {'strict', 'ignore', 'replace'}, default='strict'
        Instruction on what to do if a byte sequence is given to analyze that
        contains characters not of the given `encoding`. By default, it is
        'strict', meaning that a UnicodeDecodeError will be raised. Other
        values are 'ignore' and 'replace'.

    strip_accents : {'ascii', 'unicode'} or callable, default=None
        Remove accents and perform other character normalization
        during the preprocessing step.
        'ascii' is a fast method that only works on characters that have
        a direct ASCII mapping.
        'unicode' is a slightly slower method that works on any characters.
        None (default) does nothing.

        Both 'ascii' and 'unicode' use NFKD normalization from
        :func:`unicodedata.normalize`.

    lowercase : bool, default=True
        Convert all characters to lowercase before tokenizing.

    preprocessor : callable, default=None
        Override the preprocessing (string transformation) stage while
        preserving the tokenizing and n-grams generation steps.
        Only applies if ``analyzer`` is not callable.

    tokenizer : callable, default=None
        Override the string tokenization step while preserving the
        preprocessing and n-grams generation steps.
        Only applies if ``analyzer == 'word'``.

    analyzer : {'word', 'char', 'char_wb'} or callable, default='word'
        Whether the feature should be made of word or character n-grams.
        Option 'char_wb' creates character n-grams only from text inside
        word boundaries; n-grams at the edges of words are padded with space.

        If a callable is passed it is used to extract the sequence of features
        out of the raw, unprocessed input.

        .. versionchanged:: 0.21
            Since v0.21, if ``input`` is ``'filename'`` or ``'file'``, the data
            is first read from the file and then passed to the given callable
            analyzer.

    stop_words : {'english'}, list, default=None
        If a string, it is passed to _check_stop_list and the appropriate stop
        list is returned. 'english' is currently the only supported string
        value.
        There are several known issues with 'english' and you should
        consider an alternative (see :ref:`stop_words`).

        If a list, that list is assumed to contain stop words, all of which
        will be removed from the resulting tokens.
        Only applies if ``analyzer == 'word'``.

        If None, no stop words will be used. In this case, setting `max_df`
        to a higher value, such as in the range (0.7, 1.0), can automatically detect
        and filter stop words based on intra corpus document frequency of terms.

    token_pattern : str, default=r"(?u)\\b\\w\\w+\\b"
        Regular expression denoting what constitutes a "token", only used
        if ``analyzer == 'word'``. The default regexp selects tokens of 2
        or more alphanumeric characters (punctuation is completely ignored
        and always treated as a token separator).

        If there is a capturing group in token_pattern then the
        captured group content, not the entire match, becomes the token.
        At most one capturing group is permitted.

    ngram_range : tuple (min_n, max_n), default=(1, 1)
        The lower and upper boundary of the range of n-values for different
        n-grams to be extracted. All values of n such that min_n <= n <= max_n
        will be used. For example an ``ngram_range`` of ``(1, 1)`` means only
        unigrams, ``(1, 2)`` means unigrams and bigrams, and ``(2, 2)`` means
        only bigrams.
        Only applies if ``analyzer`` is not callable.

    max_df : float or int, default=1.0
        When building the vocabulary ignore terms that have a document
        frequency strictly higher than the given threshold (corpus-specific
        stop words).
        If float in range [0.0, 1.0], the parameter represents a proportion of
        documents, integer absolute counts.
        This parameter is ignored if vocabulary is not None.

    min_df : float or int, default=1
        When building the vocabulary ignore terms that have a document
        frequency strictly lower than the given threshold. This value is also
        called cut-off in the literature.
        If float in range of [0.0, 1.0], the parameter represents a proportion
        of documents, integer absolute counts.
        This parameter is ignored if vocabulary is not None.

    max_features : int, default=None
        If not None, build a vocabulary that only consider the top
        `max_features` ordered by term frequency across the corpus.
        Otherwise, all features are used.

        This parameter is ignored if vocabulary is not None.

    vocabulary : Mapping or iterable, default=None
        Either a Mapping (e.g., a dict) where keys are terms and values are
        indices in the feature matrix, or an iterable over terms. If not
        given, a vocabulary is determined from the input documents.

    binary : bool, default=False
        If True, all non-zero term counts are set to 1. This does not mean
        outputs will have only 0/1 values, only that the tf term in tf-idf
        is binary. (Set idf and normalization to False to get 0/1 outputs).

    dtype : dtype, default=float64
        Type of the matrix returned by fit_transform() or transform().

    norm : {'l1', 'l2'} or None, default='l2'
        Each output row will have unit norm, either:

        - 'l2': Sum of squares of vector elements is 1. The cosine
          similarity between two vectors is their dot product when l2 norm has
          been applied.
        - 'l1': Sum of absolute values of vector elements is 1.
          See :func:`preprocessing.normalize`.
        - None: No normalization.

    use_idf : bool, default=True
        Enable inverse-document-frequency reweighting. If False, idf(t) = 1.

    smooth_idf : bool, default=True
        Smooth idf weights by adding one to document frequencies, as if an
        extra document was seen containing every term in the collection
        exactly once. Prevents zero divisions.

    sublinear_tf : bool, default=False
        Apply sublinear tf scaling, i.e. replace tf with 1 + log(tf).

    Attributes
    ----------
    vocabulary_ : dict
        A mapping of terms to feature indices.

    fixed_vocabulary_ : bool
        True if a fixed vocabulary of term to indices mapping
        is provided by the user.

    idf_ : array of shape (n_features,)
        The inverse document frequency (IDF) vector; only defined
        if ``use_idf`` is True.

    stop_words_ : set
        Terms that were ignored because they either:

          - occurred in too many documents (`max_df`)
          - occurred in too few documents (`min_df`)
          - were cut off by feature selection (`max_features`).

        This is only available if no vocabulary was given.

    See Also
    --------
    CountVectorizer : Transforms text into a sparse matrix of n-gram counts.

    TfidfTransformer : Performs the TF-IDF transformation from a provided
        matrix of counts.

    Notes
    -----
    The ``stop_words_`` attribute can get large and increase the model size
    when pickling. This attribute is provided only for introspection and can
    be safely removed using delattr or set to None before pickling.

    Examples
    --------
    >>> from sklearn.feature_extraction.text import TfidfVectorizer
    >>> corpus = [
    ...     'This is the first document.',
    ...     'This document is the second document.',
    ...     'And this is the third one.',
    ...     'Is this the first document?',
    ... ]
    >>> vectorizer = TfidfVectorizer()
    >>> X = vectorizer.fit_transform(corpus)
    >>> vectorizer.get_feature_names_out()
    array(['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',
           'this'], ...)
    >>> print(X.shape)
    (4, 9)
    """

    _parameter_constraints: dict = {**CountVectorizer._parameter_constraints}
    _parameter_constraints.update(
        {
            "norm": [StrOptions({"l1", "l2"}), None],
            "use_idf": ["boolean"],
            "smooth_idf": ["boolean"],
            "sublinear_tf": ["boolean"],
        }
    )

    def __init__(
        self,
        *,
        input="content",
        encoding="utf-8",
        decode_error="strict",
        strip_accents=None,
        lowercase=True,
        preprocessor=None,
        tokenizer=None,
        analyzer="word",
        stop_words=None,
        token_pattern=r"(?u)\b\w\w+\b",
        ngram_range=(1, 1),
        max_df=1.0,
        min_df=1,
        max_features=None,
        vocabulary=None,
        binary=False,
        dtype=np.float64,
        norm="l2",
        use_idf=True,
        smooth_idf=True,
        sublinear_tf=False,
    ):

        super().__init__(
            input=input,
            encoding=encoding,
            decode_error=decode_error,
            strip_accents=strip_accents,
            lowercase=lowercase,
            preprocessor=preprocessor,
            tokenizer=tokenizer,
            analyzer=analyzer,
            stop_words=stop_words,
            token_pattern=token_pattern,
            ngram_range=ngram_range,
            max_df=max_df,
            min_df=min_df,
            max_features=max_features,
            vocabulary=vocabulary,
            binary=binary,
            dtype=dtype,
        )
        self.norm = norm
        self.use_idf = use_idf
        self.smooth_idf = smooth_idf
        self.sublinear_tf = sublinear_tf

    # Broadcast the TF-IDF parameters to the underlying transformer instance
    # for easy grid search and repr

    @property
    def idf_(self):
        """Inverse document frequency vector, only defined if `use_idf=True`.

        Returns
        -------
        ndarray of shape (n_features,)
        """
        if not hasattr(self, "_tfidf"):
            raise NotFittedError(
                f"{self.__class__.__name__} is not fitted yet. Call 'fit' with "
                "appropriate arguments before using this attribute."
            )
        return self._tfidf.idf_

    @idf_.setter
    def idf_(self, value):
        if not self.use_idf:
            raise ValueError("`idf_` cannot be set when `user_idf=False`.")
        if not hasattr(self, "_tfidf"):
            # We should support transferring `idf_` from another `TfidfTransformer`
            # and therefore, we need to create the transformer instance it does not
            # exist yet.
            self._tfidf = TfidfTransformer(
                norm=self.norm,
                use_idf=self.use_idf,
                smooth_idf=self.smooth_idf,
                sublinear_tf=self.sublinear_tf,
            )
        self._validate_vocabulary()
        if hasattr(self, "vocabulary_"):
            if len(self.vocabulary_) != len(value):
                raise ValueError(
                    "idf length = %d must be equal to vocabulary size = %d"
                    % (len(value), len(self.vocabulary))
                )
        self._tfidf.idf_ = value

    def _check_params(self):
        if self.dtype not in FLOAT_DTYPES:
            warnings.warn(
                "Only {} 'dtype' should be used. {} 'dtype' will "
                "be converted to np.float64.".format(FLOAT_DTYPES, self.dtype),
                UserWarning,
            )

    def fit(self, raw_documents, y=None):
        """Learn vocabulary and idf from training set.

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        y : None
            This parameter is not needed to compute tfidf.

        Returns
        -------
        self : object
            Fitted vectorizer.
        """
        self._validate_params()
        self._check_params()
        self._warn_for_unused_params()
        self._tfidf = TfidfTransformer(
            norm=self.norm,
            use_idf=self.use_idf,
            smooth_idf=self.smooth_idf,
            sublinear_tf=self.sublinear_tf,
        )
        X = super().fit_transform(raw_documents)
        self._tfidf.fit(X)
        return self

    def fit_transform(self, raw_documents, y=None):
        """Learn vocabulary and idf, return document-term matrix.

        This is equivalent to fit followed by transform, but more efficiently
        implemented.

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        y : None
            This parameter is ignored.

        Returns
        -------
        X : sparse matrix of (n_samples, n_features)
            Tf-idf-weighted document-term matrix.
        """
        self._check_params()
        self._tfidf = TfidfTransformer(
            norm=self.norm,
            use_idf=self.use_idf,
            smooth_idf=self.smooth_idf,
            sublinear_tf=self.sublinear_tf,
        )
        X = super().fit_transform(raw_documents)
        self._tfidf.fit(X)
        # X is already a transformed view of raw_documents so
        # we set copy to False
        return self._tfidf.transform(X, copy=False)

    def transform(self, raw_documents):
        """Transform documents to document-term matrix.

        Uses the vocabulary and document frequencies (df) learned by fit (or
        fit_transform).

        Parameters
        ----------
        raw_documents : iterable
            An iterable which generates either str, unicode or file objects.

        Returns
        -------
        X : sparse matrix of (n_samples, n_features)
            Tf-idf-weighted document-term matrix.
        """
        check_is_fitted(self, msg="The TF-IDF vectorizer is not fitted")

        X = super().transform(raw_documents)
        return self._tfidf.transform(X, copy=False)

    def _more_tags(self):
        return {"X_types": ["string"], "_skip_test": True}
