from django.shortcuts import render

# Create your views here.

def index(request):

    suma = 5 + 10
    return render(request, "ejemplo/saludar.html",
    {
        "nombre":"Claudio",
        "apellido": suma,
        
        })

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",
    {
        "nombre":nombre,
        "apellido":apellido,

    })

def index_tres(request):
    
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )

    def imc(request, peso, altura):
        imc = 1
        return render(request, "ejemplo/imc.html", {"imc":imc"})
        