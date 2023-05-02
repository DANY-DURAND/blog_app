from django.shortcuts import render

# Create your views here.
error_message = "Invalid Credentials"
def index(request):
    return render( request, "login.html",
                    {
                        "error_message": error_message,
                    })