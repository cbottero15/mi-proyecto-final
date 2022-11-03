from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm
from django.views import View


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
    return render(request, "ejemplo/saludar.html", {"notas": [1,2,3,4,5,6,7,8]})

def imc(request, peso, altura):
    
    imc = peso, altura  # imc = (peso / (altura * altura))

    return render(request, "ejemplo/imc.html", {"imc": imc})
    

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_un_solo_familar(request, id):
    Familiar.objects.get(id)

class BuscarFamiliar(View):
    
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
    
    
class AltaFamiliar(View):
    
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,'msg_exito': msg_exito})
        return render(request, self.template_name, {"form": form})
    

    
    
