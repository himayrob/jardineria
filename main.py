from tabulate import tabulate

import modules.getClients as clientes

import modules.getOficina as oficina

import modules.getEmpleados as empleado

print(tabulate(empleado.getAllNombreApellidoEmailJefe(7), tablefmt ='grid'))

#print(tabulate(cliente.getClientPaisCiudadRegion('spain,fuenlabrada')))getAllNombreApellidoEmailJefe