# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# Primeiro nao faco ideia de onde esteja o arquivo json ou xml

maior_faturamento = 0
dias_acima_media = 0
faturamento_do_mes = 0

faturamento_diario = [] # Aqui ficaria os valores que foram faturados no mes, dia apos dia

for i in range(30):
    if faturamento_diario[i] > maior_faturamento:
        maior_faturamento = faturamento_diario[i]
    
    faturamento_do_mes += faturamento_diario[i]

media_faturamento_mensal = faturamento_do_mes / 30

menor_faturamento = media_faturamento_mensal

for i in range(30):
    if faturamento_diario[i] < menor_faturamento:
        menor_faturamento = faturamento_diario[i]
    
    if faturamento_diario[i] > media_faturamento_mensal:
        dias_acima_media += 1
    