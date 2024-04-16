from django.shortcuts import render
from .models import Accessory, Coupon

from django.core.paginator import Paginator

def all_accessories(request):
    accessories_list = Accessory.objects.all()

    # Get the query parameters
    type_query = request.GET.get('type')
    price_query = request.GET.get('price')

    # Filter the accessories based on the query parameters
    if type_query:
        accessories_list = accessories_list.filter(type__name=type_query)
    if price_query:
        accessories_list = accessories_list.filter(price__lte=price_query)

    # Create a Paginator object
    paginator = Paginator(accessories_list, 9)  # Show 5 accessories per page

    # Get the page number from the query parameters
    page_number = request.GET.get('page')

    # Get the accessories for the current page
    accessories = paginator.get_page(page_number)

    return render(request, 'boutiquesensations/all_accessories.html', {'accessories': accessories})

def cart(request):
    # Aquí necesitarás implementar la lógica para obtener los accesorios que el usuario ha agregado al carrito.
    # Por ahora, solo renderizamos una página vacía.
    return render(request, 'boutiquesensations/cart.html')