#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Metadata about languages used by our model training code for our
SingleByteCharSetProbers.  Could be used for other things in the future.

This code is based on the language metadata from the uchardet project.
"""
from __future__ import absolute_import, print_function

from string import ascii_letters


# TODO: Add Ukranian (KOI8-U)

class Language(object):
    """Metadata about a language useful for training models

    :ivar name: The human name for the language, in English.
    :type name: str
    :ivar iso_code: 2-letter ISO 639-1 if possible, 3-letter ISO code otherwise,
                    or use another catalog as a last resort.
    :type iso_code: str
    :ivar use_ascii: Whether or not ASCII letters should be included in trained
                     models.
    :type use_ascii: bool
    :ivar charsets: The charsets we want to support and create data for.
    :type charsets: list of str
    :ivar alphabet: The characters in the language's alphabet. If `use_ascii` is
                    `True`, you only need to add those not in the ASCII set.
    :type alphabet: str
    :ivar wiki_start_pages: The Wikipedia pages to start from if we're crawling
                            Wikipedia for training data.
    :type wiki_start_pages: list of str
    """
    def __init__(self, name=None, iso_code=None, use_ascii=True, charsets=None,
                 alphabet=None, wiki_start_pages=None):
        super(Language, self).__init__()
        self.name = name
        self.iso_code = iso_code
        self.use_ascii = use_ascii
        self.charsets = charsets
        if self.use_ascii:
            if alphabet:
                alphabet += ascii_letters
            else:
                alphabet = ascii_letters
        elif not alphabet:
            raise ValueError('Must supply alphabet if use_ascii is False')
        self.alphabet = ''.join(sorted(set(alphabet))) if alphabet else None
        self.wiki_start_pages = wiki_start_pages

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ', '.join('{}={!r}'.format(k, v)
                                         for k, v in self.__dict__.items()
                                         if not k.startswith('_')))


LANGUAGES = {'Arabic': Language(name='Arabic',
                                iso_code='ar',
                                use_ascii=False,
                                # We only support encodings that use isolated
                                # forms, because the current recommendation is
                                # that the rendering system handles presentation
                                # forms. This means we purposefully skip IBM864.
                                charsets=['ISO-8859-6', 'WINDOWS-1256',
                                          'CP720', 'CP864'],
                                alphabet=u'ءآأؤإئابةتثجحخدذرزسشصضطظعغػؼؽؾؿـفقكلمنهوىيًٌٍَُِّ',
                                wiki_start_pages=[u'الصفحة_الرئيسية']),
             'Belarusian': Language(name='Belarusian',
                                    iso_code='be',
                                    use_ascii=False,
                                    charsets=['ISO-8859-5', 'WINDOWS-1251',
                                              'IBM866', 'MacCyrillic'],
                                    alphabet=(u'АБВГДЕЁЖЗІЙКЛМНОПРСТУЎФХЦЧШЫЬЭЮЯ'
                                              u'абвгдеёжзійклмнопрстуўфхцчшыьэюяʼ'),
                                    wiki_start_pages=[u'Галоўная_старонка']),
             'Bulgarian': Language(name='Bulgarian',
                                   iso_code='bg',
                                   use_ascii=False,
                                   charsets=['ISO-8859-5', 'WINDOWS-1251',
                                             'IBM855'],
                                   alphabet=(u'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯ'
                                             u'абвгдежзийклмнопрстуфхцчшщъьюя'),
                                   wiki_start_pages=[u'Начална_страница']),
             'Czech': Language(name='Czech',
                               iso_code='cz',
                               use_ascii=True,
                               charsets=['ISO-8859-2', 'WINDOWS-1250'],
                               alphabet=u'áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ',
                               wiki_start_pages=[u'Hlavní_strana']),
             'Danish': Language(name='Danish',
                                iso_code='da',
                                use_ascii=True,
                                charsets=['ISO-8859-1', 'ISO-8859-15',
                                          'WINDOWS-1252'],
                                alphabet=u'æøåÆØÅ',
                                wiki_start_pages=[u'Forside']),
             'German': Language(name='German',
                                iso_code='de',
                                use_ascii=True,
                                charsets=['ISO-8859-1', 'WINDOWS-1252'],
                                alphabet=u'äöüßÄÖÜ',
                                wiki_start_pages=[u'Wikipedia:Hauptseite']),
             'Greek': Language(name='Greek',
                               iso_code='el',
                               use_ascii=False,
                               charsets=['ISO-8859-7', 'WINDOWS-1253'],
                               alphabet=(u'αβγδεζηθικλμνξοπρσςτυφχψωάέήίόύώ'
                                         u'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩΆΈΉΊΌΎΏ'),
                               wiki_start_pages=[u'Πύλη:Κύρια']),
             'English': Language(name='English',
                                 iso_code='en',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'WINDOWS-1252'],
                                 wiki_start_pages=[u'Main_Page']),
             'Esperanto': Language(name='Esperanto',
                                   iso_code='eo',
                                   # Q, W, X, and Y not used at all
                                   use_ascii=False,
                                   charsets=['ISO-8859-3'],
                                   alphabet=(u'abcĉdefgĝhĥijĵklmnoprsŝtuŭvz'
                                             u'ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ'),
                                   wiki_start_pages=[u'Vikipedio:Ĉefpaĝo']),
             'Spanish': Language(name='Spanish',
                                 iso_code='es',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'ISO-8859-15',
                                           'WINDOWS-1252'],
                                 alphabet=u'ñáéíóúüÑÁÉÍÓÚÜ',
                                 wiki_start_pages=[u'Wikipedia:Portada']),
             'Estonian': Language(name='Estonian',
                                  iso_code='et',
                                  use_ascii=False,
                                  charsets=['ISO-8859-4', 'ISO-8859-13',
                                            'WINDOWS-1257'],
                                  # C, F, Š, Q, W, X, Y, Z, Ž are only for
                                  # loanwords
                                  alphabet=(u'ABDEGHIJKLMNOPRSTUVÕÄÖÜ'
                                            u'abdeghijklmnoprstuvõäöü'),
                                  wiki_start_pages=[u'Esileht']),
             'Finnish': Language(name='Finnish',
                                 iso_code='fi',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'ISO-8859-15',
                                           'WINDOWS-1252'],
                                 alphabet=u'ÅÄÖŠŽåäöšž',
                                 wiki_start_pages=[u'Wikipedia:Etusivu']),
             'French': Language(name='French',
                                iso_code='fr',
                                use_ascii=True,
                                charsets=['ISO-8859-1', 'ISO-8859-15',
                                          'WINDOWS-1252'],
                                alphabet=u'œàâçèéîïùûêŒÀÂÇÈÉÎÏÙÛÊ',
                                wiki_start_pages=[u'Wikipédia:Accueil_principal',
                                                  u'Bœuf (animal)']),
             'Hebrew': Language(name='Hebrew',
                                iso_code='he',
                                use_ascii=False,
                                charsets=['ISO-8859-8', 'WINDOWS-1255'],
                                alphabet=u'אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ',
                                wiki_start_pages=[u'עמוד_ראשי']),
             'Croatian': Language(name='Croatian',
                                  iso_code='hr',
                                  # Q, W, X, Y are only used for foreign words.
                                  use_ascii=False,
                                  charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                  alphabet=(u'abcčćdđefghijklmnoprsštuvzž'
                                            u'ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ'),
                                  wiki_start_pages=[u'Glavna_stranica']),
             'Hungarian': Language(name='Hungarian',
                                   iso_code='hu',
                                   # Q, W, X, Y are only used for foreign words.
                                   use_ascii=False,
                                   charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                   alphabet=(u'abcdefghijklmnoprstuvzáéíóöőúüű'
                                             u'ABCDEFGHIJKLMNOPRSTUVZÁÉÍÓÖŐÚÜŰ'),
                                   wiki_start_pages=[u'Kezdőlap']),
             'Italian': Language(name='Italian',
                                 iso_code='it',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'ISO-8859-15',
                                           'WINDOWS-1252'],
                                 alphabet=u'ÀÈÉÌÒÓÙàèéìòóù',
                                 wiki_start_pages=[u'Pagina_principale']),
             'Lithuanian': Language(name='Lithuanian',
                                    iso_code='lt',
                                    use_ascii=False,
                                    charsets=['ISO-8859-13', 'WINDOWS-1257',
                                              'ISO-8859-4'],
                                    # Q, W, and X not used at all
                                    alphabet=(u'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
                                              u'aąbcčdeęėfghiįyjklmnoprsštuųūvzž'),
                                    wiki_start_pages=[u'Pagrindinis_puslapis']),
             'Latvian': Language(name='Latvian',
                                 iso_code='lv',
                                 use_ascii=False,
                                 charsets=['ISO-8859-13', 'WINDOWS-1257',
                                           'ISO-8859-4'],
                                 # Q, W, X, Y are only for loanwords
                                 alphabet=(u'AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽ'
                                           u'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'),
                                 wiki_start_pages=[u'Sākumlapa']),
             'Macedonian': Language(name='Macedonian',
                                    iso_code='mk',
                                    use_ascii=False,
                                    charsets=['ISO-8859-5', 'WINDOWS-1251',
                                              'MacCyrillic', 'IBM855'],
                                    alphabet=(u'АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ'
                                              u'абвгдѓежзѕијклљмнњопрстќуфхцчџш'),
                                    wiki_start_pages=[u'Главна_страница']),
             'Dutch': Language(name='Dutch',
                               iso_code='nl',
                               use_ascii=True,
                               charsets=['ISO-8859-1', 'WINDOWS-1252'],
                               wiki_start_pages=[u'Hoofdpagina']),
             'Polish': Language(name='Polish',
                                iso_code='pl',
                                # Q and X are only used for foreign words.
                                use_ascii=False,
                                charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                alphabet=(u'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
                                          u'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'),
                                wiki_start_pages=[u'Wikipedia:Strona_główna']),
             'Portuguese': Language(name='Portuguese',
                                 iso_code='pt',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'ISO-8859-15',
                                           'WINDOWS-1252'],
                                 alphabet=u'ÁÂÃÀÇÉÊÍÓÔÕÚáâãàçéêíóôõú',
                                 wiki_start_pages=[u'Wikipédia:Página_principal']),
             'Romanian': Language(name='Romanian',
                                  iso_code='ro',
                                  use_ascii=True,
                                  charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                  alphabet=u'ăâîșțĂÂÎȘȚ',
                                  wiki_start_pages=[u'Pagina_principală']),
             'Russian': Language(name='Russian',
                                 iso_code='ru',
                                 use_ascii=False,
                                 charsets=['ISO-8859-5', 'WINDOWS-1251',
                                           'KOI8-R', 'MacCyrillic', 'IBM866',
                                           'IBM855'],
                                 alphabet=(u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                           u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'),
                                 wiki_start_pages=[u'Заглавная_страница']),
             'Slovak': Language(name='Slovak',
                                iso_code='sk',
                                use_ascii=True,
                                charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                alphabet=u'áäčďéíĺľňóôŕšťúýžÁÄČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ',
                                wiki_start_pages=[u'Hlavná_stránka']),
             'Slovene': Language(name='Slovene',
                                 iso_code='sl',
                                 # Q, W, X, Y are only used for foreign words.
                                 use_ascii=False,
                                 charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                 alphabet=(u'abcčdefghijklmnoprsštuvzž'
                                           u'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'),
                                 wiki_start_pages=[u'Glavna_stran']),
             # Serbian can be written in both Latin and Cyrillic, but there's no
             # simple way to get the Latin alphabet pages from Wikipedia through
             # the API, so for now we just support Cyrillic.
             'Serbian': Language(name='Serbian',
                                 iso_code='sr',
                                 alphabet=(u'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ'
                                           u'абвгдђежзијклљмнњопрстћуфхцчџш'),
                                 charsets=['ISO-8859-5', 'WINDOWS-1251',
                                           'MacCyrillic', 'IBM855'],
                                 wiki_start_pages=[u'Главна_страна']),
             'Thai': Language(name='Thai',
                              iso_code='th',
                              use_ascii=False,
                              charsets=['ISO-8859-11', 'TIS-620', 'CP874'],
                              alphabet=u'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯะัาำิีึืฺุู฿เแโใไๅๆ็่้๊๋์ํ๎๏๐๑๒๓๔๕๖๗๘๙๚๛',
                              wiki_start_pages=[u'หน้าหลัก']),
             'Turkish': Language(name='Turkish',
                                 iso_code='tr',
                                 # Q, W, and X are not used by Turkish
                                 use_ascii=False,
                                 charsets=['ISO-8859-3', 'ISO-8859-9',
                                           'WINDOWS-1254'],
                                 alphabet=(u'abcçdefgğhıijklmnoöprsştuüvyzâîû'
                                           u'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZÂÎÛ'),
                                 wiki_start_pages=[u'Ana_Sayfa']),
             'Vietnamese': Language(name='Vietnamese',
                                    iso_code='vi',
                                    use_ascii=False,
                                    # Windows-1258 is the only common 8-bit
                                    # Vietnamese encoding supported by Python.
                                    # From Wikipedia:
                                    # For systems that lack support for Unicode,
                                    # dozens of 8-bit Vietnamese code pages are
                                    # available.[1] The most common are VISCII
                                    # (TCVN 5712:1993), VPS, and Windows-1258.[3]
                                    # Where ASCII is required, such as when
                                    # ensuring readability in plain text e-mail,
                                    # Vietnamese letters are often encoded
                                    # according to Vietnamese Quoted-Readable
                                    # (VIQR) or VSCII Mnemonic (VSCII-MNEM),[4]
                                    # though usage of either variable-width
                                    # scheme has declined dramatically following
                                    # the adoption of Unicode on the World Wide
                                    # Web.
                                    charsets=['WINDOWS-1258'],
                                    alphabet=(u'aăâbcdđeêghiklmnoôơpqrstuưvxy'
                                              u'AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY'),
                                    wiki_start_pages=[u'Chữ_Quốc_ngữ']),
            }
