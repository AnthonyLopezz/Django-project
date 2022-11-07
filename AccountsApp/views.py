from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib import messages

from AccountsApp.forms.forms import FormUser


def register(request):
    context = {
        'forms': FormUser()
    }
    if request.method == 'POST':
        form_user = FormUser(data=request.POST)
        if form_user.is_valid():
            form_user.save()
            user = authenticate(username=form_user.cleaned_data["username"],
                                password=form_user.cleaned_data['password1'])
            login(request, user)
            return redirect('Store')
    return render(request, 'registration/register.html', context)


'''

def views_user(request):
    list_user = User.objects.all()
    return render(request, 'user_customer/user_view.html', {'list': list_user})



@permission_required('products.delete_products')
def delete_user(request, id):
    user_get = User.objects.get(id=id)
    if request.method == 'POST':
        user_get.delete()
        messages.info(request, 'Delete user in the system.')
        return redirect('views_user')
    return render(request, {'user': user_get})

'''