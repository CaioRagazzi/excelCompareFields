import pandas as pd
import sys

fileName = sys.argv

xl = pd.read_excel("./arquivo2.xlsx", sheet_name="Data")

values_a = xl["QuoteID"].values
values_e = xl["ApproverOrDenier"].values

tamanho = len(values_a)

lista_final = []
counter_um = 0
counter_dois = 0
for item_a in range(0, tamanho):
    comparador = [values_e[item_a], values_a[item_a]]
    lista = []
    for item_b in range(0, tamanho):
        if (
            comparador[0] == values_e[item_b]
            and comparador[1] == values_a[item_b]
            and counter_um != counter_dois
        ):
            lista.append([values_e[item_b], values_a[item_b], [(item_a + 2), (item_b + 2)]])
        counter_dois += 1
    if len(lista) >= 1:
        lista_final.append(lista)
    counter_dois = 0
    counter_um += 1

with open("listfile2.txt", "w") as filehandle:
    for item in lista_final:
        filehandle.write("%s\n" % item)
