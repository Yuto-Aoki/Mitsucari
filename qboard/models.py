from django.contrib.auth.models import User 
from django.db import models 
 
GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = {0:'男性',1:'女性'}

DEGREE_LIST = ( (0, '学士(取得予定)'), (1, '学士'), (2, '修士'), (3, '博士'), (4, '短期大学士'), (5, '専門士'), (6, '高度専門士'))
dict_degree_list = dict(DEGREE_LIST)
#デフォルトであるdjango.dbのmodelsを継承して作成する
class Profile(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    class Meta:
        verbose_name = 'ユーザー情報データ'
        verbose_name_plural = 'ユーザー情報データ'
    #ユーザーの設定。下記のフィールドとの紐づけはビューで行う
    user = models.OneToOneField(User, verbose_name='ユーザー',null=True, blank=True, on_delete=models.CASCADE)

    #フィールドの設定。コード１行がフィールド１列に対応する。
    id = models.CharField(max_length=6,primary_key=True)
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)
    univercity = models.CharField('大学名', max_length=20, default='大学')
    faculty = models.CharField('学部', max_length=20,default='学部')
    department = models.CharField('学科', max_length=20,default='学科')
    degree = models.IntegerField('学位', choices=DEGREE_LIST, default=0)
    grade = models.IntegerField('学年',default=3)
    #graduate_date = models.DateField('卒業(予定)年月',default=201903)
    #graduate_month = models.IntegerField('卒業(予定)月')
    highschool = models.CharField('高校名',max_length=20, blank=True,default='高校')
    email_address = models.EmailField('メールアドレス',max_length=255, unique=True,default='gmail')
    memo = models.TextField('備考欄',null=True,default='なし')
    twitter = models.TextField('Twitter', blank=True)

    
    
    #管理画面で表示される文字列を定義する
    def __str__(self):
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'

        return self.id+' '+str(self.univercity)+' ' \
            +str(self.faculty) + ' ' + str(self.department)+ ' ' \
            +dict_degree_list.get(self.degree) + ' ' + str(self.grade) + '年生 ' \
            +dict_gender_list.get(self.gender)+' ' \
            # +str(self.graduate_year)+'年卒 ' \

class Language(models.Model):
    class Meta:
        verbose_name = '言語情報データ'
        verbose_name_plural = '言語情報データ'
    
    language = models.CharField('プログラミング言語', max_length=20)
    
    def __str__(self):
        return str(self.language)

class InternName(models.Model):
    class Meta:
        verbose_name = 'インターン名前情報データ'
        verbose_name_plural = 'インターン名前情報データ'
    name = models.CharField('インターン名', max_length=20)

    def __str__(self):
        return str(self.name)

class Intern(models.Model):
    class Meta:
        verbose_name = 'インターン情報データ'
        verbose_name_plural = 'インターン情報データ'
    
    
    name = models.CharField('インターン名', max_length=20)
    language = models.ForeignKey(Language, verbose_name='プログラミング言語', on_delete=models.CASCADE)
    work = models.TextField('内容')
    score = models.IntegerField('最低限スコア')
    salary = models.IntegerField('給料')
    url = models.URLField('url')

    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        verbose_name = 'スキルタグ情報データ'
        verbose_name_plural = 'スキルタグ情報データ'
    
    name = models.CharField('スキルタグ名',max_length=20)

    def __str__(self):
        return str(self.name)

class Superman(models.Model):
    class Meta:
        verbose_name = 'すごい人情報データ'
        verbose_name_plural = 'すごい人情報データ'

    id = models.CharField(max_length=6,primary_key=True)
    name = models.CharField('名前',max_length=20)
    intern_name= models.ManyToManyField(InternName,verbose_name='インターン名', blank=True)
    skill = models.ForeignKey(Skill,verbose_name='系統',null=True, blank=True,on_delete=models.CASCADE)
    twitter_name = models.CharField('ホームページ用',max_length=20,null=True)
    twitter = models.CharField('Twitterアカウント', max_length=20)
    url = models.URLField('インターン体験記url',blank=True,null=True)
    github = models.URLField('開発物url',blank=True,null=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.twitter)+' '+str(self.skill)+'系'

class Candidate(models.Model):
    class Meta:
        verbose_name = 'すごい人候補情報データ'
        verbose_name_plural = 'すごい人候補情報データ'
    
    name = models.CharField('名前',max_length=20)
    intern_name= models.ForeignKey(InternName,verbose_name='インターン名', blank=True,on_delete=models.CASCADE,null=True)
    skill_tag = models.ForeignKey(Skill,verbose_name='系統', null=True,blank=True,on_delete=models.CASCADE)
    twitter_name = models.CharField('ホームページ用',max_length=20,null=True)
    twitter = models.CharField('Twitterアカウント', max_length=20)
    url = models.URLField('インターン体験記url',blank=True,null=True)
    github = models.URLField('開発物url',blank=True,null=True)
    memo = models.TextField('理由、備考欄')

    def __str__(self):
        return str(self.name) + ' ' + str(self.twitter)+' '+str(self.skill_tag)+'系'

class Predict(models.Model):
    class Meta:
        verbose_name = '予測データ'
        verbose_name_plural = '予測データ'
    
    language = models.ForeignKey(Language, verbose_name='言語',blank=True, on_delete=models.CASCADE)
    programming = models.IntegerField('プログラミング歴',blank=True)
    develop_num = models.IntegerField('開発物数',blank=True)
    gpa = models.IntegerField('GPA',blank=True)
    atcoder = models.IntegerField('Atcoderレート',blank = True)
    score = models.IntegerField('スコア',blank = True)

    def __str__(self):
        return str(self.score)

    