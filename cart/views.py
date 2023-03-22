from django.shortcuts import ( 
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view that renders the cart content page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart """

    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
