import pytest
from code_vars_task.sum_of_intervals import sum_of_intervals


class TestCase:

    @pytest.mark.parametrize('intervals, result', (
            [[(1, 5)], 4],
            [[(1, 5), (6, 10)], 8],
            [[(1, 5), (1, 5)], 4],
            [[(1, 4), (7, 10), (3, 5)], 7],
            [[(-1000000000, 1000000000)], 2000000000],
            [[(0, 20), (-100_000_000, 10), (30, 40)], 100_000_030]
    ))
    def test_sum_of_intervals(self, intervals, result):
        assert sum_of_intervals(intervals) == result

