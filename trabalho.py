def exibir_menu():
    menu = """
╔═════════════════════════════════════╗
║           MENU DE OPÇÕES            ║
╠═════════════════════════════════════╣
║ 1. Buscar candidatos por critérios  ║
║═════════════════════════════════════╣
║ 2. Adicionar ou excluir funcionários║
║═════════════════════════════════════╣
║              3. Sair                ║
╚═════════════════════════════════════╝
"""
    print(menu)

def buscar_candidato_por_critérios(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_encontrados = []
    for candidato in candidatos:
        resultado = candidato["resultado"]
        e, t, p, s = resultado.split("_")
        if int(e[1:]) >= nota_e and int(t[1:]) >= nota_t and int(p[1:]) >= nota_p and int(s[1:]) >= nota_s:
            candidato_com_pontuacao = candidato["nome"] + " " + resultado
            candidatos_encontrados.append(candidato_com_pontuacao)
    return candidatos_encontrados

candidatos = [
    {"nome": "João", "resultado": "e5_t10_p8_s8"},
    {"nome": "Maria", "resultado": "e10_t7_p7_s8"},
    {"nome": "Pedro", "resultado": "e8_t5_p4_s9"},
    {"nome": "Ana", "resultado": "e2_t2_p2_s1"},
    {"nome": "Carlos", "resultado": "e10_t10_p8_s9"}
]

def adicionar_funcionario():
    nome = input("Digite o nome do novo funcionário: ")
    resultado = input("Digite o resultado do novo funcionário no formato 'ex_tx_px_sx': ")
    candidatos.append({"nome": nome, "resultado": resultado})
    print(f"Funcionário {nome} adicionado com sucesso!")