from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect


def is_registered():
    return True


def user(request):
    if request.method == "GET":
        if is_registered():
            return render(request, 'user.html')
        else:
            return redirect('registration')

    else:
        return HttpResponseNotAllowed(["GET"])


def order(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "User orders page",
            "user_orders": [
                "order 1",
                "order 2",
            ]
        })

    else:
        return HttpResponseNotAllowed(["GET"])


def cart(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "User cart page",
            "user_cart": [
                "product 1",
                "product 2",
            ]
        })

    else:
        return HttpResponseNotAllowed(["GET"])


def registration(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "Registration user page. There will be a form"
        })
    elif request.method == "POST":
        return JsonResponse({
            "method": "POST",
            "success": True,  # or False
        })
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
