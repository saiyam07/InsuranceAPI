'''
defines url paths for the views available
'''
from django.urls import path,re_path
from .views import PolicyView,CustomerPolicyView,PolicyUpdateView,PolicyRegionalSalesView,PolicyMonthlySalesView

urlpatterns=[
    #PolicyView
    re_path(r'^get(?P<policy>)',PolicyView.as_view()),
    #Customer Policies View
    re_path(r'^policies(?P<customer>)',CustomerPolicyView.as_view()),
    #Policy update view
    path('policy/update/<pk>',PolicyUpdateView.as_view()),
    #Policy sales view
    re_path(r'^policy/sales(?P<region>)',PolicyRegionalSalesView.as_view()),
    path('policy/monthly/sales',PolicyMonthlySalesView.as_view())
]
