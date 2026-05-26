codigo_cidade = []
nome_cidade = []
nome_estado = []
num_veiculos_passeio = []
num_acidentes_com_vitimas = []
num_acidentes_sem_vitimas = []
condutor_embriagado = []
indice_menor = 0
indice_maior = 0
menor_num_acidente = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000
maior_num_acidentes = -1

quantidade_cidades = int (input("\nDigite a quantidade de cidades para realizar a estatística: "))

for i in range (quantidade_cidades):
    total_acidentes = 0

    dig_codigo_cidade = int (input("\nDigite o código da cidade: "))
    codigo_cidade.append (nome_cidade)

    dig_nome_cidade = str (input("\nDigite o nome da cidade: "))
    nome_cidade.append (dig_nome_cidade)

    dig_nome_estado = str (input("\nDigite o nome do estado: "))
    nome_estado.append (dig_nome_estado)

    dig_num_veiculos_passeio = int (input("\nDigite o número de veículos de passeio: "))
    num_veiculos_passeio.append (dig_num_veiculos_passeio)

    dig_num_acidentes_com_vitimas = int (input("\nDigite o número de acidentes com vitimas: "))
    num_acidentes_com_vitimas.append (dig_num_acidentes_com_vitimas)
    total_acidentes += dig_num_acidentes_com_vitimas

    dig_num_acidentes_sem_vitimas = int (input("\nDigite o número de acidentes sem vitimas: "))
    num_acidentes_sem_vitimas.append (dig_num_acidentes_sem_vitimas)
    total_acidentes += dig_num_acidentes_sem_vitimas
    if total_acidentes < menor_num_acidente:
        indice_menor = i
        menor_num_acidente = total_acidentes

    dig_condutor_embriagado = int (input("\nDigite o número de acidentes com condutor embriagado: "))
    condutor_embriagado.append (dig_condutor_embriagado)

    if total_acidentes > maior_num_acidentes:
        indice_maior = i
        maior_num_acidentes = total_acidentes

print (f"\nO menor índice de acidentes de transito é: {num_acidentes_com_vitimas[indice_menor] + num_acidentes_sem_vitimas [indice_menor]}")
print (f"E essa cidade é: {nome_cidade[indice_menor]}")

print (f"\nO maior índice de acidentes de transito é: {num_acidentes_com_vitimas[indice_maior] + num_acidentes_sem_vitimas [indice_maior]}")
print (f"E essa cidade é: {nome_cidade[indice_maior]}")

print (f"\nA média de veículos de todas as cidades é: {sum(num_veiculos_passeio)/quantidade_cidades}")

