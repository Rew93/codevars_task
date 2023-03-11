import pytest
from code_vars_task.evaluate_mathematical_expression import calc


class TestCase:

    @pytest.mark.parametrize('str, result', (
            ["1 + 1", 2],
            ["8/16", 0.5],
            ["3 -(-1)", 4],
            ["2 + -2", 0],
            ["10- 2- -5", 13],
            ["(((10)))", 10],
            ["3 * 5", 15],
            ["-7 * -(6 / 3)", 14],
            ['69 / 38 - -40 / 53 - -55 - 10 * 82 / -14', 116.14193502624485],
            ['11 * 45 + -45 / -71 + 70 / 8 + 66 * 63', 4662.383802816901],
            ['6 + -(- 4)', 'Invalid'],
            ['-((-90))', 90],
    ))
    def test_calc(self, str, result):
        assert calc(str) == result

