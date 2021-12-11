import statistical_analysis.principal_component_analysis as pca
import numpy as np
import pytest



matrix = np.array([[1, 0], [2, 1], [3, 2], [4, 3]])
result = np.array([[-2.12132034e+00,  2.22044605e-16],
           [-7.07106781e-01,  5.55111512e-17],
           [ 7.07106781e-01, -5.55111512e-17],
           [ 2.12132034e+00, -2.22044605e-16]])


@pytest.mark.stat_pca
@pytest.mark.parametrize(
    ("mat1", "result"), [(matrix, result)]
)
def test_pca(mat1, result):
    my_pca_result = pca.principal_comoponent_analysis(mat1, 2)

    assert np.allclose(my_pca_result, result)
