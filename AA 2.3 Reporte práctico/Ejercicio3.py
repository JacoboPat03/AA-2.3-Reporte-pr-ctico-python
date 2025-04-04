''' crea una lista de nombre asignaturas_viii y almacena el nombre de una asignatura
crea otra lista que contiene la lista Asingnaturas_viii y una nueva asignatura
imprime y comprueba
crea una funcion agregar_asignatura que reciba dos parametros una lista y una asignatura
la funcion debe devolver lista mas la asignatura''
ejecuta la funcion agregar_asignatura, proporcionando la lista_asignatura '''

# Lista original
asignaturas_viii = ["PWeb backend", "redes", "inteligencia", "aplicaciones moviles"]

# Función para agregar asignatura
def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]
pregunta = input('INgresa nueva asignatura: ')

print(agregar_asignatura(asignaturas_viii,pregunta))