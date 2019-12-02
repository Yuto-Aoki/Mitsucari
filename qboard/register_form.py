from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from qboard.models import GENDER_LIST, Profile, DEGREE_LIST

class RegisterForm(UserCreationForm):
    age = forms.IntegerField(required=True, label='年齢')
    gender = forms.ChoiceField(choices=GENDER_LIST, required=True,label='性別')
    univercity = forms.CharField(required=True,label='大学名　　例　○○大学')
    faculty = forms.CharField(required=True, label='学部')
    department = forms.CharField(required=True,label='学科')
    degree = forms.ChoiceField(choices=DEGREE_LIST, required=True, label='学位')
    grade = forms.IntegerField(required=False,label='学年')
    #graduate_date = forms.DateTimeField(label='卒業(予定)年月　　例　2021/03',required=True, input_formats=['%Y/%m'])
    #graduate_month = forms.IntegerField(required=True)
    highschool = forms.CharField(required=False,label='高校名')
    email_address = forms.EmailField(required=True,label='メールアドレス')
    memo = forms.CharField(required=False,label='備考欄')
    

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','age','gender','univercity', 'faculty', 'department', 'degree', 'grade', 'highschool','email_address','memo']
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード確認',
            'age': '年齢',
            'gender': '性別',
            'univercity': '大学名',
            'faculty': '学部',
            'department': '学科',
            'degree': '学位',
            'grade': '学年',
            'highschool': '高校名',
            'email_address': 'メールアドレス',
            'memo': '備考欄'
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError('Cannot create User and Profile without database save')
        
        user = super().save()

        try:
            max_id = Profile.objects.latest('id').id
        except ObjectDoesNotExist:
            max_id = 'B00000'

        prof_id = 'B'+(str(int(max_id[1:])+1).zfill(5))

        age = self.cleaned_data['age']
        gender = self.cleaned_data['gender']
        univercity = self.cleaned_data['univercity']
        faculty = self.cleaned_data['faculty']
        department = self.cleaned_data['department']
        degree = self.cleaned_data['degree']
        grade = self.cleaned_data['grade']
        #graduate_date = self.cleaned_data['graduate_date']
        #graduate_month = self.cleaned_data['graduate_month']
        highschool = self.cleaned_data['highschool']
        email_address = self.cleaned_data['email_address']
        memo = self.cleaned_data['memo']

        profile = Profile(id=prof_id,age=age,gender=gender,univercity=univercity,faculty=faculty,department=department,degree=degree,grade=grade,highschool=highschool,email_address=email_address,memo=memo ,user_id=user.id)
        profile.save()

        return user