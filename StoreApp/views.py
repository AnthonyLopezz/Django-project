from django.db.models import Q
from django.shortcuts import render
from .models import Product, CategoryProd
from django.core.paginator import Paginator # import Paginator

# Create your views here.


def store(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    searched = request.POST.get('search')
    if searched:
        users = Product.objects.filter(
            Q(username__icontains=searched) |
            Q(first_name__icontains=searched) |
            Q(last_name__icontains=searched) |
            Q(email__icontains=searched)
        ).distinct()

    return render(request, "store/store.html", {'products': page_obj})


def cart(request):

    return render(request, "store/cart.html")
