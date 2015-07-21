from django.conf.urls import patterns,url
from signup import views
urlpatterns = [
	url(r'^$',views.index, name = "index"),
	url(r'^index/',views.index, name = "index"),
	url(r'^terms/', views.terms, name = "terms"),
	url(r'^privacy/', views.privacy, name = "privacy"),
	url(r'^aboutus/', views.about, name  = "about"),
	
]
