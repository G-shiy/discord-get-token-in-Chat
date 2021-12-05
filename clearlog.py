import os, os.path
#utilizar para limpar o arquivo trashlog (Não recomendado!!)

with open("trashlog/trashlog.txt", "a") as file:
    file.truncate(0)