from django.shortcuts import render
from core.models import (cat,Site,posts,Socials)

from django.core.paginator import Paginator
from django.shortcuts import render




def home(request):
    catd = cat.objects.all()
    Sited = Site.objects.first()
    postsd = posts.objects.order_by('-views')[:3]
    postss = posts.objects.order_by('-views')[:10]
    allposts = posts.objects.all()
    Socialsd = Socials.objects.all()
    # ================================================================
    post_list = posts.objects.all()
    paginator = Paginator(post_list, 3)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    # ================================================================
    return render(request,"index.html",{
        "cat":catd,
        "Site":Sited,
        "post":postsd,
        "postss":postss,
        "social":Socialsd,
        "allp":allposts,
        "page_obj": page_obj
    })