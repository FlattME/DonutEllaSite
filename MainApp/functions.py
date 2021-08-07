import random

from django.shortcuts import render, redirect, reverse
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *

from email.mime.multipart import MIMEMultipart
import os
import smtplib
from email.mime.text import MIMEText
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'azzzzzzzzz495@gmail.com'
EMAIL_HOST_PASSWORD = '$asha2004--2004'
EMAIL_PORT = 587


def send_mail_(email, subject, text):
    addr_from = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject

    body = text
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)

    server.login(addr_from, password)

    server.send_message(msg)
    server.quit()
    return True


def generate_code(range_):
    c = [i for i in 'qwertyuiopasdfghjklzxcvbnm1234567890']
    ret = ''
    for i in range(range_):
        ret += random.choice(c)
    return ret


def register_func(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():  # Почта уже зарегестрирована?
            # ошибка
            messages.error = [request, 'Пользователь с этим адресом уже зарегестрирован']
        else:
            if form.is_valid():
                ins = form.save()
                # username = form.cleaned_data['username']
                # password = form.cleaned_data['password1']
                # if password == form.cleaned_data['password2']:  # Проверяем совпадают ли пароли
                if True:
                    user = authenticate(username='username', password='password', email=email)
                    ins.email = email
                    ins.save()
                    form.save_m2m()
                    messages.success(request, 'Вы успешно зарегистрировались')
                    return redirect('/')
                else:
                    # ошибка
                    messages.error = [request, 'Пароли не совпадают']
    else:
        form = UserRegisterForm()

    return form

