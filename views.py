from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "index.html", context=context)

def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre,camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html",context)

def estudiantes(request):
    return render(request, "base.html")

def profesores(request):
    return render(request, "base.html")

def guardar_curso(request):
    curso = Curso(nombre="Python", camada=23800)
    curso.save()
    return HttpResponse("Usuario Creado Exitosamente")

