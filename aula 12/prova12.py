class Material:
    def __init__(self,titulo, autor_ou_editora):
        self.titulo = titulo
        self.escritor = autor_ou_editora

    def exibir_informacoes(self):
        return f"Título: {self.titulo}, {self.escritor} "

class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    
    def exibir_informacoes(self):
        print ( super().exibir_informacoes())
        print (f"Gênero do livro: {self.genero}")
       
       
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    def exibir_informacoes(self):
        print( super().exibir_informacoes())
        print (f"Edição da revista: {self.edicao}")

livro1 = Livro("Comendo e testando","Carolina Leite", 'Comida')
revista1 = Revista("Veja",'Fernanda Rios','4° ed.')
print("\nInformações do Livro: ")
livro1.exibir_informacoes()
print("\nInformações da Revista: ")
revista1.exibir_informacoes()
        
