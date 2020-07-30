from django.urls import path
from appone import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
              path('home/',views.home_view),
              path('register/',views.r_view),
              path('login/',views.login_view, name='login'),
              path('create/',views.StudentCreate.as_view()),
              path('scourse/',views.CourseList.as_view(),name='courselist'),
              path('course/<int:pk>/',views.CourseDetail.as_view(),name='detail'),
              path('authlog/',views.student_login),
              path('authlogout/',views.student_logout),
              path('batch/<int:pk>/',views.batchDetail.as_view(),name='detail'),
              path('faculty/<int:pk>/',views.facultyDetail.as_view(),name='detail')

      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
