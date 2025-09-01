alunos = []

class Aluno:
    def __init__(self, nome, email, curso, matricula):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.matricula = matricula

def terminalAlunos(alunos):
    while True:
        print("\nMenu:")
        print("1. Adicionar Aluno")
        print("2. Atualizar info de Aluno")
        print("3. Listar Alunos")
        print("4. Remover Aluno")
        print("5. Sair \n")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicinarAluno(alunos)

        elif escolha == '2':
            atualizarAluno(alunos)

        elif escolha == '3':
            listarAlunos(alunos)
        elif escolha == '4':
            removerAluno(alunos)
        elif escolha == '5':
            print("Saindo do terminal de alunos.")
            break
        else:
            print("\033[91mOpção inválida. Tente novamente.\033[0m")

def adicinarAluno(alunos):
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno (Favor utilizar apenas a sigla do curso, ex: GEC, GES, etc): ")
    matriculas_curso = [aluno.matricula for aluno in alunos if aluno.curso == curso and aluno.matricula is not None]
    nova_matricula = max(matriculas_curso, default=0) + 1
    aluno = Aluno(nome, email, curso, matricula=nova_matricula)
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso! Matrícula: {nova_matricula}")

def atualizarAluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno.nome == nome:
            novo_email = input("Digite o novo email: ")
            novo_curso = input("Digite o novo curso: ")
            if aluno.curso != novo_curso:
                matriculas_curso = [aluno.matricula for aluno in alunos if aluno.curso == novo_curso and aluno.matricula is not None]
                aluno.matricula = max(matriculas_curso, default=0) + 1
            aluno.email = novo_email
            aluno.curso = novo_curso
            print(f"Aluno {nome} atualizado com sucesso! Matrícula: {aluno.matricula}")
            return
    print(f"Aluno {nome} não encontrado.")

def listarAlunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\nLista de Alunos:")
    for aluno in alunos:
        print(f"Nome: {aluno.nome}, Email: {aluno.email}, Curso: {aluno.curso}, Matrícula: {aluno.matricula}")

def removerAluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    nome = input("Digite o nome do aluno a ser removido: ")
    for i, aluno in enumerate(alunos):
        if aluno.nome == nome:
            del alunos[i]
            print(f"Aluno {nome} removido com sucesso!")
            return
    print(f"Aluno {nome} não encontrado.")

if __name__ == "__main__":
    print("Terminal de Alunos")
    terminalAlunos(alunos)