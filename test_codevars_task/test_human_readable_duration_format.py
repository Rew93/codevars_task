import pytest
from code_vars_task.human_readable_duration_format import format_duration

class TestCase:

    @pytest.mark.parametrize('seconds, r_string',(
        [1, "1 second"],
        [62, "1 minute and 2 seconds"],
        [120, "2 minutes"],
        [3600, "1 hour"],
        [3662, "1 hour, 1 minute and 2 seconds"],
        [1113600, '12 days, 21 hours and 20 minutes']
    ))
    def test_format_duration(self, seconds, r_string):
        assert format_duration(seconds) == r_string