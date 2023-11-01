from django.shortcuts import render
from core.models import posts,cat,Site,Socials
from django.shortcuts import get_object_or_404
# Create your views here.
def search(request):

    return render(request,"search.html",{})
def detail_post(request,slug):
    data = get_object_or_404(posts,slug=slug)
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
    data = get_object_or_404(cat,slug=slug)
    catd = cat.objects.all()
    Sited = Site.objects.first()
    allpost = posts.objects.all()
    postss = posts.objects.order_by('-views')[:10]
    Socialsd = Socials.objects.all()

    return render(request,"category.html",{
        "cat":catd,
        "Site":Sited,
        "post":allpost,
        "data":data,
        "postss":postss,
        "social":Socialsd,
        })