from django.shortcuts import render
from . models import Fortune, UserFortune
from random import choice
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def fortune(request):
    user = request.user.customer
    items = Fortune.objects.all()
    new_items_list = []
    
    for i in items:
        if UserFortune.objects.filter(fortune=i, user=user).count() == 0:
            new_items_list.append(i)

    item = choice(new_items_list)
    #UserFortune.objects.create(fortune=item, user=user)

    context = {'item': item}
    return render(request, 'main/fortune.html', context)
