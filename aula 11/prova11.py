class Elevador:
    def __init__ (self,totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self):
        if self.totalAndar > self.atualAndar :
            self.atualAndar +=1
            print("Subindo...")
            print ("Andar: ", self.atualAndar)
        else:
            self.totalAndar = self.atualAndar
            print( "VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
   
    def Descer(self):
        if 0 < self.atualAndar <= self.totalAndar :
            self.atualAndar -= 1 
            print("Descendo...")
            print("Andar: ",self.atualAndar)
        else:
            self.atualAndar = 0
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.totalCapacidade > self.atualCapacidade:
            self.atualCapacidade += 1
            print( "Entrando uma pessoa")
            print("Capacidade atual: ", self.atualCapacidade)
            
        else:
            self.totalCapacidade = self.atualCapacidade
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if 0 < self.atualCapacidade <= self.totalCapacidade:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa")
            print("Capacidade atual: ",self.atualCapacidade)
         
        else:
            self.atualCapacidade = 0 
            print("NÃO TEM NINGUÉM")

#Exemplo:
elevador1 = Elevador(25,12)
for andar in range(12):
 elevador1.Subir()
elevador1.Subir()
elevador1.Entrar()