from tabulate import tabulate
import modules.getClients as clientes

import modules.getOficina as oficina
import modules.getEmpleados as em


print(tabulate(em.getnombreApellidosEmailDirectorGeneral(1), tablefmt ='grid'))

