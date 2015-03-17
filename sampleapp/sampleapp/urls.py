from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', 'searchapp.views.home', name='home'),
    url('^load-data$', 'searchapp.views.load_csv_data', name='load_csv_data'),
)
