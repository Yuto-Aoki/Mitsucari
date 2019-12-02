from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman, Candidate,Intern
from django.core.paginator import Paginator
from qboard.forms import PredictForm



def form_view(request):
    form = PredictForm()
    return render(request, 'qboard/predict_form.html', {'form' : form})

# def form_view(request):
#     return render(request, 'qboard/predict_form.html')
def result_view(request):
    intern_list = Intern.objects.all().order_by('score')
    p_message = ''
    g_message = ''
    d_message = ''
    a_message = ''
    var = request.GET
    programming = float(var.get('programming', 0.5))
    if programming >= 5:
        programming = 5
    if programming <= 1:
        p_message = 'プログラミング歴が短いです。もっと経験を積みましょう！！'

    develop_num = int(var.get('develop_num', 1))
    if develop_num > 20:
        develop_num = 20
    if develop_num <= 2:
        d_message = '開発物が少ないですね...どんどん開発しましょう！！'

    gpa = float(var.get('gpa', 1))
    if gpa > 4:
        gpa = 4
    if gpa <= 2:
        g_message = 'GPAが少し低いです！！GPAを考慮する企業が増えてますよ！！'

    atcoder = var.get('atcoder')
    if atcoder != '' and atcoder != '0':
        atcoder = int(atcoder) // 100
        if atcoder < 500:
            a_message = 'このレートではプログラミングテストを乗り越えられません！！過去問を解きましょう！！'
        score = int(programming*10 + develop_num + gpa*2 + atcoder)
    else:
        a_message = ''
        score = int(programming*12 + develop_num + gpa*4)
    if score > 100:
        score = 100
    # pers = []
    # for i in intern_list['score']:
    #     per = score - i + 50
    #     if per > 100:
    #         per = 100
    #     pers.append(per)

    paginator = Paginator(intern_list, 20) 

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    interns = paginator.get_page(page)
    #return render(request, 'qboard/superman_list.html', {'supermans':supermans, 'page': page, 'last_page': paginator.num_pages})
    return render(request, 'qboard/predict_result.html', {'score':score,'interns':interns,'page': page, 'last_page': paginator.num_pages, 'p_message':p_message, 'd_message':d_message, 'g_message':g_message,'a_message':a_message})