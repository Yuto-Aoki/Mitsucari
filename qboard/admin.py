from django.contrib import admin 

# モデルをインポート 
from .models import Language, Profile, InternName, Superman, Skill, Candidate,Intern

# 管理サイトへのモデルの登録 
admin.site.register(Profile)
admin.site.register(Language)
admin.site.register(InternName)
admin.site.register(Superman)
admin.site.register(Skill)
admin.site.register(Candidate)
admin.site.register(Intern)