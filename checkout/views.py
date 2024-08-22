from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Pqdn2P1ZrR5cUNYFwT9atwcjZMhh3l1p2f4YHZ1xN7ujRZRUIvNjRzoP7EFUtlTAQi4vVTVQpgL3t6Rwp9UkyPA00zpTSPak5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)