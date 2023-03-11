import pytest
from code_vars_task.string_mix import mix


class TestCase:

    @pytest.mark.parametrize('s1, s2, result', (
            []
    ))
    def test_string_mix(self, s1, s2, result):
        assert mix(s1, s2) == result
