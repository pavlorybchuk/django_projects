from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    visits = request.session.get("visits", 0)
    visits += 1
    request.session["visits"] = visits

    response = render(
        request,
        "cookies_sessions/index.html",
        {
            "cookies": request.COOKIES,  
            "visits": visits,            
        }
    )
    response.set_cookie("author", "Rybchuk")

    return response