import numpy as np


def matrix_multiplication(f_matrix: np.ndarray, s_matrix: np.ndarray):
    result = np.dot(f_matrix, s_matrix)
    return result


def multiplication_check(matrix_list: list):
    try:
        if len(matrix_list) == 1:
            return matrix_list[0]
        np.dot(multiplication_check(matrix_list[:-1]), matrix_list[-1])
    except ValueError:
        return False
    else:
        return True


def multiply_matrices(matrix_list: list):
    try:
        if len(matrix_list) == 1:
            return matrix_list[0]
        return np.dot(multiply_matrices(matrix_list[:-1]), matrix_list[-1])
    except ValueError:
        return None


def compute_multidimensional_distance(point1: np.ndarray, point2: np.ndarray):
    distance = np.linalg.norm(point1 - point2)
    return distance


def compute_2d_distance(point1: np.ndarray, point2: np.ndarray):
    return compute_multidimensional_distance(point1, point2)


def compute_pair_distances(two_d_array: np.ndarray):
    arr_shape = two_d_array.reshape(two_d_array.shape[0], 1, two_d_array.shape[1])
    pair_mat = np.sqrt(np.einsum("ijk,ijk->ij", two_d_array - arr_shape, two_d_array - arr_shape))
    return pair_mat


if __name__ == "__main__":
    range_array = np.arange(394)
    random_array = np.random.random((7, 13))
    one_array = np.ones((22, 6))
