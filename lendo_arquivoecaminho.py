import os

# Arquivo atual:
print("Arquivo atual:",__file__)

# Nome do arquivo:
print("Nome do arquivo atual:", os.path.basename(__file__))

# Pasta do arquivo:
print("Pasta do arquivo:",os.path.dirname(__file__))

# Pasta abslouta:
print("Caminho absoluto do arquivo:", os.path.abspath(__file__))
