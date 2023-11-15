import json
from django.db.models import Q
from itertools import chain
from django.db.models import Sum
from django.utils import timezone

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
# from wejegeh.forms import ErzakForm     #hesap klasörünün altındakı forms.py kategoriyi import ettik
from wejegeh.models import DüzenliÖdeme


import random #rastgele sayı üretmek için
from django.db.models.functions import TruncMonth
from django.db.models import F
import os
from django.contrib.auth.decorators import login_required, user_passes_test #loginmi kontrolleri için ilk parametre normal kullanıcılar ikincisi superuser kullanıcı için geçerli

from django.contrib import messages
from datetime import datetime

def my_view(request):
    düzenliödeme = DüzenliÖdeme.objects.all()
    # Geri kalan kod buraya eklenir





def fonksiyonx():
    şu_an = datetime.now().date()
    düzenliödeme = DüzenliÖdeme.objects.all()
    print(düzenliödeme)
    düzenliödeme_listesi = []

    for i in düzenliödeme:
        for detay in i.detay.all():
            if detay.ödendimi is False:
                kalan_gün = (detay.ödemeson - şu_an).days
                # print(kalan_gün)
                if kalan_gün <= 0:
                    renk = "D50000"
                    # print("ödeme tarihi geçmiş")
                elif 0 <= kalan_gün <= 10:
                    renk = "F44336"
                    # print("Sayı 0 ile 10 arasındadır.")
                else:
                    renk = "AEEA00"  
                düzenliödeme_listesi.append({
                    'kategori': i.kategori,
                    'toplamtaksit': i.toplamtaksit,
                    'notekle': i.notekle,
                    'taksitsayısı': detay.kaçıncı_taksit,
                    'tutar': detay.tutar,
                    'ödemeilk': detay.ödemeilk,
                    'ödemeson': detay.ödemeson,
                    'ödendimi': detay.ödendimi,
                    'detaynotekle': detay.notekle,
                    'id': detay.id,
                    'kalangün': kalan_gün,
                    'renk': renk,
                })

                düzenliödeme_listesi = sorted(düzenliödeme_listesi, key=lambda x: x['kalangün'])
                break
            else:
                pass







