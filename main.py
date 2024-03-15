import os
import re
import modules.getClients as cli
import modules.getOficina as of
import modules.getEmpleados as em
import modules.getPedido as pe
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto

# def menuProducto():
#      while True:
#           os.system("clear")
#           print("""
#                   1. Reportes de los productos
#                   2. Guardar, Actualizar y Eliminar productos
#                   0. Regresar al menu principal            

#             """)
#           opcion = int(input("\nseleccione una de las opciones:"))
#           if(opcion ==1):
#                 Repproducto.menu()
#           if(opcion ==2):
#                CRUDproducto.menu()
#           elif(opcion ==0):
#                break

     #if(__name__== "__main__"):
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    #    while True:
      #      os.system("clear")
def menu():
            print("""

                  1. Cliente
                  2. Oficina
                  3. Empleado
                  4. pedidos
                  5. productos
                  0. salir

                  
""")
      
            opcion = int(input("\nseleccione una de las opciones: "))        
            if(opcion==1):
               cli.menu()
            # elif(opcion==2):
            #    oficina.menu()
            # elif(opcion==3):
            #    empleado.menu()
            # elif(opcion==4):
            #       pedidos.menu()
            # elif(opcion==5):
            #     producto.menu()
            #elif(opcion == 0):
               #break
menu()
              
         #   except zeroDivision as error:
         #      print("error generado: ")   
         #   except ValueError as error:
         #      print("error generado: ")
              
              
              
              

           
           
           
           
           
           
           
      

   
     