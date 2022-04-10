from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from cart.forms import CartAddProductForm

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request, 'product/detail.html', {'product': product})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('app:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:home')
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('app:login')


class ViewNumbers(ListView):
    model = Numbers
    template_name = 'app/Cards.html'
    context_object_name = 'items'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Номера'
        return context


class GetCardNumbers(DetailView):
    model = Numbers
    pk_url_kwarg = 'number_id'
    template_name = 'app/Card.html'
    context_object_name = 'item'


class ViewMenu(ListView):
    model = Menu
    template_name = 'app/Cards.html'
    context_object_name = 'items'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ресторанное меню'
        return context


class GetCardMenu(DetailView):
    model = Menu
    pk_url_kwarg = 'menu_id'
    template_name = 'app/Card.html'
    context_object_name = 'item'


class ViewExcursion(ListView):
    model = Excursion
    template_name = 'app/Cards.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Экскурсии'
        return context


class GetCardExcursion(DetailView):
    model = Excursion
    pk_url_kwarg = 'excursion_id'
    template_name = 'app/Card.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Экскурсии'
        return context


def HomePage(request):
    return render(request, 'app/index.html')


def mail_template(request):
    return render(request, 'inc/mail_template.html')

def Cards__numbers(request):
    return render(request, 'app/cards__numbers.html')


def Basket(request):
    return render(request, 'app/Basket.html')


def Orders(request):
    return render(request, 'app/orders.html')
