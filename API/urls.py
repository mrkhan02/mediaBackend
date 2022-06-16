"""mediaBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static  
from . import views
urlpatterns = [
    path('article/',views.ArticleList.as_view()),
    path('article/instilife',views.InstiLifeList.as_view()),
    path('article/academics',views.AcademicsList.as_view()),
    path('article/scitech',views.SciTechList.as_view()),
    path('article/opinion',views.OpinionList.as_view()),
    path('article/spotlight',views.SpotLightList.as_view()),
    path('spotlight/',views.WatchList.as_view()),
    path('article/<str:pk>/',views.articleAPI,name='articleAPI'),
    path('pinnned/',views.PinnedList.as_view()),
    path('pinned/',views.pinnedArticle,name='pinnedArticle'),
    path('comment/<int:pk>/',views.commentAPI,name='commentAPI'),
    path('comment/',views.commentAPI,name='commentAPI'),
    path('videos/',views.getVideos,name='getVideos'),
    path('gallery/',views.galleryAPI,name='galleryAPI'),
    path('newsletter/',views.newsletterAPI,name='newsletterAPI'),
    path('search/<str:query>/',views.search,name='search'),
    path('search//',views.search,name='search'),
    path('search/',views.search,name='search'),
    path('',views.Home,name='Home'),
    path('newsletterpage/',views.newsletterpage,name='newsletterpage'),
      
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
