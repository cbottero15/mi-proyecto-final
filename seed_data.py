from ejemplo.models import Familiar

Familiar(nombre="Diego Vaira", direccion="Pellegrini 433", numero_pasaporte=21625533).save()
Familiar(nombre="Camila Vaira", direccion="Bv. Pueyrredon 892 3A", numero_pasaporte=39176724).save()
Familiar(nombre="Micaela Vaira", direccion="Irigoyen esq. Serafin Resta", numero_pasaporte=43345345).save()
Familiar(nombre="Emiliano Rui", direccion="San Francisco - California", numero_pasaporte=30567567).save()

print("Se cargo con exito los usuarios de pruebas")
