from django.shortcuts import render, redirect
from merchant.models import *
import stripe
from stripe_service.settings import STRIPE_API_KEY
from django.core.exceptions import BadRequest
from django.http import HttpResponse


stripe.api_key = STRIPE_API_KEY

def get_item(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'item.html', context={'item':item})

def create_checkout_session(request, pk):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': request.POST['name'],
            },
            'unit_amount': int(float(request.POST['unit_amount'])*100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
        )
        return redirect(session.url, code=303)
    return HttpResponse("{'error':'bad request'}", status=400)