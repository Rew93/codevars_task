import pytest
from code_vars_task.range_extraction import solution


class TestCase:

    @pytest.mark.parametrize('lst, result', (
            [[-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], '-6,-3-1,3-5,7-11,14,15,17-20'],
            [[-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], '-3--1,2,10,15,16,18-20'],
    ))
    def test_solution(self, lst, result):
        assert solution(lst) == result
