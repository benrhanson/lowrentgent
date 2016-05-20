from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	# shows the index page
	url(r'^$', views.index, name = "index"),
	# takes you to page where we can add articles
	url(r'^page_add/', views.page_add, name = "page_add"), 
	# adds articles to the database
	url(r'^add/', views.add, name = "add"),
	# actually searches the database
	url(r'^query/', views.query, name = "query"),
	# page for searching through the database for articles
	url(r'^search/', views.searchpage, name = "search"),
	# page for displaying an article
	url(r'^article/(?P<article_id>\d+)/$', views.article, name = "article")
]