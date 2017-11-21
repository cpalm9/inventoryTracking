from django.conf import settings
from django_mako_plus import view_function, jscontext
from .. import dmp_render, dmp_render_to_string
from datetime import datetime, timezone
from homepage import models as prod
from django import forms
from formlib.form import FormMixIn
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from homepage import models as hmod

@view_function
def process_request(request):

    form = LoginForm(request)

    if form.is_valid():

        form.commit(request)

        return HttpResponseRedirect('/homepage/index/')

    return dmp_render(request, 'login.html', {
        'form': form,
    })

    class LoginForm(FormMixIn, forms.Form):
        form_submit = 'LOGIN'
        def init(self):
            self.fields['username'] = forms.CharField(label="USERNAME", required=True, max_length=100)
            self.fields['password'] = forms.CharField(label="PASSWORD", required=True, widget=forms.PasswordInput)

        def clean(self):
            tempUser = hmod.User.objects.get(username="manager")
            if tempuser is None:
                newUser = hmod.User()
                newUser.username = "manager"
                newUser.set_password("Password1")
                newUser.save()
            self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
            if self.user is None:
                #way of saying whether or not you're happy with the form. Sets Is_Valid to false
                raise forms.ValidationError('Invalid username or password.')
            return self.user

        def commit(self, request):
            #login
            login(self.request, self.user)
