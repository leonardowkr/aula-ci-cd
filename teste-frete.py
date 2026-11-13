import pytest 
from frete import calcular_frete

def test_compra_abaixo_limite_paga_frete():
  resultado = calcular_frete(199.99)
  assert resultado == 20.0
def test_test_compra_no_limite_tem_frete_gratis():
  resultado = calcular_frete(200)
  assert resultado == 0
def test_compra_acima_limite_frete_gratis():
  resultado = calcular_frete(201)
  assert resultado == 0
def test_compra_de_valor_zero():
  resultado = calcular_frete(0.00)
  assert resultado == 20
def test_valor_negativo_deve_ser_rejeitado():
  with pytest.raises(ValueError):
    clcular_frete(-1)
