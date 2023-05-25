from django import forms
from app.models import User
from app.models import Tryacess

def validate_username_not_in_users(username):
    try_access = Tryacess.objects.filter(name=username).first()
    if User.objects.filter(name=username).exists() and try_access and try_access.login_try >= 10:
        raise forms.ValidationError('Bloqueado!Entre em contato com o administrador do sistema.')
    elif not User.objects.filter(name=username).exists() and try_access and try_access.login_try >= 10:
        raise forms.ValidationError('Bloqueado!Entre em contato com o administrador do sistema.')
    elif not User.objects.filter(name=username).exists():
        if try_access:
            try_access.login_try += 1
            try_access.save()
            raise forms.ValidationError('Nome de usuário não existe.')
                            
        else:
            try_access = Tryacess.objects.create(name=username, login_try=1)
            try_access.save()
            raise forms.ValidationError('Nome de usuário não existe.')
    
def validate_password_not_in_users(username,password):
    try_access = Tryacess.objects.filter(name=username).first()

    if not User.objects.filter(password=password).exists() and User.objects.filter(name=username).exists():
        if try_access:
            try_access.login_try += 1
            try_access.save()
            raise forms.ValidationError('Senha Inválida.')
        else:
            try_access = Tryacess.objects.create(name=username, login_try=1)
            try_access.save()
            raise forms.ValidationError('Senha Inválida.')
        

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        validators=[validate_username_not_in_users],
        error_messages={
            'required': 'Por favor, informe o nome de usuário.',
        }
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Por favor, informe a senha.',
        }
    )
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        validate_password_not_in_users(username, password)
        return password
