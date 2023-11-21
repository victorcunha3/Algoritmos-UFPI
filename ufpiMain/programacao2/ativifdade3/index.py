class Funcionario:

    def __init__(self, matricula, nome, setor, salario):
        self.matricula = matricula
        self.nome = nome
        self.setor = setor
        self.salario = salario

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_setor(self):
        return self.setor

    def set_setor(self, setor):
        self.setor = setor

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

class Gerente(Funcionario):

    def __init__(self, matricula, nome, setor, salario, senha):
        super().__init__(matricula, nome, setor, salario)
        self.validar_senha(senha)
        self.senha = senha

    def autenticar(self, senha):
        if self.senha == senha:
            return True
        else:
            print("senhas incorretas")

    def validar_senha(self, senha):
        if not isinstance(senha, str):
             raise ValueError("A senha deve ser uma string.")
        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 dígitos.")
        
        e_maiusculo = False
        e_minusculo = False
        e_numero = False

        for caractere_atual in senha:
            if caractere_atual.isupper():
                e_maiusculo = True
            if caractere_atual.islower():
                e_minusculo = True
            if caractere_atual.isdigit():
                e_numero = True

        if not (e_maiusculo and e_minusculo and e_numero):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número.")

x = Gerente("gssgg", "shghs", "js", "sanubdoad", "senhaaaAada")
resultado = x.autenticar("senalida")
