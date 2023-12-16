from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils.html import escape
from django.views import View


def main(request):
    return HttpResponse("Hi")

def funky(rquest):
    response = """
    <html>
    <body>
    <p>This is the funky function sample</p>
    <a href="https://github.com/csev/dj4e-samples">gitjubsamples</a>
    </body>
    </html>
    """
    return HttpResponse(response)

def danger(request):
    response = f"""
    <html>
    <body>
    <p>Your gess is:{escape(request.GET['guess'])}</p>
    <a href="https://github.com/csev/dj4e-samples">gitjubsamples</a>
    </body>
    </html>
    """
    return HttpResponse(response)


def template(request):
    data = {'text':"This is a simple text wich is displayes with templates"}
    return render(request,'views/template.html',data)


def game(request,guess):
    data = {"guess" :int(guess)}
    return render(request,"views/games.html",data)


def loop(request):
    fruits = ['apple','banana','watermelon']
    nuts = ['peanut','cashew']
    data = {"fruits":fruits,'nuts':nuts}
    return render(request,"views/loops.html",data)

def nested(request):
    data = {'user':{"name":"Mosi"}}
    return render(request,'views/nested.html',data)

def usingbase(Request,guess):
    data = {'guess':guess}
    return render(Request,'views/game2.html',data)

def revurl(request):
    return render(request,'views/reversurl.html')

class RestMainView(View):
    def get(self,request,guess):
        response = f"""
        <html>
        <body>
        <p>Your gess is:{escape(guess)}</p>
        <a href="https://github.com/csev/dj4e-samples">gitjubsamples</a>
        </body>
        </html>
        """
        return HttpResponse(response)
        