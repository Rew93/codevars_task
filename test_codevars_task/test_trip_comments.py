import pytest
from code_vars_task.strip_сomments import strip_comments


class TestCase:

    @pytest.mark.parametrize('str, markers, answer', (
            ['apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'], 'apples, pears\ngrapes\nbananas'],
            ['a #b\nc\nd $e f g', ['#', '$'], 'a\nc\nd'],
            [' a #b\nc\nd $e f g', ['#', '$'], ' a\nc\nd'],
    ))
    def test_strip_comments(self, str, markers, answer):
        assert strip_comments(str, markers) == answer
