from django.shortcuts import render, redirect
from a_home.models import Item
from django.http import HttpResponse
def home_view(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home.html', context)

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        item = Item.objects.create(name=name)
        item.save()
        return HttpResponse(f'<h1>Item created {item.name}</h1>')
    else:
        return redirect('home')