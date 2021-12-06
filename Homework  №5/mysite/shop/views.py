from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render


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
        print(request.POST)
        return JsonResponse({
            "method": "POST",
            "search": "result",
        })
    elif request.method == "GET":
        print(request.GET)
        return JsonResponse({
            "description": "Page with list of categories",
            "list of categories": [
                "dairy products",
                "fruits",
                "vegetables",
            ],
        })

    else:
        return HttpResponseNotAllowed(["GET", "POST"])


def category(request, category_id):
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({
            "method": "POST",
            "products": [
                "product 1",
                "product 2",
            ]
        })
    elif request.method == "GET":
        print(request.GET)
        return JsonResponse({
            "description": "Page with some category",
            "category_id": category_id,
            "category_name": "dairy products",
            "products": [
                "milk",
                "cheese",
            ]
        })
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


def product(request, product_id):
    if request.method == "GET":
        return JsonResponse({
            "description": "Page with some product",
            "product_id": product_id,
            "product_name": "milk",
            "product_image": "some.png",
            "product_description": "fresh and delicious",
        })

    else:
        return HttpResponseNotAllowed(["GET"])
