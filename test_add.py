import pytest
import add_ex

def test_sum():
    assert add_ex.sum_num(1,2) == 3

def test_sum_output_type():
    assert type(add_ex.sum_num(1,2)) is int

# Parametrizing test method
# to perform multiple call to same test function
# here pass arguments as a string and values as a list of tuples.
@pytest.mark.parametrize('num1, num2, expected', [(3,5,8),(-5,19,14)])
def test_sum_other_para(num1, num2, expected):
    assert add_ex.sum_num(num1, num2) == expected
# The above method, we can also represent by using another function of data
def get_sum_test_data_para():
    return [(3,5,8),(8,10,18)]
@pytest.mark.parametrize('num1, num2, expected', get_sum_test_data_para())
def test_sum_other_para_othr(num1, num2, expected):
    assert add_ex.sum_num(num1, num2) == expected

if __name__=='__main__':
    pytest.main()