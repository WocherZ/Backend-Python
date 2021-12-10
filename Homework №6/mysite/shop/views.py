from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.shortcuts import render

from .models import Product, Category


def shop(request):
    if request.method == "GET":
        context = {
            "info": "Information about shop",
            "links": "Links to social networks",
        }
        return render(request, "shop.html", context=context)

    else:
        return HttpResponseNotAllowed(["GET"])


def category_list(request):
    if request.method == "POST":
        return JsonResponse({
            "method": "POST",
            "search": "result",
        })

    elif request.method == "GET":
        categories = []
        for element in Category.objects.all():
            categories.append({
                "category_name": element.category_name
            })
        context = {'categories': categories}
        return render(request, 'categories.html', context=context)
    else:

        return HttpResponseNotAllowed(["GET", "POST"])


def category(request, category_id):
    if request.method == "POST":
        return JsonResponse({
            "method": "POST",
            "products": [
                "product 1",
                "product 2",
            ]
        })

    elif request.method == "GET":
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

    else:
        return HttpResponseNotAllowed(["GET", "POST"])


def product(request, product_id):
    if request.method == "GET":
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


    else:
        return HttpResponseNotAllowed(["GET"])
