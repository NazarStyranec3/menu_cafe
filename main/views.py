from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from random import sample
from .models import Category, Product


def catalog(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'main/catalog.html', {
        'lviv': False,
        'categories': categories
    })


def lviv_catalog(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'main/catalog.html', {
        'lviv': True,
        'categories': categories
    })


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.children.all()
    products = Product.objects.filter(category=category)

    return render(request, 'main/category_detail.html', {
        'lviv': False,
        'category': category,
        'subcategories': subcategories,
        'products': products
    })

def lviv_category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.children.all()
    products = Product.objects.filter(category=category)

    return render(request, 'main/category_detail.html', {
        'lviv': True,
        'category': category,
        'subcategories': subcategories,
        'products': products
    })


# def lviv_category_detail(request, category_id):
#     category = get_object_or_404(LvivCategory, id=category_id)
#     subcategories = category.children.all()
#     products = LvivProduct.objects.filter(category=category)
#
#     return render(request, 'main/lviv_category_detail.html', {
#         'lviv': True,
#         'category': category,
#         'subcategories': subcategories,
#         'products': products
#     })


def product_detail(request, category_id, product_id):
    category = get_object_or_404(Category, id=category_id)
    product = get_object_or_404(Product, id=product_id, category=category)

    return render(request, 'main/product_detail.html', {
        'lviv': False,
        'product': product,
        'category': category
    })


# def lviv_product_detail(request, category_id, product_id):
#     category = get_object_or_404(LvivCategory, id=category_id)
#     product = get_object_or_404(LvivProduct, id=product_id, category=category)
#
#     return render(request, 'main/lviv_product_detail.html', {
#         'lviv': True,
#         'product': product,
#         'category': category
#     })
def lviv_product_detail(request, category_id, product_id):
    category = get_object_or_404(Category, id=category_id)
    product = get_object_or_404(Product, id=product_id, category=category)

    return render(request, 'main/product_detail.html', {
        'lviv': True,
        'product': product,
        'category': category
    })
