from django.shortcuts import render
from core.models import posts,cat,Site,Socials
# Create your views here.
def search(request):
    pass
def detail_post(request,slug):
    data = posts.objects.get(slug=slug)
    catd = cat.objects.all()
    Sited = Site.objects.first()
    postss = posts.objects.order_by('-views')[:10]
    postsd = posts.objects.order_by('-views')[:3]
    Socialsd = Socials.objects.all()
    return render(request,'detail.html',{
        "cat":catd,
        "Site":Sited,
        "post":postsd,
        "data":data,
        "postss":postss,
        "social":Socialsd,
    })
def category(request,slug):
    pass