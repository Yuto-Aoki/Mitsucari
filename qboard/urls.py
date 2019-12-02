from django.urls import path
from . import views
from qboard.views import mypage, recommend, experience, search, superman,candidate,predict


app_name = 'qboard'

urlpatterns = [ 
    #path('hello/', views.hello, name='hello'), 
    path('mypage', mypage.mypage_top, name='mypage_top'),
    path('recommend', recommend.form_view, name='recommend_form'),
    path('recommend/result', recommend.result_view, name='recommend_result'),
    path('experience', experience.show_list, name='experience_top'),
    path('search', search.form_view, name='search_form'),
    path('search/<slug:intern_id>', search.detail_view, name='intern_detail'),
    path('search/search',search.list_search_view, name='intern_search_list'),
    path('superman_list', superman.superman_list, name='superman_list'),
    path('superman_list/search',superman.list_search_view, name='superman_search_list'),
    path('recommend/search',recommend.list_search_view, name='recommend_search_list'),
    path('superman_form', candidate.superman_form, name='superman_form'),
    path('superman_form/result', candidate.superman_result, name='superman_result'),
    path('predict', predict.form_view, name='predict_form'),
    path('predict/result', predict.result_view, name='predict_result'),
]