from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "123456", "escola_romeu")

while True:
    print(f"{"-"* 15} Sistema de Gestão Escolar {"-"* 15}")
    print('''
    1. Ver Disciplinas.
    2. Ver Professores.
    0. Encerrar programa.
    ''')
    op = int(input("selecione a opção que deseja: "))
    if (op == 0):
        print("Programa Encerrado")
        break
    elif (op == 1):


        disciplinas = conexaoBD.consultar("SELECT * FROM disciplina")
        for disciplina in disciplinas:
            print("ID  | Nome da Disciplina ")
            print(f"{disciplina[0]}   | {disciplina[1]}")
        op_disc = int(input("Digite o ID da Disciplina que deseja para vê mais informações: "))
        escolha = conexaoBD.consultarComParametros("SELECT * FROM  turma where id_disciplina = %s", (op_disc,))
        print('''
        ID TURMA
''')


    elif (op == 2):
        try:
            professores = conexaoBD.consultar("SELECT * FROM professor")
            for professor in professores:
                print("ID  | Nome do Professor ")
                print(f"{professor[0]}   | {professor[1]}")

        except:
            print("Tente uma alternativa correta! ")



    input("Digite enter para continuar")