import storage.cliente as cli

def getallClientesSpain(Spain):
    allClientesSpain = []
    for val in cli.clientes:
        if (val.get("pais") == "Spain" ):
            allClientesSpain.append(
                {
                    "nombre":val.get("nombre_cliente"),
                    "Spain": val.get("pais")

                }
            )
    return allClientesSpain
      