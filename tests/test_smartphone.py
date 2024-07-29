import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone2, smartphone3):
    assert smartphone2 + smartphone3 == 2114000


def test_smartphone_add_error(smartphone1, product2):
    with pytest.raises(TypeError):
        assert smartphone1 + product2
