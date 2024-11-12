from .models import Tarea, SubTarea


# Dentro del archivo services.py crear 6 funciones:
# a. recupera_tareas_y_sub_tareas
def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    return [
        {"tarea": tarea, "subtareas": list(tarea.subtareas.all())} for tarea in tareas
    ]


# b. crear_nueva_tarea
def crear_nueva_tarea(descripcion, estado):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()


# c. crear_sub_tarea
def crear_sub_tarea(tarea_id, descripcion, estado):
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea.objects.create(
        descripcion=descripcion, estado=estado, tarea=tarea
    )
    return recupera_tareas_y_sub_tareas()


# d. elimina_tarea
def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()


# e. elimina_sub_tarea
def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()


# f. imprimir_en_pantalla
def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea in tareas_y_subtareas:
        print(tarea["tarea"])
        for subtarea in tarea["subtareas"]:
            print(subtarea)
