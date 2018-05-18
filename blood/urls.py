from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
admin.autodiscover()
from.import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'obc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^base', views.base, name='base'),
    url(r'^tipsondonating', views.tipsondonating, name='tipsondonating'),
    # url(r'^slider', views.slider, name='slider'),
    url(r'^whocanorcantdonateblood', views.whocanorcantdonateblood, name='whocanorcantdonateblood'),
    url(r'^bloodimportance', views.bloodimportance, name='bloodimportance'),
    url(r'^mostneededblood', views.mostneededblood, name='mostneededblood'),
    url(r'^blooddonationfacts', views.blooddonationfacts, name='blooddonationfacts'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^whydonateblood', views.whydonateblood, name='whydonateblood'),
    url(r'^whoneedsblood', views.whoneedsblood, name='whoneedsblood'),
    url(r'^bloodchain', views.bloodchain, name='bloodchain'),
    url(r'^privacypolicy', views.privacypolicy, name='privacypolicy'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^inspiringstories/', views.stories, name='inspiringstories'),
    url(r'^about', views.about, name='about'),
    url(r'^signin/', views.signin, name='signin'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^footer', views.footer, name='footer'),
    url(r'^termsofuse', views.termsofuse, name='termsofuse'),
    url(r'^faq', views.faq, name='faq'),
    url(r'^userlogin/', views.userlogin, name='userlogin'),
    # url(r'^list_i/', views.list_i, name='list_i'),
    url(r'^search/', views.search, name='search'),
    url(r'^views/', views.contact_view, name='views'),
    # url(r'^logout/', views.logout, name='logout'),


    # url(r'^login/$', login, {'template_name' : 'login.html'}),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page':'index'}, name='logout'),
    # url(r'^profile/$', views.profile, name='profile'),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    # url(r'^profile/password/$', views.change_password, name='change_password'),
    
    
    # url(r'$', views.PersonListView.as_view(), name='person_changelist'),
    # url(r'^add/', views.PersonCreateView.as_view(), name='person_add'),
    # url(r'^<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),

    # url(r'^ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here
]



# from django.urls import include, path
# from . import views

# urlpatterns = [
#     path('', views.PersonListView.as_view(), name='person_changelist'),
#     path('add/', views.PersonCreateView.as_view(), name='person_add'),
#     path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),

#     path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here
# ]