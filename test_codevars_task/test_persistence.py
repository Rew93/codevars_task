import pytest
from code_vars_task.persistence import persistence


class TestCase:

    @pytest.mark.parametrize('n, count', (
            [39, 3],
            [4, 0],
            [25, 2],
            [999, 4],
    ))
    def test_persistence(self, n, count):
        assert persistence(n) == count
