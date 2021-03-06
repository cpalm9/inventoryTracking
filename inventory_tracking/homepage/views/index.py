from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as prod
from django import forms
from formlib.form import FormMixIn
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):
    utc_time = datetime.utcnow()
    products = prod.Product.objects.all().order_by('-date')
    manufacturers = prod.Product.objects.all().distinct('manufacturer')
    todayProds = prod.Product.objects.filter(date=datetime.now())
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        'products': products,
        'manufacturers': manufacturers,
        'todayProds': todayProds,
    }
    return request.dmp_render('index.html', context)