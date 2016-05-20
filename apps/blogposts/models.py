from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Controls blog post storage

class Articles(models.Model):
	blog_author = models.TextField()
	blog_article = models.TextField()
	blog_date = models.DateField()
	blog_image = models.TextField()
	blog_headline = models.TextField()
	class Meta: 
		db_table = "Articles"