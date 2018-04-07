from django.conf.urls import url
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    url(r'^branch/$', BranchAPI.as_view(), name="branchApi"),
    url(r'^appointment/$', AppointmentAPI.as_view(), name="appointmentApi"),
    url(r'^user/$', UserAPI.as_view(), name="userApi"),
]