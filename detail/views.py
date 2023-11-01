from django.shortcuts import render
from core.models import posts,cat,Site,Socials
from django.shortcuts import get_object_or_404
# Create your views here.
def search(request):
    search1 = posts.objects.filter(title__contains=request.POST['search'])
    search2 = posts.objects.filter(caption__contains=request.POST['search'])
    search3 = posts.objects.filter(slug__contains=request.POST['search'])
    return render(request,"search.html",{"search":search1,"search2":search2,"search3":search3})
def detail_post(request,slug):
    data = get_object_or_404(posts,slug=slug)
    ip_address = request.user.ip_address
    if ip_address not in data.views.all():
        data.views.add(ip_address)
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
    allpost = posts.objects.filter(categories=data)
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