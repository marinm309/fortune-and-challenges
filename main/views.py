from django.shortcuts import render, redirect
from . models import Fortune, UserFortune
from random import choice
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

def home(request):
    context = {}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def fortune(request):
    user = request.user.customer
    items = Fortune.objects.all()
    new_items_list = []
    old_items_list = []
    
    for i in items:
        if UserFortune.objects.filter(fortune=i, user=user).count() == 0:
            new_items_list.append(i)
        else:
            old_items_list.append(i)

    try:
        item = choice(new_items_list)
        UserFortune.objects.create(fortune=item, user=user)
    except:
        item = {'description': 'Няма нови късметчета!'}

    context = {'item': item, 'old_items_list': old_items_list}
    return render(request, 'main/fortune.html', context)


@login_required(login_url='login')
def challenge(request):
    context = {}
    return render(request, 'main/challenge.html', context)


@login_required(login_url='login')
def wheel(request):
    context = {}
    return render(request, 'main/wheel.html', context)


login_required(login_url='login')
def update_customer_credits(request):
    customer = request.user.customer
    data = json.loads(request.body)
    amount = data['amount']
    print(amount)
    if amount == 'БАНКРУТ':
        customer.credits = 0
        customer.save()
        return JsonResponse({'credits': customer.credits})
    elif amount == 'ОПИТАЙ ПАК':
        pass
    else:
        customer.credits += int(amount)
        customer.save()
        return JsonResponse({'credits': customer.credits})
