
from tabulate import tabulate 
import json
import request
import modules.postProducto as postproduct
def getAllData():
    peticion =request.get("")
    data = peticion.json()

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if (val,get("gama") == gama and val.get("cantidad_de_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price)
    for i, val in enumerate(condiciones):
        if(condiciones[i].get("descripcion")):
        condiciones[i] = {
                "codigo": val.get("codifo_producto"),
                "descripcion": f'{val["descripcion"][:5]}...',
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                
                
            }       
        if __name__ == "main":
    while True:
        print(f"""

                                                
   |  /  |_       |  _ _()   ()   | |
 
| |/| / -
| ' | || | |  | '| | ' / | | ' / ` | | - 
   ||  |__|||_,| || || ||||_|| .__,||
                                           |_|

                        
1. Cliente
2. Oficina
3. Empleado
4. Pedidos
5. Pagos
6. Salir
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            cli.menu()
        elif opcion == 2:
            of.menu()
        elif opcion == 3:
            em.menu()
        elif opcion == 4:
            pe.menu()
        elif opcion == 5:
            pag.menu()
        elif opcion == 6:
            break
            


 