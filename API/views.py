from crypt import methods
#from tkinter import NE
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib3 import HTTPResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from .models import Article,Newsletter,Gallery,Comments,Videos,Spotlight
from .serializers import ArticleSerializer,NewsletterSerializer,GallerySerializer,CommentsSerializer,VideoSerializer,SpotlightSerializer
from .mypagination import MyPageNumberPagination, MyPageNumberPaginationPinned
from rest_framework.generics import ListAPIView
from django.conf import settings
from math import ceil
# Create your views here.

#API to get Article

class ArticleList(ListAPIView):
    queryset=Article.objects.filter(isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class InstiLifeList(ListAPIView):
    queryset=Article.objects.filter(tag='Insti Life',isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class AcademicsList(ListAPIView):
    queryset=Article.objects.filter(tag='Academics',isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class SciTechList(ListAPIView):
    queryset=Article.objects.filter(tag='Sci-Tech',isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class OpinionList(ListAPIView):
    queryset=Article.objects.filter(tag='Opinion',isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class SpotLightList(ListAPIView):
    queryset=Article.objects.filter(tag='Spotlight',isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPagination

class WatchList(ListAPIView):
    queryset=Spotlight.objects.all().order_by('-sno')
    serializer_class=SpotlightSerializer
    pagination_class=MyPageNumberPagination

class PinnedList(ListAPIView):
    queryset=Article.objects.filter(isPinned=True,isActive=True).order_by('-date','-sno')
    serializer_class=ArticleSerializer
    pagination_class=MyPageNumberPaginationPinned

@csrf_exempt
def getPageCount(request):
    if request.method == 'GET':
        articlePerPage=MyPageNumberPagination.page_size
        pageCount=Article.objects.filter(isActive=True).count()
        pageCount=ceil(pageCount/articlePerPage)
        return JsonResponse({'pageCount': pageCount, 'articlePerPage': articlePerPage},safe=False)
    else:
        return JsonResponse("Bad Request.",safe=False)


@csrf_exempt
def articleAPI(request,pk=-1):
    if request.method=='GET':
        if(pk==-1):
            articles=Article.objects.filter(isActive=True)

            article_serializer=ArticleSerializer(articles,many=True)
            return JsonResponse(article_serializer.data,safe=False) 

        else:
            try:
                articles=Article.objects.get(slug=pk,isActive=True)
            except Article.DoesNotExist:
                result={'sno':-1}
                return JsonResponse(result,safe=False)

            s=articles.content
            k=''
            for i in range(len(s)):
                if(i+6<len(s)):
                    if(s[i:i+6]=='media/'):
                        k+=settings.HOST_URL
                        k+=s[i]
                    else:
                        k+=s[i]
                else:
                    k+=s[i]
            articles.content=k
            articles.postViews=articles.postViews+1
            
            article_serializer=ArticleSerializer(articles)
            
            return JsonResponse(article_serializer.data,safe=False) 
    else:
        return JsonResponse("Bad Request.",safe=False)



def pinnedArticle(request):
    if request.method=='GET':
        articles=Article.objects.filter(isPinned=True)
        article_serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(article_serializer.data,safe=False) 
        
    else:
        return JsonResponse("Bad Request.",safe=False)


#API for comment
@csrf_exempt
def commentAPI(request,pk=-1):
    if request.method=='GET':
        if(pk==-1):
            return JsonResponse("Bad Request.",safe=False)

        else:
            comments=Comments.objects.filter(article=pk).order_by('-sno')
          
            comment_serializer=CommentsSerializer(comments,many=True)
            return JsonResponse(comment_serializer.data,safe=False)
    elif request.method== 'POST':
        comment_data=JSONParser().parse(request)
        print(comment_data)
        comment_serializer = CommentsSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    else:
        return JsonResponse("Bad Request.",safe=False)

#API for Gallery   
@csrf_exempt
def galleryAPI(request):
    if request.method=='GET':
        images=Gallery.objects.all()
        image_serializer=GallerySerializer(images,many=True)
        return JsonResponse(image_serializer,safe=False)

    else:
        return JsonResponse("Bad Request.",safe=False)



#API for Newsletter
@csrf_exempt

def newsletterAPI(request):
    if request.method=='POST':
        newsletter_data=JSONParser().parse(request)
        email=newsletter_data['email']
        name=newsletter_data['name']
        try:
            newsletter=Newsletter.objects.get(email=email)
        except Newsletter.DoesNotExist:
            newsletter_serializer=NewsletterSerializer(data=newsletter_data)
            if newsletter_serializer.is_valid():
                return JsonResponse("Added Successfully!!" , safe=False)
            return JsonResponse("Failed to Add.",safe=False)
        return JsonResponse('Aready Added',safe=False)
    else:
        return JsonResponse("Bad Request.",safe=False)


#API for Videos
@csrf_exempt
def getVideos(request):
    if request.method=='GET':
        videos=Videos.objects.all()
       
        video_serializer=CommentsSerializer(videos,many=True)
        return JsonResponse(video_serializer.data,safe=False)
    else:
        return JsonResponse('Bad Request',safe=False)




#API for Search
@csrf_exempt
def search(request,query=""):
    if request.method=='GET':
        if (len(query)>78 or len(query)<=0):
            articles=Article.objects.none()
        else:
            allPostsTitle= Article.objects.filter(title__icontains=query)
            allPostsAuthor= Article.objects.filter(author__icontains=query)
            allPostsContent =Article.objects.filter(content__icontains=query)
            articles=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        article_serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(article_serializer.data,safe=False)
    else:
        return JsonResponse('Bad Request',safe=False)

@csrf_exempt
def Home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else :
        return render(request,'error.html')

@csrf_exempt
def newsletterpage(request):
    if request.user.is_authenticated:
        return render(request,'newsletter.html')
    else :
        return render(request,'error.html')

@csrf_exempt
def sendNewsletter(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else :
        return render(request,'error.html')