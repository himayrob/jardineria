import storage.empleado as em


def getnombreApellidosEmailDirectorGeneral(codigo):
    nombreApellidosEmailDirectorGeneral =[]
    for val in em.empleados:
        if (val.get("codigo_jefe") == codigo):
            nombreApellidosEmailDirectorGeneral.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": F'{val.get("apellido1")}{val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidosEmailDirectorGeneral
