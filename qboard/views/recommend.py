from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman
from django.core.paginator import Paginator
from django.db.models import Q
# from iekari.scripts.recommend.new_user import RecommendNew

def list_search_view(request):
    var = request.GET
    search_str = var.get('search')
    # if RentRoom.objects.filter(pref_name=search_str).exists():
    #     searched_room_list = RentRoom.objects.filter(pref_name=search_str)
    #Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |
    # Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |  
    if Superman.objects.filter(Q(name__icontains=search_str) | Q(skill__name__icontains=search_str) | Q(twitter__icontains=search_str)).exists():
        searched_room_list = Superman.objects.filter(Q(name__icontains=search_str) | Q(skill__name__icontains=search_str) | Q(twitter__icontains=search_str))
        message = ""
    else:
        searched_room_list = []
        message = "検索結果はありません"
    # searched_room_list = RentRoom.objects.filter(Q(pref_name=search_str) | Q(city_name=search_str) | Q(str(built_year)=searcsearch_str))

    # searched_room_list = RentRoom.objects.filter

    paginator = Paginator(searched_room_list, 10) # ページ当たり20個表示
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    supermans = paginator.get_page(page)
    return render(request, 'qboard/recommend_form.html', {'supermans': supermans, 'page': page, 'last_page': paginator.num_pages, 'message': message})

def form_view(request): # フォームを表示
    superman_list = Superman.objects.all().order_by('-id')
    paginator = Paginator(superman_list, 20) # ページ当たり20個表示

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    supermans = paginator.get_page(page)
    return render(request, 'qboard/recommend_form.html', {'supermans':supermans, 'page': page, 'last_page': paginator.num_pages})

def result_view(request): # フォームの入力をAPIに伝達、リターン値を用いてテンプレートに表示
    var = request.GET
    #intern = var.get
    checks = request.POST.getlist('checks[]')
    lists = []
    dic = {}
    for id in checks:
        intern = Superman.objects.get(id=id)
        intern_name = intern.intern_name.all()
        for item in intern_name:
            dic.setdefault(item, 0)
            dic[item] +=1
    
    results = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    if len(results) > 0:
        return render(request, 'qboard/recommend_result.html', {'results':results})
    else:
        return render(request, 'qboard/recommend_error.html')