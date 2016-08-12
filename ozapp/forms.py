from django import forms
from .models import Evento
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap3_datetime.widgets import DateTimePicker


# from functools import partial
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # nome = forms.CharField(required=True)
    # sobrenome = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


    #Pegar os dados so usuário e passar para as variáveis
    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class CadastroEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ("nome",
            "tipo",
            "idade_minima",
            "idade_maxima",
            "data_criacao",
            "data_inicio",
            "data_fim",
            "local",
            "cidade",
            "estado",
            "cep",
            "endereco",
            "bairro")

    # def save(self, commit=True):
    #     evento = super(CadastroEvento, self).save(commit=False)
    #     # user.email = self.cleaned_data['email']
    #     # user.first_name = self.cleaned_data['first_name']
    #     # user.last_name = self.cleaned_data['last_name']

    #     if commit:
    #         evento.save()

    #     return evento

