from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from userpages.models import UserMod, Plan
from userpages.views import check_code
# from django.core.mail import send_mail
# from django.conf import settings
# from qrgen.settings import EMAIL_HOST_USER
# Create your views here.

def show_main(request):
    context = {
        "plans":None
    }

    plans = Plan.objects.all()
    context["plans"] = plans
    if request.method == "POST":
        if request.user.is_authenticated:
            request.session["plantype"] = request.POST["plantype"]
            return redirect("payment")
        else:
            request.session["plantype"] = request.POST["plantype"]
            return redirect("login")

    response = render(request, "firstpage/main.html", context = context)
    return response

def show_reg(request):
    context = {
        "error_text":f"{check_code(request,'reg')}"
    }
    if request.method == "GET" and request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST" and not request.user.is_authenticated:
        user_name = request.POST.get("name")
        password = request.POST.get("password")
        confirm_password = request.POST["confirm password"]
        email = request.POST.get("email")
        if user_name == '':
            request.session["code_reg"] = "Ім'я не може бути порожнім!"
            return redirect("reg")
        if len(user_name) < 3:
            request.session["code_reg"] = "Ім'я не може бути менше 3 символів!"
            return redirect("reg")
        if len(user_name) > 20:
            request.session["code_reg"] = "Ім'я не може бути більше 20 символів!"
            return redirect("reg")
        if user_name.isdigit() == True:
            request.session["code_reg"] = "Ім'я не може містити лише цифри!"
            return redirect("reg")
        if len(password) < 6:
            request.session["code_reg"] = "Пароль має бути не менше 6 символів!"
            return redirect("reg")
        if password != confirm_password:
            request.session["code_reg"] = "Паролі не співпадають!"
            return redirect("reg")
        try:
            UserMod.objects.create(user = User.objects.create_user(username = user_name, password = password, email = email), plan=Plan.objects.get(plantype="Free"), last_payment="-",qr_scans=0,qr_amount=0)
            user = authenticate(username = user_name, password = password)
            login(request, user)

            if "plantype" in request.session:
                return redirect("payment")
            else:
                return redirect("profile")
        except IntegrityError:
            context["error_text"] = "Користувач вже зареєстрований"
            
    response = render(request, "firstpage/reg.html", context = context)
    return response

def show_auth(request):
    context = {
        "error_text":""
    }
    if request.method == "GET" and request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        password = request.POST.get("password")
        name = request.POST.get("name")
        user = authenticate(username = name, password = password)
        if user != None:
            login(request, user)
            if "plantype" in request.session:
                return redirect("payment")
            else:
                return redirect("profile")
        else:
            context["error_text"] = "Такого користувача не існує або не вірно вказані данні"
    response = render(request, "firstpage/auth.html", context = context) 
    return response
    