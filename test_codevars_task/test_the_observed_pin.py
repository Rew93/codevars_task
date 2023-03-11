import pytest
from code_vars_task.the_observed_pin import get_pins


class TestCase:

    @pytest.mark.parametrize('observed, result', (
        []
    ))
    def test_get_pins(self, observed, result):
        assert get_pins(observed) == result
