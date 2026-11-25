import pytest
import Conversion as con


def test_centimetros_a_pulgadas():
    assert con.centimetros_a_pulgadas(5.08) == pytest.approx(2.0)


def test_pulgadas_a_centimetros():
    assert con.pulgadas_a_centimetros(2.0) == pytest.approx(5.08)


def test_pies_a_metros():
    assert con.pies_a_metros(10.0) == pytest.approx(3.048)


def test_metros_a_pies():
    assert con.metros_a_pies(3.048) == pytest.approx(10.0)


def test_millas_a_km():
    assert con.millas_a_km(1.0) == pytest.approx(1.60934)


def test_km_a_millas():
    assert con.km_a_millas(1.60934) == pytest.approx(1.0)


def test_galones_a_litros():
    assert con.galones_a_litros(1.0) == pytest.approx(3.78541)


def test_litros_a_galones():
    assert con.litros_a_galones(3.78541) == pytest.approx(1.0)


def test_libras_a_kg():
    assert con.libras_a_kg(1.0) == pytest.approx(0.453592)


def test_kg_a_libras():
    assert con.kg_a_libras(0.453592) == pytest.approx(1.0)