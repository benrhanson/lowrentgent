from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
import datetime
from django.template import RequestContext
from .forms import AddForm, Query
from .models import Articles

# Create your views here.
def index(request):
	carousel_results = Articles.objects.order_by('-blog_date')[0:3].all()
	carousel_package = []
	for i in carousel_results: 
		if isinstance(i.blog_date, datetime.date):
			date = i.blog_date.strftime('%D')
		carousel_package.append(({'blog_author': i.blog_author, 'id': i.id, 'blog_date': date, 'blog_id': i.id, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
	request.session['carousel'] = carousel_package
	return render(request, 'blogposts/index.html')
# page for adding articles
def page_add(request):
	form_class = AddForm
	return render(request, 'blogposts/add.html', {'form':form_class})

# adds the article to the database or returns an error
def add(request):
	if request.method == "POST":
		article = AddForm(request.POST)
		if article.is_valid():
			add_article = article.save()
			print "success!"
		else: 
			print "near miss"
	else:
		print "complete miss"
	return redirect(page_add)

def searchpage(request):
	form_class = Query
	try:
		request.session['results']
	except:
		request.session['results'] = "Your results will show up here!"
	results = request.session['results']
	return render(request, 'blogposts/search.html', {'form':form_class})

def query(request):
	if request.method == "POST":
		# searches when query has a date but no author
		if not request.POST['blog_author'] and request.POST['blog_date']:
			results = Articles.objects.filter(blog_date = request.POST['blog_date'])
		# searches when query has an author but no date
		elif not request.POST['blog_date'] and request.POST['blog_author']:
			results = Articles.objects.filter(blog_author = request.POST['blog_author'])
		# date and author
		else: 
			results = Articles.objects.filter(blog_author = request.POST['blog_author'], blog_date = request.POST['blog_date'])
		result_package = []
		for i in results:
			if isinstance(i.blog_date, datetime.date):
				date = i.blog_date.strftime('%D')
				print date
			result_package.append(['blog_author', i.blog_author, 'blog_date', date, 'blog_article', i.blog_article])
		request.session['results'] = result_package
	else:
		print "oopsie"
	return redirect(searchpage)

def article(request, article_id):
	article = Articles.objects.filter(id = article_id)
	article_package = []
	for i in article: 
		if isinstance(i.blog_date, datetime.date):
			date = i.blog_date.strftime('%D')
		article_package.append(({'blog_author': i.blog_author, 'blog_article': i.blog_article, 'id': i.id, 'blog_date': date, 'blog_id': i.id, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
	request.session['article'] = article_package
	return render(request, 'blogposts/article.html')