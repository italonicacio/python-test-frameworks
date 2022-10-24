import pytest

def sum_arr(arr1, arr2):
    
    if len(arr1) != len(arr2):
        raise ValueError("Arr1 e Arr2 tem tamanhos diferentes!")
    
    return [arr1[i] + arr2[i] for i in range(len(arr1))]


def test_sum_arr_value_error_len():
    arr1 = [1, 2, 3]
    arr2 = [4, 5]

    with pytest.raises(ValueError, match=r"Arr1 e Arr2 tem tamanhos diferentes!"):
        sum_arr(arr1, arr2)

def test_sum_arr_check_sum_arr():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]

    assert sum_arr(arr1, arr2) == [5, 7, 9]