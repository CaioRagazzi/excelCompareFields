import pandas as pd
import sys

fileName = sys.argv

xl = pd.read_excel("./arquivo2.xlsx", sheet_name="Data")

values_a = xl["QuoteID"].values
values_e = xl["ApproverOrDenier"].values

tamanho = len(values_a)

lista_final = []

for item_a in range(0, tamanho):
    comparador = [values_e[item_a], values_a[item_a]]
    lista = []
    for item_b in range(0, tamanho):
        if comparador[0] == values_e[item_b] and comparador[1] == values_a[item_b]:
            lista.append([values_e[item_b], values_a[item_b], (item_b + 2)])
    if len(lista) > 1:
        lista_final.append(lista)

with open("listfile2.txt", "w") as filehandle:
    for item in lista_final:
        filehandle.write("%s\n" % item)
