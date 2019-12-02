from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman
from django.core.paginator import Paginator


def show_list(request):
    superman_list = Superman.objects.all().order_by('id')
    paginator = Paginator(superman_list, 20) 

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    supermans = paginator.get_page(page)
    return render(request, 'qboard/experience_list.html', {'supermans':supermans, 'page': page, 'last_page': paginator.num_pages})
