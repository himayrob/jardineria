import os
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pe
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto

def menuProducto():
     while True:
          os.system("clear")
          print("""



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
                Repproducto.menu()
          if(opcion ==2):
               CRUDproducto.menu()
          elif(opcion ==0):
               break

     if(__name__== "__main__"):
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
        while True:
            os.system("clear")
            print("""
                             ___      _            _             _ 
  /\/\   ___ _ __  _   _    / _ \_ __(_)_ __   ___(_)_ __   __ _| |
 /    \ / _ \ '_ \| | | |  / /_)/ '__| | '_ \ / __| | '_ \ / _` | |
/ /\/\ \  __/ | | | |_| | / ___/| |  | | | | | (__| | |_) | (_| | |
\/    \/\___|_| |_|\__,_| \/    |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                    |_|            
                  1. Cliente
                  2. Oficina
                  3. Empleado
                  4. pedidos
                  5. productos
                  0. salir

                  
""")
            opcion = int(input("\nseleccione una de las opciones: "))
            if(opcion==1):
               cliente.menu()
            elif(opcion==2):
               oficina.menu()
            elif(opcion==3):
               empleado.menu()
            elif(opcion==4):
               pedidos.menu()
            elif(opcion==5):
               menuProducto()
            elif(opcion == 0):
                break

   
     