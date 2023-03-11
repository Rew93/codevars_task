import pytest
from code_vars_task.so_many_permutations import permutations

class TestCase:

    @pytest.mark.parametrize('s, lst', (
        ['a', ['a']],
        ['ab', ['ab', 'ba']],
        ['aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']],
    ))
    def test_permutation(self, s, lst):
        assert permutations(s) == lst