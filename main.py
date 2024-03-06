from tabulate import tabulate

import modules.getClients as cli
import modules.getOficina as oficina
import modules.getEmpleados as em


print(tabulate(cli.getallClientesSpain("Spain"), tablefmt ='grid'))

