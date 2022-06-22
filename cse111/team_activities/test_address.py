from address import extract_city,  extract_state, extract_zipcode
import pytest

# 10 Street, City, ST, 12345

def test_extract_city():
    assert extract_city("10 Street, City, ST 12345") == "City"

def test_extract_state():
    assert extract_state("10 Street, City, ST 12345") == "ST"

def test_extract_zipcode():
    assert extract_zipcode("10 Street, City, ST 12345") == "12345"

pytest.main(["-v", "--tb=line", "-rN", __file__])