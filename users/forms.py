from django.forms import PasswordInput, TextInput, CharField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from . models import Customer

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={"autofocus": True, 'class': 'form-control form-control-lg', 'id': 'typeEmailX'}))
    password = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control form-control-lg', 'id': 'typePasswordX'}),
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Имейл'
        self.fields['password'].label = 'Парола'

class SignUpForm(UserCreationForm):
    name = CharField(max_length=50, min_length=5)
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Имейл'
        self.fields['password1'].label = 'Парола'
        self.fields['password2'].label = 'Повтори парола'
        self.fields['name'].label = 'Имена'
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "current-password", 'class': 'form-control form-control-lg'})

    def save(self, commit=True):
        user = super().save(commit=commit)
        name = self.cleaned_data['name']
        customer = Customer(name=name, user=user)

        if commit:
            customer.save()

        return user

    