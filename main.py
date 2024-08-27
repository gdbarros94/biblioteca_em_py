class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponivel = disponivel

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def isbn(self):
        return self.__isbn

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self.__disponivel = valor

    def adicionar(self, biblioteca):
        biblioteca.livros.append(self)

    @staticmethod
    def buscar(biblioteca, titulo=None, autor=None):
        resultados = []
        for livro in biblioteca.livros:
            if (titulo and titulo.lower() in livro.titulo.lower()) or \
               (autor and autor.lower() in livro.autor.lower()):
                resultados.append(livro)
        return resultados

    def emprestar(self, usuario):
        if self.disponivel:
            self.disponivel = False
            usuario.livros_emprestados.append(self)
            print(f'O livro "{self.titulo}" foi emprestado para {usuario.nome}.')
        else:
            print(f'O livro "{self.titulo}" não está disponível.')

    def devolver(self, usuario):
        if self in usuario.livros_emprestados:
            self.disponivel = True
            usuario.livros_emprestados.remove(self)
            print(f'O livro "{self.titulo}" foi devolvido por {usuario.nome}.')
        else:
            print(f'O livro "{self.titulo}" não foi emprestado para {usuario.nome}.')


class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade


class Usuario:
    def __init__(self, nome, usuario_id):
        self.__nome = nome
        self.__usuario_id = usuario_id
        self.__livros_emprestados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def livros_emprestados(self):
        return self.__livros_emprestados


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu de Gerenciamento da Biblioteca")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Adicionar Usuário")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o ISBN do livro: ")
            novo_livro = Livro(titulo, autor, isbn)
            novo_livro.adicionar(biblioteca)
            print(f'Livro "{titulo}" adicionado à biblioteca.')

        elif escolha == "2":
            criterio = input("Buscar por título (t) ou autor (a)? ").lower()
            if criterio == "t":
                titulo = input("Digite o título do livro: ")
                resultados = Livro.buscar(biblioteca, titulo=titulo)
            elif criterio == "a":
                autor = input("Digite o nome do autor: ")
                resultados = Livro.buscar(biblioteca, autor=autor)
            else:
                print("Opção inválida.")
                continue

            if resultados:
                print("Livros encontrados:")
                for livro in resultados:
                    status = "Disponível" if livro.disponivel else "Indisponível"
                    print(f'Título: {livro.titulo}, Autor: {livro.autor}, ISBN: {livro.isbn}, Status: {status}')
            else:
                print("Nenhum livro encontrado.")

        elif escolha == "3":
            usuario_id = input("Digite o ID do usuário: ")
            usuario = next((u for u in biblioteca.usuarios if u.usuario_id == usuario_id), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro a ser emprestado: ")
            resultados = Livro.buscar(biblioteca, titulo=titulo)
            if resultados:
                livro = resultados[0]
                livro.emprestar(usuario)
            else:
                print("Livro não encontrado.")

        elif escolha == "4":
            usuario_id = input("Digite o ID do usuário: ")
            usuario = next((u for u in biblioteca.usuarios if u.usuario_id == usuario_id), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro a ser devolvido: ")
            livro = next((l for l in usuario.livros_emprestados if l.titulo == titulo), None)
            if livro:
                livro.devolver(usuario)
            else:
                print("O usuário não possui esse livro.")

        elif escolha == "5":
            nome = input("Digite o nome do usuário: ")
            usuario_id = input("Digite o ID do usuário: ")
            novo_usuario = Usuario(nome, usuario_id)
            biblioteca.adicionar_usuario(novo_usuario)
            print(f'Usuário "{nome}" adicionado ao sistema.')

        elif escolha == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()


# mano que codigo bom :O
