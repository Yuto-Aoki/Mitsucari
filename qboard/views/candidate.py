from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from qboard.models import Superman, Candidate,InternName,Skill
from django.core.paginator import Paginator
from qboard.forms import CandidateForm
from django import forms
from django.core.exceptions import ObjectDoesNotExist


def superman_form(request):
    form = CandidateForm()
    return render(request, 'qboard/superman_form.html', {'form' : form})

def superman_result(request):
    try:
        max_id = Superman.objects.latest('id').id
    except ObjectDoesNotExist:
        max_id = 'S00000'
   

    candidate_id = 'S'+(str(int(max_id[1:])+1).zfill(5))

    var = request.GET
    name = var.get('name', None) 
    
    intern_id = var.get('intern_name', None)
    intern_name = InternName.objects.get(name=intern_id)
    # form.fields['tag'].queryset = Tag.objects
    #intern_name = form.cleaned_data['intern_name']

    skill_id = var.get('skill_tag', None)
    skill_tag = Skill.objects.get(id=skill_id)

    twitter = var.get('twitter', None)
    twitter_name = twitter[1:]
    url = var.get('url', None)
    github = var.get('github', None)
    memo = var.get('memo', None)
    candidate = Superman(id=candidate_id,name=name, skill=skill_tag,twitter_name=twitter_name,twitter=twitter,url=url,github=github)
    candidate.save()
    candidate.intern_name.add(intern_name)
    #candidate.intern_name.set(intern_name)
    count = Candidate.objects.filter(twitter=twitter).count()
    
    # try:
    #         max_id = Profile.objects.latest('id').id
    #     except ObjectDoesNotExist:
    #         max_id = 'B00000'

    #     prof_id = 'B'+(str(int(max_id[1:])+1).zfill(5))
    
    return render(request, 'qboard/superman_result.html')
#     person1 = Person.objects.get(id=1)
# >>> person1.hobbys.all()
# lass Candidate(models.Model):
#     class Meta:
#         verbose_name = 'すごい人候補情報データ'
#         verbose_name_plural = 'すごい人候補情報データ'
    
#     name = models.CharField('名前',max_length=20)
#     intern_name= models.ForeignKey(InternName,verbose_name='インターン名', blank=True,on_delete=models.CASCADE,null=True)
#     skill_tag = models.ForeignKey(Skill,verbose_name='系統', null=True,blank=True,on_delete=models.CASCADE)
#     twitter_name = models.CharField('ホームページ用',max_length=20,null=True)
#     twitter = models.CharField('Twitterアカウント', max_length=20)
#     url = models.URLField('インターン体験記url',blank=True,null=True)
#     github = models.URLField('開発物url',blank=True,null=True)
#     memo = models.TextField('理由、備考欄')

    