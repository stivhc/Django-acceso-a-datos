from django.db import models


# CREACIÓN DE MODELOS
# Modelo Tarea
class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.id}] {self.descripcion}"


# Modelo SubTarea
class SubTarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    tarea = models.ForeignKey(
        Tarea, related_name="subtareas", on_delete=models.CASCADE
    )  # La clave foránea nos permite conectar Subtarea con Tarea.
    # Cada SubTarea está asociada con una Tarea específica.
    # on_delete=models.CASCADE: indica que, si se elimina una Tarea, también se eliminarán todas las SubTarea asociadas.

    def __str__(self):
        return f".... [{self.id}] {self.descripcion}"
