from tabulate import tabulate

import module.getClients as clientes

import module.getOficina as oficina

import modules.getEmpleados as empleado

print(tabulate(empleado.getAllNombreApellidosEmailJefe(7), tablefmt ='grid'))

#print(tabulate(cliente.getClientPaisCiudadRegion('spain,fuenlabrada')))