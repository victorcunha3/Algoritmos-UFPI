def validar_dados_de_entrada(nome, idade):
  """Valida os dados de entrada do usuário."""
  if not all((nome, idade)):
    return False
  return True

# Solicita os dados do usuário
nome = input("Nome: ")
idade = int(input("Idade: "))

# Valida os dados do usuário
if validar_dados_de_entrada(nome, idade):
  # Os dados são válidos
  print("Os dados são válidos.")
else:
  # Os dados não são válidos
  print("Os dados não são válidos.")


# Conjunto
my_set = {1, 2, 3, 4, 5}
print(all(my_set))  # True

# Dicionário
my_dict = {1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco"}
print(all(my_dict))  # True

# String
my_string = "Olá, mundo!"