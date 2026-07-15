import pytest
from src.index_checker.validator import validate_index


def test_valid_index():
    assert validate_index("ATCG") == "ATCG"


def test_valid_index_lowercase():
    assert validate_index("atcg") == "ATCG"


def test_valid_index_with_spaces():
    assert validate_index(" ATCG ") == "ATCG"


def test_empty_index_raises_error():
    with pytest.raises(ValueError):
        validate_index("")


def test_invalid_character_raises_error():
    with pytest.raises(ValueError):
        validate_index("ATCN")


def test_wrong_length_raises_error():
    with pytest.raises(ValueError):
        validate_index("ATCG", expected_length=8)