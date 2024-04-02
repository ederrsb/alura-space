from django.shortcuts import render

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescop.org / NASA / James Webb"},
        2: {"nome": "Gal�xia MGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
