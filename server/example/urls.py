from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

from crest_app.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(HomeView.as_view(), redirect_field_name=None)),
    url(r'^login/$', 'crest_app.views.login', name='user_login'),
    url(r'^logout/$', 'crest_app.views.logout', name='user_logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^test/$', 'main.views.test', name='main_test'),
    url(r'^stratop/(?P<stratop_id>[^/]+)/?$', 'main.views.stratop_state', name='main_stratop'),
    url(r'^test/(?P<stratop_id>[^/]+)/?$', 'main.views.test', name='main_test'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
