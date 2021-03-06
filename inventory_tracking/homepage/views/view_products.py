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
    products = prod.Product.objects.all()
    context = {
        # sent to view_products.html:
        'utc_time': utc_time,
        # sent to view_products.html and view_products.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        'products': products,
    }
    return request.dmp_render('view_products.html', context)