'''Insira os nomes até escrever parar'''

j=0
'''candidatos = {
    'Candidato 1': 'e5_t10_p8_s8',
    'Candiddato 2': 'e10_t7_p7_s8',
    'Candidato 3': 'e8_t5_p4_s9',
    'Candidato 4': 'e2_t2_p2_s1',
    'Candidato 5': 'e10_t10_p8_s9'
}'''

candidatos = [
    ['candidato 1', 'e5_t10_p8_s8' ],
    ['candidato 2', 'e10_t7_p7_s8'],
    ['candidato 3', 'e8_t5_p4_s9'],
    ['candidato 4', 'e2_t2_p2_s1'],
    ['candidato 5', 'e10_t10_p8_s9']
]

'''O código comentado abaixo insere os candidatos com as notas dinamicamente'''
while j==0:
    i=0
    lista_de_notas = []
    candidato_atual = input('Insira o nome do candidato: ')
    if(candidato_atual == 'parar'):
        break
    else:

        while i < 4:
            lista_de_notas.append(input('Insira a ' + str(i+1) + ' nota: '))
            i=i+1
        resultado = ('e' + str(lista_de_notas[0]) + '_' + 't' + str(lista_de_notas[1]) + '_' + 'p' + str(lista_de_notas[2]) + '_' + 's' + str(lista_de_notas[3]))
        candidatos.append([candidato_atual, resultado])
print(candidatos)
notas_minimas = []
i=0
while i < 4:
    if(i==0):
        notas_minimas.append(int(input('Insira a nota mínima da entrevista: ')))
    elif(i==1):
        notas_minimas.append(int(input('Insira a nota mínima do teste teórico: ')))
    elif(i==2):
        notas_minimas.append(int(input('Insira a nota mínima do teste prático: ')))
    elif(i==3):
        notas_minimas.append(int(input('Insira a nota mínima do teste de soft-skills: ')))
    i=i+1

lista_atual = []
caractere_proibido = ['e', 't', 'p', 's', '_']

lista_aprovados = []

for candidato in candidatos:
    '''print(candidatos[candidato])'''
    i=0
    lista_nota_candidato = []
    lista_atual = list(candidato[1])
    while i < len(lista_atual):
        nota_atualizada = ''
        if(i < len(lista_atual) - 1):
            if(lista_atual[i] in caractere_proibido):
                i = i+1
            elif(lista_atual[i+1] == '0'):
                nota_atualizada = nota_atualizada + lista_atual[i] + lista_atual[i+1]
                i=i+2
            else:
                nota_atualizada = nota_atualizada + lista_atual[i]
                i=i+1
            if(nota_atualizada != ''):
                lista_nota_candidato.append(int(nota_atualizada))
        else:
            nota_atualizada = nota_atualizada + lista_atual[i]
            lista_nota_candidato.append(int(nota_atualizada))
            i=i+1
    if(lista_nota_candidato[0]>=notas_minimas[0] and lista_nota_candidato[1]>=notas_minimas[1] and lista_nota_candidato[2]>=notas_minimas[2] and lista_nota_candidato[3]>=notas_minimas[3]):
        lista_aprovados.append(candidato[0])

'''print(lista_aprovados)'''

def aprovados(lista_dos_aprovados):
    i=0
    print('///////////////////////////APROVADOS/////////////////////////// ')
    while(i<len(lista_dos_aprovados)):
        print(lista_dos_aprovados[i])
        i=i+1
    print('//////////////////////////////////////////////////////////////')

aprovados(lista_aprovados)