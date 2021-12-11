from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Product, Category


@require_http_methods(["GET"])
def shop(request):
    context = {
        "info": "Information about shop",
        "links": "Links to social networks",
    }
    return render(request, "shop.html", context=context)


@require_http_methods(["GET"])
def category_list(request):
    categories = []
    for element in Category.objects.all():
        categories.append({
            "category_name": element.category_name
        })
    context = {'categories': categories}
    return render(request, 'categories.html', context=context)


@require_http_methods(["GET"])
def category(request, category_id):
    try:
        necessary_category = Category.objects.get(id=category_id)
        items = []
        for item in Product.objects.filter(category=necessary_category):
            item = {
                "name": item.product_name
            }
            items.append(item)

        context = {'category_name': necessary_category.category_name,
                   'items': items}
        return render(request, 'category.html', context=context)

    except ObjectDoesNotExist:
        raise Http404


@require_http_methods(["GET"])
def product(request, product_id):
    try:
        product_by_id = Product.objects.get(id=product_id)
        context = {
            "product_number": product_id,
            "product_name": product_by_id.product_name,
            "product_category": product_by_id.category,
            "image_link": product_id,
        }
        return render(request, "product.html", context=context)
    except ObjectDoesNotExist:
        raise Http404
