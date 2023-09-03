from django.urls import path, register_converter, converters
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'

class FarsiSlug:
    regex = "^[a-z0-9]+(?:-[a-z0-9]+)*$"

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value

# register_converter(converters.FarsiSlug, "slugf")
# register_converter(FarsiSlug, "slugf")

urlpatterns = [
    path('', views.post_list, name="post_list"),
    # path('', views.PostListView.as_view(), name="post_list"),
    # path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('tag/<str:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('<int:id>/', views.post_detail, name="post_detail"),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
    path('<int:year>/<int:month>/<int:day>/<str:post>/', views.post_detail, name="post_detail"),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
