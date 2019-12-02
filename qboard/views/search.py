from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman,Intern
from django.core.paginator import Paginator
from django.db.models import Q



def list_search_view(request):
    var = request.GET
    search_str = var.get('search')
    # if RentRoom.objects.filter(pref_name=search_str).exists():
    #     searched_room_list = RentRoom.objects.filter(pref_name=search_str)
    #Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |
    # Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |  
    if Intern.objects.filter(Q(name__icontains=search_str) | Q(language__name__icontains=search_str) | Q(salary__icontains=search_str) | Q(score__icontains=search_str)).exists():
        searched_room_list = Intern.objects.filter(Q(name__icontains=search_str) | Q(language__name__icontains=search_str) | Q(salary__icontains=search_str) | Q(score__icontains=search_str))
        searched_room_list = list(set(searched_room_list))
        message = ""
    else:
        searched_room_list = []
        message = "検索結果はありません"
    # searched_room_list = RentRoom.objects.filter(Q(pref_name=search_str) | Q(city_name=search_str) | Q(str(built_year)=searcsearch_str))

    # searched_room_list = RentRoom.objects.filter

    paginator = Paginator(searched_room_list, 20) # ページ当たり20個表示
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    interns = paginator.get_page(page)
    return render(request, 'qboard/search_form.html', {'interns': interns, 'page': page, 'last_page': paginator.num_pages, 'message': message})

def form_view(request):
    intern_list = Intern.objects.all().order_by('-id')
    paginator = Paginator(intern_list, 20) 

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    interns = paginator.get_page(page)
    return render(request, 'qboard/search_form.html', {'interns':interns, 'page': page, 'last_page': paginator.num_pages})

def detail_view(request, intern_id):
    intern = get_object_or_404(Intern, id=intern_id) #見つからなかったら404を返す

    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1

    # try:
    #     log = ScoreLog.objects.get(profile_id=request.user.profile.id, rent_room_id=rentroom_id)
    #     current_score = log.score
    # except:
    #     current_score = -1
    
    return render(request, 'qboard/intern_detail.html', {'intern': intern, 'page': page})
    