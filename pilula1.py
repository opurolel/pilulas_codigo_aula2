import math

assinantes = int(input('Digite a q. de assinantes atuais: '))
mensalidade = float(input('Digite o valor da mensalidade: '))
taxa = float(input('Digite a taxa de crescimento mensal %: '))/100
meses = int(input('Digite a q. de meses da projeção: '))

assinantes_finais = assinantes * math.pow((1+taxa), meses)
receita_final = assinantes_finais * mensalidade

print(f"Assinantes estimados: {assinantes_finais:.0f}")
print(f"Receita estimada: R${receita_final:.2f}")