import pytest
from code_vars_task.who_likes_it import likes


class TestCase:

    @pytest.mark.parametrize('names, like', ([[], 'no one likes this'],
                                             [['Peter'], 'Peter likes this'],
                                             [['Jacob', 'Alex'], 'Jacob and Alex like this'],
                                             [['Max', 'John', 'Mark'], 'Max, John and Mark like this'],
                                             [['Leon McNichol', 'Nene Romanova', 'Brian J. Mason', 'Quincy Rosenkreutz',
                                               'Macky Stingray'], 'Leon McNichol, Nene Romanova and 3 others like this']))
    def test_func(self, names, like):
        assert likes(names) == like
