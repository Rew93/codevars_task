import pytest
from code_vars_task.find_outlier import find_outlier


class TestCase:

    @pytest.mark.parametrize('list, number', (
        [[2, 4, 6, 8, 10, 3], 3],
        [[2, 4, 0, 100, 4, 11, 2602, 36], 11],
        [[160, 3, 1719, 19, 11, 13, -21], 160],
    ))
    def test_fint_outlier(self, list, number):
        assert find_outlier(list) == number