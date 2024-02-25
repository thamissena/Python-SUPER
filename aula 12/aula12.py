class Animal:
    def fazerSom (self):
        pass

class Cachorro(Animal):
    def fazerSom(self):
        return "Woof!"
    
class Gato(Animal):
    def fazerSom(self):
        return "Meow!"
    
class Pato(Animal):
    def fazerSom(self):
        return "Quack!"

#Função que usa polimorfismo
def fazerAnimalFalar (animal):
    return animal.fazerSom()
#Criando os objetos
Rex = Cachorro()
Whiskers = Gato()
Donald = Pato()

#Chamando a função usando polimorfismo 
animais = [Rex, Whiskers, Donald]
for animal in animais:
    print(animal.__class__.__name__, "faz", fazerAnimalFalar(animal))
    
exit()


#Polimorfismo:
class ContasCorrentes:
    def __init__(self, numero, correntista):
        self.numero = numero
        self.correntista = correntista
        self.__saldo = 0 
        
    #Decorator (Disfarce)
    @property
    def movimentar(self):   #Getter
        return f"R$ {self.__saldo}"

    @movimentar.setter    #Setter
    def movimentar(self,valor):
        if(self.__saldo + valor) >= 0:
            self.__saldo += valor
        else:
          print ("Saldo depositado negativo.")
# Para ter um Setter precisa de um Getter, mas podemos fazer um Getter sem o Setter.   

#--------------

minhaConta = ContasCorrentes("12345-0","Vinicius Costas")
print(f"Número da conta: {minhaConta.numero}") 
print(minhaConta.movimentar)  #Getter -> 0 

minhaConta.movimentar = -100  #Setter

print (minhaConta.movimentar)  #Getter - > - 100 (não pode)

minhaConta.movimentar = 100  #Setter

print (minhaConta.movimentar)  #Getter - > 100 



exit() #Desativa o programa abaixo 

class Motores:
    def funcionar(self):
        return f"Motor ligado!!"

objMotor1 = Motores()

class Carros:
    #Método construtor:
    def __init__(self, maxima,objMotor1, cor = "Branca"):
        #Atributos:
        self.cor = cor
        self.veloMax = maxima
        self.motor = objMotor1
        self.__renavam = 123456 #o atributo está na class, mas não é possível sua visualização por causa dos "__", protegido. 
        self.veloAtual = 0

    def frear(self):
        return f"Freando..."
   
class Caminhoes(Carros):
    pass

#Estanciando objeto:
objCaminhao = Caminhoes(cor="Vermelha", maxima=190, objMotor1= objMotor1)
objCarro = Carros(maxima=200,objMotor1=objMotor1)

print (objCaminhao.frear())
print(objCarro.motor.funcionar())
print (objCaminhao.motor.funcionar()) 