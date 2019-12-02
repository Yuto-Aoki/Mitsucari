from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
#from qboard.models import RentRoom, ScoreLog


@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    
    # mylogs = ScoreLog.objects.filter(profile_id=profile.id)
    # myrooms = RentRoom.objects.filter(owner_id=profile.id)

    return render(request, 'qboard/mypage.html', {'profile':profile})