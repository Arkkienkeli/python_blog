#coding=utf-8
import re

from django.db import models
from django.contrib import admin
from transliterate import translit

class PostCategory(models.Model):
	class Meta:
		verbose_name = 'Категория поста'
		verbose_name_plural = 'Категории постов'
	title = models.CharField(u'Название категории', max_length=200)
	def __unicode__(self):
		return self.title

class Post(models.Model):
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
	author = models.ForeignKey('auth.User')
	title = models.CharField(u'Заголовок поста', max_length=250)
	category = models.ForeignKey('PostCategory')
	text = models.TextField(u'Текст поста')
	visible = models.BooleanField(default=False)

	def translite_title(self):
		b = self.title
		b = b.strip().lower()
		trans = translit(b, "ru", reversed=True)

		re_com = re.compile(r'[^a-z0-9\s]', re.U)
		re_spaces = re.compile(r'\s+', re.U)
		re_dashes = re.compile(r'-{2,}', re.U)
		
		trans = re_com.sub('', trans)
		trans = re_spaces.sub('-', trans)
		trans = re_dashes.sub('-', trans)
		
		return trans

	def __unicode__(self):
		return self.title

admin.site.register(PostCategory)
admin.site.register(Post)