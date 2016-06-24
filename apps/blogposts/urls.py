from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	# shows the index page
	url(r'^$', views.index, name = "index"),
	# displays all articles
	url(r'^all/', views.all, name = "all"),
	# displays about articles
	url(r'^about/', views.about, name = "about"),
	# actually searches the database
	url(r'^query/', views.query, name = "query"),
	# page for searching through the database for articles
	url(r'^search/', views.searchpage, name = "search"),
	# page for displaying an article
	url(r'^article/(?P<article_id>\d+)/$', views.article, name = "article")
]