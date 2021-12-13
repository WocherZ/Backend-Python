from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods



def is_registered():
    return True


@require_http_methods(["GET"])
def user(request):
    if is_registered():
        return render(request, 'user.html')
    else:
        return redirect('registration')


@require_http_methods(["GET"])
def order(request):
    return JsonResponse({
        "description": "User orders page",
        "user_orders": [
            "order 1",
            "order 2",
        ]
    })


@require_http_methods(["GET"])
def cart(request):
    return JsonResponse({
        "description": "User cart page",
        "user_cart": [
            "product 1",
            "product 2",
        ]
    })


@require_http_methods(["GET", "POST"])
def registration(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "Registration user page. There will be a form"
        })

    else:
        return JsonResponse({
            "method": "POST",
            "success": True,  # or False
        })



