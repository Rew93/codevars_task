import pytest
from code_vars_task.duplicate_count import duplicate_count


class TestCase:

    @pytest.mark.parametrize('text, count_dublicate', (
            ['', 0],
            ["abcde", 0],
            ["abcdeaa", 1],
            ["abcdeaB", 2],
            ["Indivisibilities", 2],
    ))
    def test_dublicate_count(self, text, count_dublicate):
        assert duplicate_count(text) == count_dublicate
