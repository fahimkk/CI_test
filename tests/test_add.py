import pytest
import add_ex

def test_sum():
    assert add_ex.sum_num(1,2) == 3
    assert add_ex.sum_num(2,2) == 4

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
    return [(3,5,8),(8,10,18),(-5,-9,-14),(-48,100,52),(-83,3,-80)]
@pytest.mark.parametrize('num1, num2, expected', get_sum_test_data_para())
def test_sum_other_para_othr(num1, num2, expected):
    assert add_ex.sum_num(num1, num2) == expected

    # Fixtures
# Fixtures can be used to share test data btw test, 
# execute setup and teardown methods
@pytest.fixture
def get_sum_test_data_fixture():
    return [(3,5,8),(8,10,18),(-5,-9,-14),(-48,100,52),(-83,3,-80)]
def test_sum_other_fixture(get_sum_test_data_fixture):
    for data in get_sum_test_data_fixture:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert add_ex.sum_num(num1, num2) == expected

# setup and teardown function
# scope - how often a fixture gets called
    # function - run once per test
    # class - run once per class of tests
    # module - run once per module
    # session - run once per session
@pytest.fixture(scope='session')
def get_sum_test_data_fixture_scope():
    return [(3,5,8),(8,10,18),(-5,-9,-14),(-48,100,52),(-83,3,-80)]
@pytest.fixture(autouse=True)
# autouse=True- will make every tesst in your suite use it by default
# ie we dont have to pass setup_and_teardown function as parameter to
# test_sum_fixture function, they will automatically called before and after
def setup_and_teardown():
    print('\nFetching data from db')
    yield
    # anything written after yield will executed ater the tests finishes
    print('\nSaving test run data in db')
def test_sum_fixture(get_sum_test_data_fixture):
    for data in get_sum_test_data_fixture:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert add_ex.sum_num(num1, num2) == expected


if __name__=='__main__':
    pytest.main()