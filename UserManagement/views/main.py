from django.shortcuts import render
from UserManagement.forms.signup_form import SignupForm

__author__ = 'Iman'

def main_page(request):
    form = SignupForm()
    return render(request, 'UserManagementUI/homepage.html', {'form': form, 'login_error': False,
                                                              'forget_password_error': False,
    })
