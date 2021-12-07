from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .models import AssessmentForm 


def home(request):
    Answers= AssessmentForm.objects.filter(username=request.user.username).order_by(-'id')[0]
    list = [Answers.chronic,Answers.tenderness,Answers.symptoms,Answers.feeling]
    score = list.count("Yes")
    if score>=3:
      message = Answers.username + "Your condition is severe"
    else:
       message = Answers.username + "Your condition is mild" 
    #return render(request,'vaccidocapp/home.html' ,{'message':message,'score':score})
    return render(request,'vaccidocapp/home.html' ,{'message':message,'score':score})


def Assessment(request):
    if request.method =="POST":
        username=request.user.username
        age=request.POST['age']
        vaccine=request.POST['vaccine']
        chronic=request.POST['chronic']
        tenderness=request.POST['tenderness']
        symptoms=request.POST['symptoms']
        feeling=request.POST['feeling']
        form = AssessmentForm(username= username,age= age,vaccine= vaccine,chronic= chronic,tenderness= tenderness,symptoms= symptoms,feeling= feeling)
        form.save()
        messages.success(request, f'your Assessment form has been sucessfully submitted')
        return redirect('vaccidocapp-home')
    else:
        form = AssessmentForm()
        return render(request,'users/Assessment.html')


def register(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Your account has been sucessfully created! you can able to login now')
             return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
      u_form = UserUpdateForm(request.POST,instance=request.user)
      if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been sucessfully updated')
            return redirect('profile')
    else:
      u_form = UserUpdateForm(instance= request.user)

    context = {
        'u_form': u_form,
    }

    return render(request,'users/profile.html',context)