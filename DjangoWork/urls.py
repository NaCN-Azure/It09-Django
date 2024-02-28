"""
URL configuration for DjangoWork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.views import job_views,user_views,apply_views,feedback_views
from django.urls import path, re_path


# 我说明一下，这个name字段是给前端html获取这个url的名称，比如{% url 'get_user_info' 1 %}，就会得到userInfo/1，虽然不知道为什么出现在这里
# user的地方除了info没有其他返回的，具体返回的数据被分装在Json里，具体的你们可以去看get_user_info的逻辑，前端可以通过字典拿到那个json,其他的get方法你可以沿用这个逻辑
# 一般而言，调用时肯定要用到ajax
urlpatterns = [
    #这部分就是主要的视图方法
    path('admin/', admin.site.urls),

    #user视图部分
    path('register/<int:user_type>', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('userInfo/<int:user_id>/', user_views.get_user_info, name='get_user_info'),
    path('user/<int:user_id>/update/', user_views.update_user_info, name='update_user_info'),
    path('logout/', user_views.logout_user, name='logout'),
    path('userInfo/<int:user_id>/change_password/', user_views.change_password, name='change_password'),

    path("index/",job_views.index_view, name='index'),

    #application视图部分
    path('application/create/', apply_views.create_application_view, name='create_application'),
    path('application/update/<int:application_id>/', apply_views.update_application_status_view, name='update_application_status'),
    path('application/searchByUser/<int:user_id>/', apply_views.get_applications_by_user_view, name='get_applications_by_user'),
    path('application/searchByJob/<int:job_id>/', apply_views.get_applications_by_job_view, name='get_applications_by_job'),
]
