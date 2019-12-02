from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman, Candidate
from django.core.paginator import Paginator
from qboard.forms import CandidateForm
from django.db.models import Q



def list_search_view(request):
    var = request.GET
    search_str = var.get('search')
    # if RentRoom.objects.filter(pref_name=search_str).exists():
    #     searched_room_list = RentRoom.objects.filter(pref_name=search_str)
    #Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |
    # Q(name__icontains=search_str) | Q(intern_name__icontains=search_str) |  
    if Superman.objects.filter(Q(name__icontains=search_str) | Q(skill__name__icontains=search_str) | Q(twitter__icontains=search_str) | Q(intern_name__name__icontains=search_str)).exists():
        searched_room_list = Superman.objects.filter(Q(name__icontains=search_str) | Q(skill__name__icontains=search_str) | Q(twitter__icontains=search_str) | Q(intern_name__name__icontains=search_str))
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

    supermans = paginator.get_page(page)
    return render(request, 'qboard/superman_list.html', {'supermans': supermans, 'page': page, 'last_page': paginator.num_pages, 'message': message})

def superman_list(request):
    superman_list = Superman.objects.all().order_by('id')
    paginator = Paginator(superman_list, 20) 

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    supermans = paginator.get_page(page)
    return render(request, 'qboard/superman_list.html', {'supermans':supermans, 'page': page, 'last_page': paginator.num_pages})

def superman_form(request):
    form = CandidateForm()
    return render(request, 'qboard/superman_form.html', {'form' : form})

def superman_result(request):
    var = request.GET
    name = var.get('name', None) 
    intern_name = var.get('intern_name', None)
    skill_tag = var.get('skill_tag', None)  
    twitter = var.get('twitter', None)
    url = var.get('url', None)
    memo = var.get('memo', None)
    candidate = Candidate(name=name,intern_name=intern_name,skill_tag=skill_tag,twitter=twitter,url=url,memo=memo)
    candidate.save()
    if candidate is not None:
        return render(request, 'qboard/superman_result.html')
    
    