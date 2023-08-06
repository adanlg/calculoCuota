def calcular_odds_sum(cuota1, cuota2, cuota3):
    odds_sum = 1 / cuota1 + 1 / cuota2 + 1 / cuota3
    return odds_sum

def verificar_valor_mayor_que_uno(cuota_sum):
    return cuota_sum >= 1

# Ejemplo de uso
cuota1 = 9.6
cuota2 = 5.7
cuota3 = 1.3

odds_sum_resultado = calcular_odds_sum(cuota1, cuota2, cuota3)
es_mayor_que_uno = verificar_valor_mayor_que_uno(odds_sum_resultado)

print(f"La suma de las odds es: {odds_sum_resultado:.2f}")
if es_mayor_que_uno:
    print("El valor es mayor o igual que 1. Mal.")
else:
    print("El valor es menor que 1. Bien.")
