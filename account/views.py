from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import User
# Create your views here.
from django.contrib.auth import logout
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, SuperUserCreateForm


class UserListView(ListView):
    model = User
    template_name = "account/user_list.html"


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect("")


class CreateSpecialUser(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "account/special_user.html"

    def form_valid(self, form):
        special_user = form.save(commit=False)
        special_user.is_special_user = True
        special_user.save()
        return super(CreateSpecialUser, self).form_valid(form)


class CreateAdminUser(CreateView):
    model = User
    form_class = SuperUserCreateForm
    template_name = "account/create_admin.html"

    def form_valid(self, form):
        special_user = form.save(commit=False)
        special_user.is_admin = True
        special_user.save()
        return super(CreateAdminUser, self).form_valid(form)


class AdminUserList(ListView):
    queryset = User.objects.filter(is_admin=True)
    template_name = "account/admin_list.html"
