import pytest
from code_vars_task.multiples_of_3_or_5 import solution


class TestSolution:

    @pytest.mark.parametrize('number, result', ([3, 0],
                                                [6, 8],
                                                [16, 60],
                                                [4, 3],
                                                [5, 3],
                                                [15, 45],
                                                [0, 0],
                                                [-1, 0],
                                                [10, 23],
                                                [20, 78],
                                                [200, 9168],
                                                ))
    def test_one(self, number, result):
        assert solution(number) == result

