from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^create/$', views.create_message, name='create_message'),
    url(r'^reply/(?P<message_pk>\d+)/$', views.reply_message, name='reply_message'),
]