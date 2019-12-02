from django.forms import Form, ModelForm, HiddenInput, TextInput, NumberInput, RadioSelect, Textarea
from qboard.models import Superman, Candidate, Predict, Skill,InternName
from django import forms



class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields  = [
            'name', 'intern_name', 'skill_tag', 'twitter', 'url','github', 'memo'
        ]
        labels = {
            'name' : '名前(Twitter名)',
            'intern_name' : '参加経験のあるインターン(複数選択可)',
            'skill_tag' : 'その方は何系のエンジニアですか？(１つ選んでください)',
            'twitter' : '例  ＠sample',
            'url' : 'インターン体験記',
            'github' : 'Githubページ',
            'memo' : '備考欄、理由'

        }
    skill = Skill.objects.all()
    Candidate.skill_tag = skill
    intern_name = InternName.objects.all()
    Candidate.intern_name = intern_name
    name = forms.CharField(required=True,label='名前')
    intern_name = forms.ModelChoiceField(queryset=InternName.objects.all(),
                                                required=True,label='参加経験のあるインターン(1つ選んでください)',
                                                to_field_name='name',
                                                )
    skill_tag = forms.ModelChoiceField(queryset=Skill.objects.all(),
                                        required=True,label='その方は何系のエンジニアですか？(１つ選んでください)',
                                        empty_label='選択してください',
                                        )
    twitter = forms.CharField(required=True,label='Twitterアカウント')
    url = forms.URLField(required=False,label='その方のインターン体験記があればurlを記載ください')
    github = forms.URLField(required=False,label='Githubページまたは開発物があればurlを記載ください')
    memo = forms.CharField(required=True,widget=Textarea,label='備考欄、理由をお書きください')

    

class PredictForm(ModelForm):
    class Meta:
        model = Predict
        
        fields = [
            'programming','develop_num','gpa','atcoder'
        ]
        labels = {
            'programming' : '例　1.5',
            'develop_num' : '例　3',
            'gpa': '例　3.2',
            'atcoder':'例　1330',
            
        }
    
    programming = forms.FloatField(required=True,label='プログラミング歴(年)')
    develop_num = forms.IntegerField(required=True,label='開発物、プロジェクト数')
    gpa = forms.FloatField(required=True,label='GPA')
    atcoder = forms.IntegerField(required=False,label='Atcoderのレート(なくても大丈夫です)')
# class RentRoomAssessmentForm(ModelForm):
#     class Meta:
#         model = RentRoomAssessment
#         fields = [
#             'pref_name','city_name','district_name','house_no',
#             'built_year','structure','top_floor_num',
#             'room_type','area','nearest_station','dist_to_nearest_station'
            
#             # 自動決定
#             #'latitude', 'longitude', 
#             # price
#         ]
#         labels = {
#             'pref_name': '都道府県',
#             'city_name': '市区町村',
#             'district_name': '町丁目',
#             'house_no': '番地・号(xx-yy)',
#             'built_year': '築年',
#             'structure': '構造',
#             'top_floor_num': 'マンション最上階数',
#             'room_type': '間取り',
#             'area': '専有面積',
#             'nearest_station':'最寄駅',
#             'dist_to_nearest_station':'最寄駅までの距離(m)'
#         }