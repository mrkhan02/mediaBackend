from dataclasses import field
from rest_framework import serializers
from API.models import Article,Newsletter,Gallery,Comments, Spotlight,Videos

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Article
        fields =('sno','thumbnail','title','author','profile','date','content','summary','isActive','tag')


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Newsletter
        fields=('sno','name','email')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields=('sno','image','click','event')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=('sno','article','name','email','profile','message')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Videos
        fields=('sno','link')

class SpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spotlight
        fields=('sno','url','title','summary')



