from django.http import HttpResponse
from django.shortcuts import render


#is one hard way to prepare a page
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <h1>Bienvenue sur mon blog !</h1>
    <p>Les crépes bretonnes ça tue des mouettes en plein vol
    !</p>"""
    return HttpResponse(text)

#here is from a template
def index(request):
  return render(request, 'blog/home.html')#is in the folder templates  in
  #forlder blog
