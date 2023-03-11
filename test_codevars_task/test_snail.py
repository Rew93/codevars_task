import pytest
from code_vars_task.snail import snail


class TestCase:

    @pytest.mark.parametrize('matrix, lst', (
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
            [[[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    ))
    def test_snail(self, matrix, lst):
        assert snail(matrix) == lst
