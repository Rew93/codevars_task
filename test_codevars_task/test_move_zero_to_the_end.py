import pytest
from code_vars_task.move_zero_to_the_end import move_zeros


class TestCase:

    @pytest.mark.parametrize('list, l_m_z', (
            [[0, 0], [0, 0]],
            [[], []],
            [[0], [0]],
            [[1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]]
    ))
    def test_move_zeros(self, list, l_m_z):
        assert move_zeros(list) == l_m_z
