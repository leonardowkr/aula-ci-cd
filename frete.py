def calcular_frete(valor_compra):
  #Não aceita valor negativo
  if valor_compra < 0:
    raise ValueError("O valor da compra não pode ser negativo")
  #Acima de 200 frete grátis
  if valor_compra >= 200:
    return 0.0
  #Abaixo de 200, 20 reais
  return 20.0
