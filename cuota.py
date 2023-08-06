def calcular_odds_sum(cuota1, cuota2, cuota3):
    odds_sum = 1 / cuota1 + 1 / cuota2 + 1 / cuota3
    return odds_sum

def verificar_valor_mayor_que_uno(cuota_sum):
    return cuota_sum >= 1

# Ejemplo de uso
cuota1 = 1.27
cuota2 = 5.70
cuota3 = 9.21

odds_sum_resultado = calcular_odds_sum(cuota1, cuota2, cuota3)
es_mayor_que_uno = verificar_valor_mayor_que_uno(odds_sum_resultado)

print(f"La suma de las odds es: {odds_sum_resultado:.2f}")
if es_mayor_que_uno:
    print("El valor es mayor o igual que 1. Mal.")
else:
    print("El valor es menor que 1. Bien.")
    
odd1 = 1 / cuota1
odd2 = 1 / cuota2
odd3 = 1 / cuota3
print(odds_sum_resultado)
print(odd1)
porcentaje1 = odd1 / odds_sum_resultado
porcentaje2 = odd2 / odds_sum_resultado
porcentaje3 = odd3 / odds_sum_resultado

cuotaJusta1 = 1 / porcentaje1
cuotaJusta2 = 1 / porcentaje2
cuotaJusta3 = 1 / porcentaje3

comprobacion = porcentaje1 + porcentaje2 + porcentaje3

print(comprobacion)
print(porcentaje1)
print(cuotaJusta1)
print(cuotaJusta2)
print(cuotaJusta3)
