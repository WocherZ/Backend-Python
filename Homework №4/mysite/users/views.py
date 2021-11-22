from django.http import JsonResponse, Http404
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
        raise Http404


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
        raise Http404


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
        raise Http404


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
        raise Http404
