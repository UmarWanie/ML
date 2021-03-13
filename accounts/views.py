from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, PredForm, PredForm2, UserLoginForm, userUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method=='POST':
        f = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if f.is_valid() and profile_form.is_valid():
            user = f.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('accounts:home')

    else:
        f = UserForm()
        profile_form = ProfileForm()

    return render(request,'signup.html',{'form':f, 'profile_form':ProfileForm})


def signin(request):
    if request.method=='POST':
        form = UserLoginForm(request= request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('accounts:dashboard')
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")
    form = UserLoginForm()
    return render(request, "signin.html",{"form":form})




def signout(request):
    logout(request)
    messages.success(request, "You are now Logged Out")

    return redirect('accounts:home')






def ad_login(request):
    if request.method=='POST':
        form = AuthenticationForm(request= request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user.is_superuser:
                login(request, user)
                
                userList =User.objects.values()
                return render(request, "dashbaord.html", {"userList":userList})
            else:
                print('im user')
        
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "admin_login.html",{"form":form})




    

def predict_opd(request):
    prediction=username=polyu=polyd=swl=par_par=polyp=BMI=irrit=alop=v_bull=wkns=Gender = 0
    if request.method=='POST':
        form = PredForm2(request.POST)
        if form.is_valid():
                instance = form.save(commit=False)

                username = form.cleaned_data['username']
                Gender = form.cleaned_data['Gender']
                polyu  = form.cleaned_data['Polyuria']
                polyd   = form.cleaned_data['Polydipsia']
                swl  = form.cleaned_data['Sudden_weight_loss']
                par_par  = form.cleaned_data['Partial_paresis']
                polyp   = form.cleaned_data['Polyphagia']
                irrit = form.cleaned_data['Irritability']
                alop    = form.cleaned_data['Alopecia']
                v_bull    = form.cleaned_data['Visual_blurring']
                wkns    = form.cleaned_data['Weakness']
                

                

          



                
                

                prediction = getPredictions(polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns)
                instance.Prediction = prediction
                print(prediction)
                instance.save()
                print(Gender)

                

                



    else:
        form = PredForm2()
    return render( request, "predict_opd.html",{"username":username, "prediction":prediction, "Polyuria":polyu,"Polydipsia":polyd, "Gender":Gender, "Sudden_weight_loss":swl,
     "Partial_paresis":par_par, "Polyphagia":polyp, "Irritability":irrit, "Alopecia":alop,"Visual_blurring":v_bull,'Weakness':wkns,"form": form})




               
    

    



def getPredictions(polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns):

    import pickle
    model      = pickle.load(open("diabetes_ml_Rfcmodel.sav", "rb"))
    prediction = model.predict([[polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns]])


    if prediction == 0:
        return "NO"
    elif prediction == 1:
        return "yes"
    else:
        return "error"



@login_required(login_url='/accounts:signin/')
def predict(request):
    prediction=polyu=polyd=swl=par_par=polyp=BMI=irrit=alop=v_bull=wkns=Gender = 0
    if request.method=='POST':
        form = PredForm(request.POST)
        if form.is_valid():

                polyu  = form.cleaned_data['Polyuria']
                polyd   = form.cleaned_data['Polydipsia']
                swl  = form.cleaned_data['Sudden_weight_loss']
                par_par  = form.cleaned_data['Partial_paresis']
                polyp   = form.cleaned_data['Polyphagia']
                irrit = form.cleaned_data['Irritability']
                alop    = form.cleaned_data['Alopecia']
                v_bull    = form.cleaned_data['Visual_blurring']
                wkns    = form.cleaned_data['Weakness']


          



                instance = form.save(commit=False)
                instance.patient= request.user
                instance.Gender= request.user.profile.gender

            

                Gender= instance.Gender
               
                print(Gender)

                prediction = getPredictions(polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns)
                instance.Prediction = prediction
                print(prediction)
                instance.save()
                print(Gender)



    else:
        form = PredForm()
    return render( request, "predict.html",{"prediction":prediction, "Polyuria":polyu,"Polydipsia":polyd, "Gender":Gender, "Sudden_weight_loss":swl,
     "Partial_paresis":par_par, "Polyphagia":polyp, "Irritability":irrit, "Alopecia":alop,"Visual_blurring":v_bull,'Weakness':wkns,"form": form})




               
    

    



def getPredictions(polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns):

    import pickle
    model      = pickle.load(open("diabetes_ml_Rfcmodel.sav", "rb"))
    prediction = model.predict([[polyu, polyd, Gender, swl, par_par, polyp, irrit, alop, v_bull,wkns]])


    if prediction == 0:
        return "NO"
    elif prediction == 1:
        return "yes"
    else:
        return "error"









@login_required(login_url='/accounts:signin/')
def dashboard(request):
    return render(request, 'dashboard.html')




@login_required(login_url='/signin/')
def myTable(request):
    info = Prediction.objects.filter(patient__id=request.user.id)
    context={
             'info':info
    }


    


    return render(request, 'myTable.html', context)





def profile(request):
    if request.method=='POST':
        u_form=userUpdateForm(request.POST, instance=request.user)
        # p_form=ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid:
            u_form.save()
            # p_form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Profile Not Updated??')
    else:

        u_form=userUpdateForm(request.POST, instance=request.user)
        # p_form=ProfileForm(request.POST, instance=request.user.profile)


    return render(request, 'profile.html', {'u_form':u_form})