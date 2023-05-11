from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from .forms import UserForm

def index(request):
    form = UserForm(request.POST or None, initial={'categoryProduct_id': 0})
    id = 0
    if form.is_valid():
        id = form.cleaned_data.get("categoryProduct_id")
    data = list(Product.objects.all().filter(idCategory=int(id)))
    print(data)
    context = {
        'data': data,
        'form': form
    }
    return render(request, 'index.html', context)
    #return HttpResponse("aaa")