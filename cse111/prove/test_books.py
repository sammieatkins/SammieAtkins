import pytest
from books import find_author

def test_find_author():
    find_author()
    pass

pytest.main(["-v", "--tb=line", "-rN", __file__])