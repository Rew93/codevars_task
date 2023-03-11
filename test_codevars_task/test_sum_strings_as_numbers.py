import pytest
from code_vars_task.sum_strings_as_numbers import sum_strings

class TestCase:

    @pytest.mark.parametrize('string, result', (
        [],
    ))
    def test_sum_string(self, string, result):
        pass