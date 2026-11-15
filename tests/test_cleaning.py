import pytest

from plantdoctor.cleaning import clean_label


def test_clean_label_trims_collapses_whitespace_and_casefolds():
    assert clean_label("  Tomato   Early Blight ") == "tomato early blight"


def test_clean_label_rejects_non_string():
    with pytest.raises(TypeError):
        clean_label(None)
