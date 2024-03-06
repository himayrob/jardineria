import storage.cliente as cli

def getallClientesSpain(all):
    allClientesSpain = []
    for val in cli.clientes:
        if (val.get("puesto") == "spain" ):
            allClientesSpain.append(
                {
                    "spain": val.get("spain")

                }
            )
    return allClientesSpain
      