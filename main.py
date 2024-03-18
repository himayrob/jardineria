import os
import re
import modules.getClients as cli
import modules.getOficina as of
import modules.getEmpleados as em
import modules.getPedido as pe
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto
import json
import requests

   #   while True:
   #        os.system("clear")
   #        print("""
   #                1. Reportes de los productos
   #                2. Guardar, Actualizar y Eliminar productos
   #                0. Regresar al menu principal            

   #          """)
   #        opcion = int(input("\nseleccione una de las opciones:"))
   #        if(opcion ==1):
   #              Repproducto.menu()
   #        if(opcion ==2):
   #             CRUDproducto.menu()
   #        elif(opcion ==0):
   #             break

   #   if(__name__== "__main__"):
       # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
# def menu():
#       while True:
#       # os.system("clear")
#             print("""

#                   1. Cliente
#                   2. Oficina
#                   3. Empleado
#                   4. pedidos
#                   5. productos
#                   0. salir

                  
# """)

      #   if(__name__== "__main__"):            
      #    while True:
      #      os.system("clear")  
      #       opcion = int(input("\nseleccione una de las opciones: "))        
      #       if(opcion==1):
      #          cli.menu()
      #       # elif(opcion==2):
            #    oficina.menu()
            # elif(opcion==3):
            #    empleado.menu()
            # elif(opcion==4):
            #       pedidos.menu()
            # elif(opcion==5):
            #     producto.menu()
            #elif(opcion == 0):
               # break
# menu()
              
         #   except zeroDivision as error:
         #      print("error generado: ")   
         #   except ValueError as error:
         #      print("error generado: ")
              
              
     
# if(__name__ == "__main__"):
#    with open("storage/producto.json". "r") as f:
#       fichero = f.read()
#       data =json.loads(f.read())
#       for i, val in enumerate(data):
#            val["id"] = (i+1)      
#            print(data)
#            whit open("storage/producto.json", "r") as f:
#            f1.write(data)
         #   f1.close()
