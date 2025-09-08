
dinheiro = float(input())
dinheiro_centavos = dinheiro * 100


notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]


print("NOTAS:")
for nota in notas:
    print(f"{(dinheiro_centavos // nota):.0f} nota(s) de R$ {(nota/100):.2f}")
    dinheiro_centavos = dinheiro_centavos % nota