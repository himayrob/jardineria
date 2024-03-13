import json
import requests
def postProducto(producto):
    peticion = requests.post("",data=json.dumps())
    res=peticion.json
    return res

