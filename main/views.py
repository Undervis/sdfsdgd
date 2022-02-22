from django.shortcuts import render, get_object_or_404
from .models import Items


def home(request):
    items = Items.objects.all()
    return render(request, 'home.html', {'items': items})


def item(request, pk):
    item_pk = get_object_or_404(Items, pk=pk)
    return render(request, 'item.html', {'item': item_pk})