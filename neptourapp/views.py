from django.shortcuts import render
from django.views.generic import *
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework import generics
from .forms import Form, LoginForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
class Home(TemplateView):
    template_name = "navbar.html"


class HomeView(TemplateView):
    template_name = "myhome.html"





class ApiCreateView(ListCreateAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer


class APIRetreiveDestroyDelete(RetrieveUpdateDestroyAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer


class Registration(CreateView):
    template_name = 'registration.html'
    form_class = Form
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        pword = form.cleaned_data['password']
        user = User.objects.create_user(email, '', pword)
        form.instance.user = user
        # login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    

# def loginview(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/website/profile/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'website/login.html', {'form': form})


    # def form_valid(self,form):
    #     email = form.cleaned_data['email']
    #     pword = form.cleaned_data['password']
    #     user = authenticate(email=email, password=pword)
    #     self.thisuser = user
    #     if user is not None:
    #         if user.is_active:

    #             login(self.request, user)
    #     else:
    #         return render(self.request, self.template_name, {
    #             'error': 'your email doesnot exist',
    #             'form': form
    #         })
    #     return super().form_valid(form)




# class Login(FormView):
#     template_name = 'login.html'
#     form_class = LoginForm
#     success_url = '/'

#     def form_valid(self,form):
#         uname = form.cleaned_data['username']
#         pword = form.cleaned_data['password']

#         user = authenticate(username=uname, password=pword)
#         self.thisuser = user
#         if user is not None and user.groups.exists():
#             login(self.request, user)
#         else:
#             return render(self.request, self.template_name, {
#                 'error': 'your username doesnot exist',
#                 'form': form
#             })
#         return super().form_valid(form)
