from multiprocessing import context
from django.shortcuts import HttpResponse, render
from productos.views import *
from django.core.paginator import Paginator

html_base = """
    "<h1>MARY CAKES</h1>
    <ul>
        <li><a href="/">PORTADA</a></li>
        <li><a href="/torta/">TORTAS</a></li>
        <li><a href="/postre/">POSTRES Y BOCADITOS</a></li>
        <li><a href="/about/">SOBRE NOSOTROS</a></li>
        <li><a href="/contact/">CONTACTO</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    torta = Torta.objects.all()
    postre = Postres.objects.all()
    context ={
        'torta':torta,
        'postre':postre
    }
    if torta and postre:
        paginator = Paginator((torta, postre), 6)
        page_number = request.GET.get('page')
        digital_products_data = paginator.get_page(page_number)
    return render(request, "core/home.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")
