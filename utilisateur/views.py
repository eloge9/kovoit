from django.shortcuts import render, redirect


def splash(request):
    return render(request, 'splash.html')

"""login"""
def welcome(request):
    return render(request, 'login/welcome.html')

def connection_phone(request):
    return render(request, "login/loginwithmobile.html")

def verification_phone(request):
    return render(request, "login/otpverification.html")

def connection_reussi(request):
    return render(request, "login/accountconnect.html")


"""inscription"""

def inscription(request):
    return render(request, "inscription/inscription.html")

def compte_create(request):
    return render(request, "inscription/accountcreated.html")

"""acceuil"""

def home(request):
    return render(request, "home.html")

"""logout"""