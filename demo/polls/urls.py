from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.DetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/results/$',
        view=views.ResultsView.as_view(),
        name='results'
    ),
    url(
        regex=r'^(?P<question_id>[0-9]+)/vote/$',
        view=views.vote,
        name='vote'
    ),
]
