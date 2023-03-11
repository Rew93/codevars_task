from func import orel_reshka
import pytest


@pytest.mark.parametrize('a, b', [('orel', 'reshka')])
def test_work(a, b):
    assert orel_reshka() == a or b


@pytest.mark.parametrize('a, b', [('s', 'sss')])
def test_error(a, b):
    assert orel_reshka() != (a or b)
