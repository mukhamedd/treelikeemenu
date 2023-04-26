from django.shortcuts import render
from .models import MenuItem
from django.http import HttpResponse

def menu(request):
    menu_items = MenuItem.objects.filter(parent=None)
    return render(request, 'menu.html', {'menu_items': menu_items})
def menu_detail(request, item_name):
    try:
        item = MenuItem.objects.get(name=item_name)
    except MenuItem.DoesNotExist:
        item = None
    context = {
        'item': item,
        'get_item': item_name
    }

    return render(request, 'menu_detail.html', context)