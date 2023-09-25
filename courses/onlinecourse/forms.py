from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),  # Obtiene todos los grupos disponibles
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        # Configura el helper de crispy-forms
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            'group',
            Submit('submit', 'Registrarse')
        )

