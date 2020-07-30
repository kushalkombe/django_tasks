from django.conf.urls import url,include 
from rest_framework import routers 
from Firstapp.api.views import ITJobsCRUDCBV ,MECHJobsCRUDCBV
router=routers.DefaultRouter() 
router.register('itjobs',ITJobsCRUDCBV) 
router.register('mechjobs',MECHJobsCRUDCBV)
urlpatterns = [url('', include(router.urls)),
]
 