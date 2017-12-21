from django.conf.urls import url
from .views import BranchDetailAPIView, BranchListAPIView

urlpatterns = [
    url('^branch-retrieve/(?P<ifsc>\w+)/$', BranchDetailAPIView.as_view(),
        name="branch-detail-view"),
    url('^bank-branches/(?P<bank>[\w ]+)/(?P<city>[\w ]+)/$', BranchListAPIView.as_view(),
        name="bank-branches-view"),
]