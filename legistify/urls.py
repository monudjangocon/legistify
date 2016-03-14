from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'legistify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lawyer.views.home'),
    url(r'^register/$', 'lawyer.views.UserInfo'),
    url(r'^legal_info/$', 'lawyer.views.LegalInfo'),
    url(r'^basic_info/$', 'lawyer.views.BasicInfo'),
    url(r'^bar_info/$', 'lawyer.views.BarInfo'),
    url(r'^login/$', 'lawyer.views.Login'), 
]
