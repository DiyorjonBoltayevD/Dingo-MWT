from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import ListView, TemplateView

from dingoapp.forms import BookingForm, LoginForm
from dingoapp.models import FoodModel, Category, Chefs


def index(request):
    exfoods = FoodModel.objects.filter(exclusive=True)[:3]
    category = Category.objects.all()
    cat = request.GET.get('cat')
    chefs = Chefs.objects.filter(level__ch_level="Chef Master")[:3]
    if cat is None:
        cat = "Special"

    foods = FoodModel.objects.filter(category__category_name__contains=cat)[:6]
    tags = FoodModel.objects.filter(tags__tag="Food news")[:3]
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"home_menu": 'home_menu',
               'foods3': foods[:3],
               'foods6': foods[3:6],
               'tags': tags,
               "exfoods": foods[:3], "categories": category,
               "cat": cat,
               "chefs": chefs,
               "form": form
               }
    return render(request, 'index.html', context)


class ChefsView(TemplateView):
    template_name = "chefs.html"

    def get_context_data(self, **kwargs):
        chefs = Chefs.objects.all(**kwargs)
        context = {"chefs": chefs}

        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        my_context = super().get_context_data(**kwargs)
        my_context["chefs"] = Chefs.objects.filter(level__ch_level="Chef Master")
        return my_context

    # def get_context_data(self, **kwargs):
    #     chefs = Chefs.objects.all(**kwargs)
    #     context = {"chefs": chefs}
    #     return context


class MenuView(TemplateView):
    template_name = 'food_menu.html'

    def get_context_data(self, **kwargs):
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = "Special"

        foods = FoodModel.objects.filter(category__category_name__contains=cat)[:6]
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['foods3'] = foods[:3]
        context['foods6'] = foods[3:6]

        return context


class BlogView(TemplateView):
    template_name = "blog-1.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class SingleView(TemplateView):
    template_name = "single-blog-1.html"


class ElementsView(TemplateView):
    template_name = "elements.html"


# class LoginPageView(View):
#     template_name = 'login.html'
#     form_class = LoginForm
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         user = authenticate(
#             username=request.POST.get['username'],
#             password=request.POST.get['password'],
#         )
#         if user is not None:
#             login(request, user)
#             print(user)
#             return redirect('home')
#         message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'form': LoginForm,
                'error': "Error login ",
                }
            return render(request, 'login.html', context)

    else:
        context = {
            'form': LoginForm
        }
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
