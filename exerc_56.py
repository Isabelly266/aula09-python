despesas = [45.0, 120.0, 35.5, 80.0]
total = 0
for despesa in despesas:
    total += despesa
media = total / len(despesas)
maior_despesa = max(despesas)
menor_despesa = min(despesas)       
print("Total de despesas: R$", total)
print("Média de despesas: R$", media)
print("Maior despesa: R$", maior_despesa)
print("Menor despesa: R$", menor_despesa)
