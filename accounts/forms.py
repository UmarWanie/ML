from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Prediction, Prediction2


from django.contrib.auth.forms import AuthenticationForm




class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input'
            
        }
))





class UserForm(UserCreationForm):

    class Meta:
      model=User
      fields = ('username', 'email', 'password1', 'password2')
      widgets= {
            'username': forms.TextInput(attrs={'class':'input'}),

            'email': forms.EmailInput(attrs={'class':'input'}),

            'password1':forms.PasswordInput(attrs={'class':'input'}),
            'password2':forms.PasswordInput(attrs={'class':'input'})
        }










    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'input'}))
    # email= forms.CharField(widget=forms.EmailInput(
    #     attrs={
    #         'class': 'input'
            
    #     }))

    password1= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input'
            
        }))
    password2= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input'
            
        }
))
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'gender')
        widgets= {
            'gender': forms.Select(attrs={'class':'form-control col-md-6'}),

            'age': forms.TextInput(attrs={'class':'input'})
            
        }









class PredForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ('Polyuria','Polydipsia', 'Sudden_weight_loss', 'Partial_paresis', 'Polyphagia', 'Irritability', 'Alopecia', 'Visual_blurring', 'Weakness')
        widgets= {
            'Polyuria': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Polydipsia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Sudden_weight_loss': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Partial_paresis': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Polyphagia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Irritability': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Alopecia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Visual_blurring': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Weakness': forms.Select(attrs={'class':' form-control col-md-3'})
            
        }







class PredForm2(forms.ModelForm):
    class Meta:
        model = Prediction2
        fields = ('username', 'Gender', 'Polyuria','Polydipsia', 'Sudden_weight_loss', 'Partial_paresis', 'Polyphagia', 'Irritability', 'Alopecia', 'Visual_blurring', 'Weakness')
        widgets= {

            'username': forms.TextInput(attrs={'class': 'form-control col-md-3'}),
            'Gender': forms.Select(attrs={'class': 'form-control col-md-3'}),
            'Polyuria': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Polydipsia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Sudden_weight_loss': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Partial_paresis': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Polyphagia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Irritability': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Alopecia': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Visual_blurring': forms.Select(attrs={'class':' form-control col-md-3'}),
            
            'Weakness': forms.Select(attrs={'class':' form-control col-md-3'})
            
        }





class userUpdateForm(UserChangeForm):
    class Meta:
        model= User
        fields=('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class':' form-control '}),
            'email': forms.EmailInput(attrs={'class':' form-control'}),
            'first_name': forms.TextInput(attrs={'class':' form-control'}),
            'last_name': forms.TextInput(attrs={'class':' form-control'}),
        }