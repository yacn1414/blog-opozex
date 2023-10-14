from django.shortcuts import render
from core.models import (cat,Site,posts,Socials)
# Create your views here.
def home(request):
    catd = cat.objects.all()
    Sited = Site.objects.all()
    postsd = posts.objects.order_by('-views')[:3]
    allposts = posts.objects.all()
    Socialsd = Socials.objects.all()

    return render(request,"index.html",{
        "cat":catd,
        "Site":Sited,
        "post":postsd,
        "social":Socialsd,
        "allp":allposts,
    })