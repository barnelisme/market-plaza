from django.shortcuts import render
from item.models import Category, Item
from django.http import HttpResponse
from django.template import loader

from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=True)[0:6]
    categories = Category.objects.all()

    return render(request,'core/index.html', {
        'categories': categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def inde(request):
  items = Item.objects.filter(is_sold=True)[0:6].values()
  categories = Category.objects.all()
  template = loader.get_template('core/index.html')
  context = {
    'items': items,   
  }
  return HttpResponse(template.render(context, request))


def signup (request):
   form = SignupForm()

   return render(request, 'core/signup.html',{
      'form': form
   })

