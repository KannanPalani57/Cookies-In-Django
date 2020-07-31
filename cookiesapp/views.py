from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def cookies_creation(request):
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set Successfully")
        response.set_cookie('color','blue',5)  #1-name of the cookie, 2- value of the cookie
        return response
    else:
        return HttpResponse("Your Favorite color is {0}".format(request.COOKIES['color']))


def track_user(request):
    response = render(request, "base.html")
    if not request.COOKIES.get('visit'):
        response.set_cookie('visit', "1")
    else:
        visit = int(request.COOKIES.get('visit'))+1
        response.set_cookie('visit',str(visit))
    return response         



def delete_cookie(request):
    if request.COOKIES.get('visit'):
        sendResponse = HttpResponse("The cookie cleared successfully")
        sendResponse.delete_cookie('visit')
    else:
        sendResponse = HttpResponse("Now, We are not tracking(countingTheVisits) you, You deleted the Cookie Already")
    return sendResponse        


def home_page(request):
    return render(request, "base.html")




