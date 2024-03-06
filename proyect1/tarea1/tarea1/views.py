from django.http import HttpResponse
def saludo (request):
    documento= "<html><body><h1>hola Mundo <html><body><h1>"
    return HttpResponse (documento)
def despedida (request):
    documento="<html><body><h1> CHAU<h1><body><html>"
    return HttpResponse (documento)
def damefecha (request):
    