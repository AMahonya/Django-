from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.IntegerField(max_value=120, min_value=1, label='Введите ваш возраст',
                             help_text='Возраст должен быть не больше 120.')
