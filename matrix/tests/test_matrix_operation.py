"""
Testing here assumes that numpy and linalg is ALWAYS correct!!!!

If running from PyCharm you can place the following line in "Additional Arguments" for the pytest run configuration
-vv -m mat_ops -p no:cacheprovider
"""

# standard libraries
import sys
import numpy as np
import pytest
import logging

# Custom/local libraries
from matrix import matrix_operation as matop

mat_a = [[12, 10], [3, 9]]
mat_b = [[3, 4], [7, 4]]
mat_c = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
mat_d = [[3, 0, -2], [2, 0, 2], [0, 1, 1]]
mat_e = [[3, 0, 2], [2, 0, -2], [0, 1, 1], [2, 0, -2]]
mat_f = [1]
mat_h = [2]

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_addition(mat1, mat2):
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        with pytest.raises(TypeError):
            logger.info(f"\n\t{test_addition.__name__} returned integer")
            matop.add(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        logger.info(f"\n\t{test_addition.__name__} with same matrix dims")
        act = (np.array(mat1) + np.array(mat2)).tolist()
        theo = matop.add(mat1, mat2)
        assert theo == act
    else:
        with pytest.raises(ValueError):
            logger.info(f"\n\t{test_addition.__name__} with different matrix dims")
            matop.add(mat1, mat2)


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_subtraction(mat1, mat2):
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        with pytest.raises(TypeError):
            logger.info(f"\n\t{test_subtraction.__name__} returned integer")
            matop.subtract(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        logger.info(f"\n\t{test_subtraction.__name__} with same matrix dims")
        act = (np.array(mat1) - np.array(mat2)).tolist()
        theo = matop.subtract(mat1, mat2)
        assert theo == act
    else:
        with pytest.raises(ValueError):
            logger.info(f"\n\t{test_subtraction.__name__} with different matrix dims")
            assert matop.subtract(mat1, mat2)


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_multiplication(mat1, mat2):
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        logger.info(f"\n\t{test_multiplication.__name__} returned integer")
        with pytest.raises(TypeError):
            matop.add(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        logger.info(f"\n\t{test_multiplication.__name__} meets dim requirements")
        act = (np.matmul(mat1, mat2)).tolist()
        theo = matop.multiply(mat1, mat2)
        assert theo == act
    else:
        with pytest.raises(ValueError):
            logger.info(f"\n\t{test_multiplication.__name__} does not meet dim requirements")
            assert matop.subtract(mat1, mat2)


@pytest.mark.mat_ops
def test_scalar_multiply():
    act = (3.5 * np.array(mat_a)).tolist()
    theo = matop.scalar_multiply(mat_a, 3.5)
    assert theo == act


@pytest.mark.mat_ops
def test_identity():
    act = (np.identity(5)).tolist()
    theo = matop.identity(5)
    assert theo == act


@pytest.mark.mat_ops
@pytest.mark.parametrize('mat', [mat_a, mat_b, mat_c, mat_d, mat_e, mat_f])
def test_transpose(mat):
    if (np.array(mat)).shape < (2, 2):
        with pytest.raises(TypeError):
            logger.info(f"\n\t{test_transpose.__name__} returned integer")
            matop.transpose(mat)
    else:
        act = (np.transpose(mat)).tolist()
        theo = matop.transpose(mat, return_map=False)
        assert theo == act
