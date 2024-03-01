# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Functions for downloading and reading MNIST data (deprecated).

This module and all its submodules are deprecated.
"""


import collections
import gzip
import os
import urllib

import numpy
from tensorflow.python.framework import dtypes, random_seed
from tensorflow.python.platform import gfile
from tensorflow.python.util.deprecation import deprecated

_Datasets = collections.namedtuple("_Datasets", ["train", "validation", "test"])

# CVDF mirror of http://yann.lecun.com/exdb/mnist/
DEFAULT_SOURCE_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"


def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder(">")
    return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]


@deprecated(None, "Please use tf.data to implement this functionality.")
def _extract_images(f):
    """Extract the images into a 4D uint8 numpy array [index, y, x, depth].

    Args:
      f: A file object that can be passed into a gzip reader.

    Returns:
      data: A 4D uint8 numpy array [index, y, x, depth].

    Raises:
      ValueError: If the bytestream does not start with 2051.

    """
    print("Extracting", f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        if magic != 2051:
            raise ValueError(
                "Invalid magic number %d in MNIST image file: %s" % (magic, f.name)
            )
        num_images = _read32(bytestream)
        rows = _read32(bytestream)
        cols = _read32(bytestream)
        buf = bytestream.read(rows * cols * num_images)
        data = numpy.frombuffer(buf, dtype=numpy.uint8)
        data = data.reshape(num_images, rows, cols, 1)
        return data


@deprecated(None, "Please use tf.one_hot on tensors.")
def _dense_to_one_hot(labels_dense, num_classes):
    """Convert class labels from scalars to one-hot vectors."""
    num_labels = labels_dense.shape[0]
    index_offset = numpy.arange(num_labels) * num_classes
    labels_one_hot = numpy.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot


@deprecated(None, "Please use tf.data to implement this functionality.")
def _extract_labels(f, one_hot=False, num_classes=10):
    """Extract the labels into a 1D uint8 numpy array [index].

    Args:
      f: A file object that can be passed into a gzip reader.
      one_hot: Does one hot encoding for the result.
      num_classes: Number of classes for the one hot encoding.

    Returns:
      labels: a 1D uint8 numpy array.

    Raises:
      ValueError: If the bystream doesn't start with 2049.
    """
    print("Extracting", f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        if magic != 2049:
            raise ValueError(
                "Invalid magic number %d in MNIST label file: %s" % (magic, f.name)
            )
        num_items = _read32(bytestream)
        buf = bytestream.read(num_items)
        labels = numpy.frombuffer(buf, dtype=numpy.uint8)
        if one_hot:
            return _dense_to_one_hot(labels, num_classes)
        return labels


class _DataSet:
    """Container class for a _DataSet (deprecated).

    THIS CLASS IS DEPRECATED.
    """

    @deprecated(
        None,
        "Please use alternatives such as official/mnist/_DataSet.py"
        " from tensorflow/models.",
    )
    def __init__(
        self,
        images,
        labels,
        fake_data=False,
        one_hot=False,
        dtype=dtypes.float32,
        reshape=True,
        seed=None,
    ):
        """Construct a _DataSet.

        one_hot arg is used only if fake_data is true.  `dtype` can be either
        `uint8` to leave the input as `[0, 255]`, or `float32` to rescale into
        `[0, 1]`.  Seed arg provides for convenient deterministic testing.

        Args:
          images: The images
          labels: The labels
          fake_data: Ignore inages and labels, use fake data.
          one_hot: Bool, return the labels as one hot vectors (if True) or ints (if
            False).
          dtype: Output image dtype. One of [uint8, float32]. `uint8` output has
            range [0,255]. float32 output has range [0,1].
          reshape: Bool. If True returned images are returned flattened to vectors.
          seed: The random seed to use.
        """
        seed1, seed2 = random_seed.get_seed(seed)
        # If op level seed is not set, use whatever graph level seed is returned
        numpy.random.seed(seed1 if seed is None else seed2)
        dtype = dtypes.as_dtype(dtype).base_dtype
        if dtype not in (dtypes.uint8, dtypes.float32):
            raise TypeError("Invalid image dtype %r, expected uint8 or float32" % dtype)
        if fake_data:
            self._num_examples = 10000
            self.one_hot = one_hot
        else:
            assert (
                images.shape[0] == labels.shape[0]
            ), f"images.shape: {images.shape} labels.shape: {labels.shape}"
            self._num_examples = images.shape[0]

            # Convert shape from [num examples, rows, columns, depth]
            # to [num examples, rows*columns] (assuming depth == 1)
            if reshape:
                assert images.shape[3] == 1
                images = images.reshape(
                    images.shape[0], images.shape[1] * images.shape[2]
                )
            if dtype == dtypes.float32:
                # Convert from [0, 255] -> [0.0, 1.0].
                images = images.astype(numpy.float32)
                images = numpy.multiply(images, 1.0 / 255.0)
        self._images = images
        self._labels = labels
        self._epochs_completed = 0
        self._index_in_epoch = 0

    @property
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size, fake_data=False, shuffle=True):
        """Return the next `batch_size` examples from this data set."""
        if fake_data:
            fake_image = [1] * 784
            fake_label = [1] + [0] * 9 if self.one_hot else 0
            return (
                [fake_image for _ in range(batch_size)],
                [fake_label for _ in range(batch_size)],
            )
        start = self._index_in_epoch
        # Shuffle for the first epoch
        if self._epochs_completed == 0 and start == 0 and shuffle:
            perm0 = numpy.arange(self._num_examples)
            numpy.random.shuffle(perm0)
            self._images = self.images[perm0]
            self._labels = self.labels[perm0]
        # Go to the next epoch
        if start + batch_size > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Get the rest examples in this epoch
            rest_num_examples = self._num_examples - start
            images_rest_part = self._images[start : self._num_examples]
            labels_rest_part = self._labels[start : self._num_examples]
            # Shuffle the data
            if shuffle:
                perm = numpy.arange(self._num_examples)
                numpy.random.shuffle(perm)
                self._images = self.images[perm]
                self._labels = self.labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size - rest_num_examples
            end = self._index_in_epoch
            images_new_part = self._images[start:end]
            labels_new_part = self._labels[start:end]
            return (
                numpy.concatenate((images_rest_part, images_new_part), axis=0),
                numpy.concatenate((labels_rest_part, labels_new_part), axis=0),
            )
        else:
            self._index_in_epoch += batch_size
            end = self._index_in_epoch
            return self._images[start:end], self._labels[start:end]


@deprecated(None, "Please write your own downloading logic.")
def _maybe_download(filename, work_directory, source_url):
    """Download the data from source url, unless it's already here.

    Args:
        filename: string, name of the file in the directory.
        work_directory: string, path to working directory.
        source_url: url to download from if file doesn't exist.

    Returns:
        Path to resulting file.
    """
    if not gfile.Exists(work_directory):
        gfile.MakeDirs(work_directory)
    filepath = os.path.join(work_directory, filename)
    if not gfile.Exists(filepath):
        urllib.request.urlretrieve(source_url, filepath)  # noqa: S310
        with gfile.GFile(filepath) as f:
            size = f.size()
        print("Successfully downloaded", filename, size, "bytes.")
    return filepath


@deprecated(None, "Please use alternatives such as: tensorflow_datasets.load('mnist')")
def read_data_sets(
    train_dir,
    fake_data=False,
    one_hot=False,
    dtype=dtypes.float32,
    reshape=True,
    validation_size=5000,
    seed=None,
    source_url=DEFAULT_SOURCE_URL,
):
    if fake_data:

        def fake():
            return _DataSet(
                [], [], fake_data=True, one_hot=one_hot, dtype=dtype, seed=seed
            )

        train = fake()
        validation = fake()
        test = fake()
        return _Datasets(train=train, validation=validation, test=test)

    if not source_url:  # empty string check
        source_url = DEFAULT_SOURCE_URL

    train_images_file = "train-images-idx3-ubyte.gz"
    train_labels_file = "train-labels-idx1-ubyte.gz"
    test_images_file = "t10k-images-idx3-ubyte.gz"
    test_labels_file = "t10k-labels-idx1-ubyte.gz"

    local_file = _maybe_download(
        train_images_file, train_dir, source_url + train_images_file
    )
    with gfile.Open(local_file, "rb") as f:
        train_images = _extract_images(f)

    local_file = _maybe_download(
        train_labels_file, train_dir, source_url + train_labels_file
    )
    with gfile.Open(local_file, "rb") as f:
        train_labels = _extract_labels(f, one_hot=one_hot)

    local_file = _maybe_download(
        test_images_file, train_dir, source_url + test_images_file
    )
    with gfile.Open(local_file, "rb") as f:
        test_images = _extract_images(f)

    local_file = _maybe_download(
        test_labels_file, train_dir, source_url + test_labels_file
    )
    with gfile.Open(local_file, "rb") as f:
        test_labels = _extract_labels(f, one_hot=one_hot)

    if not 0 <= validation_size <= len(train_images):
        msg = (
            "Validation size should be between 0 and "
            f"{len(train_images)}. Received: {validation_size}."
        )
        raise ValueError(msg)

    validation_images = train_images[:validation_size]
    validation_labels = train_labels[:validation_size]
    train_images = train_images[validation_size:]
    train_labels = train_labels[validation_size:]

    options = {"dtype": dtype, "reshape": reshape, "seed": seed}

    train = _DataSet(train_images, train_labels, **options)
    validation = _DataSet(validation_images, validation_labels, **options)
    test = _DataSet(test_images, test_labels, **options)

    return _Datasets(train=train, validation=validation, test=test)
