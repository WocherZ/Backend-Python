from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, DeleteView

from .forms import ProductForm
from .models import Product, Category


def login_required(function):
    def decorator(request):
        if request.user.is_authenticated:
            return function(request)
        else:
            return HttpResponseForbidden()
    return decorator



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


@require_http_methods(["GET", "POST"])
def add(request):
    error = ''
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            error = 'Форма была неверной'

    form = ProductForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, "add.html", data)


class UpdateProduct(UpdateView):
    model = Product
    template_name = "add.html"

    fields = ["product_name", "category", "product_image", "description"]


class DeleteProduct(DeleteView):
    model = Product
    template_name = "delete.html"
    success_url = '/shop/category/'


def login(request):
    context = {}
    if request.user.is_authenticated:
        print("Пользователь залогинин")
        context['is_auth'] = True
        context['user_name'] = request.user
    else:
        print("Анонимус")
        context['is_auth'] = False


    return render(request, 'login.html', context=context)


@login_required
def private(request):

    return render(request, 'private.html')
