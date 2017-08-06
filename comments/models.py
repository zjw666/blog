# -*- coding: utf-8 -*-
from django.db import models

class Comment(models.Model):
	name=models.CharField("名字",max_length=100)
	email=models.EmailField("邮箱",max_length=100)
	url=models.URLField(blank=True)
	text=models.TextField()
	created_time=models.DateTimeField(auto_now_add=True)
	post=models.ForeignKey('blog.Post')
	
	def __str__(self):
		return '评论人：'+self.name+'\n评论内容：'+self.text[:20]
	
