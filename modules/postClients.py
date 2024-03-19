import json
import requests
from tabulate import tabulate
import re

import modules.getClients as getcli


def FuncionDeConeccionClienteJson():
    peticion = requests.get("http://10.0.2.15:5001/clientes") 
    Informacion = peticion.json()
    return Informacion


def deletProduct(id)
    
    data = get