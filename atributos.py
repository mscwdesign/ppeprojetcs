"""
Atributos representam as caracteristicas do objetos, ou seja pelos atributos nos conseguimos
representar computacionalmente os estados dos objetos

Em python dividimos os atributos em 3 grupos:
    atributos de instancias
    atributos de classe
    atributo dinamicos


Atributo de instancia:
São declarados dentro do metodo construtor

Metodo construtor é um metodo especial utilizado para a construção do objeto.

Em java ficaria + - assim

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}



print(user.email)

print(user.__senha)

print(user._Acesso__senha)

# Atributo de instancia

# Significa que ao criar instancias de uma classe, todas as instancias de uma classe
# terão estes atributos.

user = Acesso('user@gmail.com', '123456')



user1 = Acesso('user@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '98765')

user.mostra_email()


p1 = Produto('PS4', 'Video Game', 2300)
p2 = Produto('XBOX S', 'Video Game', 4600)

print(p1.valor)
print(p2.valor)

# Atributo de classe, são atributos declarados fora do construtor, Geralmente já inicializamos um
# Valor, este valor é compartilhado entre todas as instancias ou seja ao inves de cada instancia
# de classe ter seus proprios valores como é o caso dos atributos de instancia com os atributos
# de classe todas as instancias terão o mesmo valor para este atributo.

"""

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Modo atributo privado

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)



# Refatorando produto

class Produto:

    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributo dinamico

p1 = Produto('PS4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# Deletando atributos



