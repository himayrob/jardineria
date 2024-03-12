from tabulate import tabulate
import modules.getClients as cli
import modules.getOficina as of
import modules.getEmpleados as em
import modules.getPagos as pag
import modules.getPedido as pe

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



