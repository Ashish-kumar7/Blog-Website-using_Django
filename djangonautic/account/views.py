from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
#sign up view
def signup_veiw(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #login the user
            login(request,user)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    
    return render(request,'account/signup.html',{'form':form})

#login view
def login_veiw(request):
    if request.method=='POST':
         form=AuthenticationForm(data=request.POST)
         if form.is_valid():
             #login the user
             user=form.get_user()
             login(request,user)
             if 'next' in request.POST:
                return redirect(request.POST.get('next'))
             else:
                return redirect('articles:list')
    else:
        form=AuthenticationForm()

    return render(request,'account/login.html',{'form':form})

#log out view
def logout_veiw(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')

