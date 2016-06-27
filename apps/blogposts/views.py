from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
import datetime
from django.template import RequestContext
from .forms import AddForm, Query
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	# pops session results for searches so old searches aren't in the session the next time someone goes back to the search page
	request.session.pop('results')
	# populates the carousel with the most recent three article links and images
	carousel_articles = Articles.objects.order_by('-blog_date')[0:3].all()
	# variable to store articles for carousel
	carousel_package = []
	for i in carousel_articles: 
		if isinstance(i.blog_date, datetime.date):
		# makes the date into a nicer form- may not be necessary since dates are not displayed
			date = i.blog_date.strftime('%D')
		carousel_package.append(({'blog_author': i.blog_author, 'id': i.id, 'blog_date': date, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
	request.session['carousel'] = carousel_package
	# populates the right side with the next 4 articles
	non_carousel_articles = Articles.objects.order_by('-blog_date')[3:10].all()
	non_carousel_package  = []
	for i in non_carousel_articles: 
		# makes the date into a nicer form - may not be necessary since dates are not displayed
		if isinstance(i.blog_date, datetime.date):
			date = i.blog_date.strftime('%D')
		non_carousel_package.append(({'blog_author': i.blog_author, 'id': i.id, 'blog_date': date, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))	 
	request.session['non_carousel'] = non_carousel_package
	return render(request, 'blogposts/index.html')

# Page for searching database

def searchpage(request):
	form_class = Query
	try:
		request.session['results']
	except:
		request.session['results'] = ["Your results will show up here."]
	results = request.session['results']
	return render(request, 'blogposts/search.html', {'form':form_class})

# handles search queries by author and by date

def query(request):
	if request.method == "POST":
		print "got hit"
		# searches when query has a date but no author
		if not request.POST['blog_author'] and request.POST['blog_date']:
			results = Articles.objects.filter(blog_date = request.POST['blog_date'])
		# searches when query has an author but no date
		elif not request.POST['blog_date'] and request.POST['blog_author']:
			results = Articles.objects.filter(blog_author = request.POST['blog_author'])
		# date and author
		else: 
			results = Articles.objects.filter(blog_author = request.POST['blog_author'], blog_date = request.POST['blog_date'])
		results_package = []
		for i in results:
			if isinstance(i.blog_date, datetime.date):
				date = i.blog_date.strftime('%D')
			results_package.append(({'blog_author': i.blog_author, 'id': i.id, 'blog_date': date, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
		request.session['results'] = results_package
	else:
		print "oopsie"
	return redirect(searchpage)

# loads a page with links to all articles

def all(request):
	# pops session results for searches so old searches aren't in the session the next time someone goes back to the search page
	request.session.pop('results')
	all_articles = Articles.objects.order_by('-blog_date').all()
	article_links = []
	for i in all_articles: 
		if isinstance(i.blog_date, datetime.date):
			date = i.blog_date.strftime('%D')
		article_links.append(({'blog_author': i.blog_author, 'id': i.id, 'blog_date': date, 'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
	request.session['article_list'] = article_links
	return render(request, 'blogposts/all.html')

# loads a particular article

def article(request, article_id):
	# pops session results for searches so old searches aren't in the session the next time someone goes back to the search page
	request.session.pop('results')
	article = Articles.objects.filter(id = article_id)
	article_package = []
	for i in article: 
		if isinstance(i.blog_date, datetime.date):
			date = i.blog_date.strftime('%D')
		article_package.append(({'blog_author': i.blog_author, 'blog_article': i.blog_article, 'id': i.id, 'blog_date': date,'blog_headline': i.blog_headline, 'blog_image': i.blog_image}))
	request.session['article'] = article_package
	return render(request, 'blogposts/article.html')

# loads a page about the authors

def about(request):
	# pops session results for searches so old searches aren't in the session the next time someone goes back to the search page
	request.session.pop('results')
	return render(request, 'blogposts/about.html')