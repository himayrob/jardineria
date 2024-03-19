from tabulate import tabulate
import json
import requests


def getDataDePagos():
    peticion = requests.get("http://172.16.103.27:5004")
    data = peticion.json()
    return data
# pida todos los pedido realizados en 2008 mediante paypal


def getAllPagosPayPal2008():
    pagos = getDataDePagos()
    pagosPayPal2008 = [pago for pago in pagos if "2008" in pago["Fecha"]]
    return pagosPayPal2008


def menu():
    while True:

        print("""
                     1.pagos hechos en 2008
                                                """)

        opcion = int(input("\nSelecione una de las opciones:"))
        if (opcion == 1):
            print(tabulate(getAllPagosPayPal2008(), headers="keys", tablefmt="github"))
        elif (opcion == 2):
            break
        else:
            print("opcion invalida. intente de nuevo")


menu()
