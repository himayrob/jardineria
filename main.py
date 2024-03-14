import os
import modules.getClients as cli
import modules.getOficina as of
import modules.getEmpleados as em
import modules.getPagos as pag
import modules.getPedido as pe

if __name__ == "main":
    while True:
        print(f"""

   _     _                           _     _               _                              
  | |   (_)                         (_)   | |             | |                             
  | |__  _  ___ _ ____   _____ _ __  _  __| | ___     __ _| |                             
  | '_ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | |                             
  | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | |                             
  |_.__/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|   _            _            
                                  | |                          | |          | |           
  _ __ ___   ___ _ __  _   _    __| | ___   _ __  _ __ ___   __| |_   _  ___| |_ ___  ___ 
 | '_ ` _ \ / _ \ '_ \| | | |  / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
 | | | | | |  __/ | | | |_| | | (_| |  __/ | |_) | | | (_) | (_| | |_| | (__| || (_) \__ \
 |_| |_| |_|\___|_| |_|\__,_|  \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/|___/
                                           | |                                            
                                           |_|                                            

            
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal            

            """)
        opcion = int(input("\nseleccione una de las opciones:"))
        if(opcion ==1):
            repproducto.menu()
        if(opcion ==2):
            CRUDproducto.menu()
        elif(opcion ==0):
            break

if(__name__== "__main__"):
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
        while True:
            os.system("clear")
            print("""
                                                            _            _             _ 
                                         (_)          (_)           | |
  _ __ ___   ___ _ __  _   _   _ __  _ __ _ _ __   ___ _ _ __   __ _| |
 | '_ ` _ \ / _ \ '_ \| | | | | '_ \| '__| | '_ \ / __| | '_ \ / _` | |
 | | | | | |  __/ | | | |_| | | |_) | |  | | | | | (__| | |_) | (_| | |
 |_| |_| |_|\___|_| |_|\__,_| | .__/|_|  |_|_| |_|\___|_| .__/ \__,_|_|
                              | |                       | |            
                              |_|                       |_|       
                  1. Cliente
                  2. Oficina
                  3. Empleado
                  4. pedidos
                  5. productos
                  0. salir

                  
""")
            opcion = int(input("\nseleccione una de las opciones: "))



   
     