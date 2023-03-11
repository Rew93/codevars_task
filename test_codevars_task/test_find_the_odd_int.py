import pytest
from code_vars_task.find_the_odd_int import find_it


class TestFind:

    @pytest.mark.parametrize('seq, answer', ([[1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1], 4],
                                             [[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5],
                                             [[1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], -1],
                                             [[20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], 5],
                                             [[10], 10],
                                             [[10, 10, 10], 10],
                                             [[1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1], 10],
                                             [[5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10], 1],
                                             [[0], 0]))
    def test_find_it(self, answer, seq):
        assert find_it(seq) == answer





