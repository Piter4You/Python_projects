from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
from shortUrl.models import Urls
from shortUrl.functions import generate_link

class Main(View):
    def get(self,request):
        link = generate_link.generate()
        return render(request, "index.html")
    
    def post(self, request):
        link = request.POST.get("longUrl")
        newUrl = Urls()
        newUrl.link = link
        newUrl.shortlink = generate_link.generate()
        allShortLinks = Urls.objects.all()
        temp = False
        while temp == False:
            temp = True
            for elements in allShortLinks:
                if elements.shortlink == newUrl.shortlink:
                    newUrl.shortlink = generate_link()
                    temp = False
        newUrl.save()
        newLink = "http://127.0.0.1:8000/" + newUrl.shortlink
        return render(request, "link.html", context={'newLink' : newLink })

                
def ReddirectFromShortUrl(request, shortUrl):
    longUrl = Urls.objects.get(shortlink = shortUrl).link
    return redirect(longUrl)
        

# Create your views here.
