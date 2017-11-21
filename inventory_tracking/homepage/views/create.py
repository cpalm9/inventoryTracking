from django.conf import settings
from django_mako_plus import view_function, jscontext
from .. import dmp_render, dmp_render_to_string
from datetime import datetime, timezone
from homepage import models as prod
from django import forms
from formlib.form import FormMixIn
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@view_function
@login_required(login_url='/homepage/welcome/')
def process_request(request):
    # process the form
    form = CreateForm(request)

    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/')

    context = {
        'form': form,
    }

    return dmp_render(request, "add_product.html", context)

class CreateForm(FormMixIn, forms.Form):
    def init(self):
        self.fields['manufacturer'] = forms.CharField(label='Product Name', max_length=100)
        self.fields['man_part_number'] = forms.IntegerField(label='Part Number')
        self.fields['description'] = forms.CharField(label='Description' )
        self.fields['man_notes'] = forms.CharField(label='Special Notes' )
        self.fields['city'] = forms.CharField(label='City' )
        self.fields['state'] = forms.CharField(label='State' )
        self.fields['country'] = forms.CharField(label='Country' )
        self.fields['zipcode'] = forms.IntegerField(label='Zipcode' )




    def commit(self):
        product = prod.Product()
        l = prod.Location()
        product.manufacturer = self.cleaned_data.get('manufacturer')
        product.man_part_number = self.cleaned_data.get('man_part_number')
        product.description = self.cleaned_data.get('description')
        product.man_notes = self.cleaned_data.get('man_notes')
        l.city = self.cleaned_data.get('city')
        l.state = self.cleaned_data.get('state')
        l.country = self.cleaned_data.get('country')
        l.zipcode = self.cleaned_data.get('zipcode')
        l.save()
        product.location = l
        product.save()
