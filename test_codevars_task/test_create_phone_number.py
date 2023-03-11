import pytest
from code_vars_task.create_phone_number import create_phone_number


class TestCase:

    @pytest.mark.parametrize('n, number', (
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111"],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"],
        [[0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "(000) 000-0000"],
    ))
    def test_func(self, n, number):
        assert create_phone_number(n) == number