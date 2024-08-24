import pytest


def test_lawn_grass_init(grass1):
    assert grass1.color == "Зеленый"


def test_lawn_grass_add(grass1, grass2):
    assert grass1 + grass2 == 16750


def test_lawn_grass_add_error(grass1, product2):
    with pytest.raises(TypeError):
        assert grass1 + product2
