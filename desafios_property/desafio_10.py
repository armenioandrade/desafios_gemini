# Crie uma classe chamada Perfil.

# 1. Construtor (__init__)
# Deve receber username e email.

# Regra: Você deve usar os setters das propriedades correspondentes para inicializar ambos os atributos.

# 2. Propriedade: username (@property e @setter)
# Getter: Retorna self._username em letras minúsculas.

# Setter:

# Validação de Comprimento: Deve ter entre 3 e 15 caracteres (incluídos).

# Se o comprimento for inválido, lance um ValueError.

# Se for válido, atribua a self._username.

# 3. Propriedade: email (@property e @setter)
# Getter: Retorna self._email sem nenhuma modificação.

# Setter:

# Validação de Formato: Deve conter o caractere '@'.

# Se o formato for inválido, lance um ValueError.

# Se for válido, atribua a self._email.

class Perfil():

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def username(self):
        return self._username.lower()
    
    @username.setter
    def username(self, new_username):
        if len(new_username) > 3 and len(new_username) <= 15:
            self._username = new_username
        else:
            raise ValueError('Comprimento inválido')
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if new_email.__contains__('@'):
            self._email = new_email
        else:
            raise ValueError('e-mail inválido')
