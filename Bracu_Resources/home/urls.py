from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('index',views.index, name="home"),
    path('Courses', views.Courses,name='Courses'),
    path('CourseInformation', views.CourseInformation,name='CourseInformation'),
    path('Add_resources', views.Add_Resources,name='Add_resources'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('cse1',views.cse1,name='cse1'),
    path('cse2',views.cse2,name='cse2'),
    path('cse3',views.cse3,name='cse3'),
    path('cse4',views.cse4,name='cse4'),
    path('mns1',views.mns1,name='mns1'),
    path('search',views.searchfunc,name='search'),
    
    path('view', views.show_file, name="view"),
    path('faculty', views.Faculty, name="faculty"),
    path('fac', views.show_file1, name="fac")
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
