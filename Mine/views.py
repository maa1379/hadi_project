from django.shortcuts import render, redirect,get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Madan
from django.views.generic import ListView,DetailView

class MadanListView(ListView):
    model = Madan
    template_name = "madan/madan_list.html"

class MadanDetail(DetailView):
    def get(self,request,id):
        madan=get_object_or_404(Madan,id=id)
        return madan

    template_name = "madan/detail.html"

# # Create your views here.
#
# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username", "password")
#         labels = {"username": "نام کابری", "password": "رمز عبور"}
#
#
# def UserRegister(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = User.objects.create_user(username=cd["username"], password=cd["password"])
#             messages.success(request, "اطلاعات شما با موفقیت ثبت شد")
#             return redirect("")
#     else:
#         form = UserRegisterForm()
#     return render(request, "register.html", {"form": form})
#
#
# from django.urls import path
#
# app_name = "config"
