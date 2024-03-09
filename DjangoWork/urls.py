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
    #这部分是静态的测试区域
    path('', job_views.index,name='index'),
    path('admin/', admin.site.urls),
    path('job/',job_views.index,name='index'),
    path('job/job_detail/<int:job_id>/', job_views.job_detail, name='job_detail'),
    path('profile/user/', job_views.job_info, name='index_user'),
    path('profile/employer/', job_views.job_em, name='index_employer'),

    #user视图部分
    path('register/<int:user_type>/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('userInfo/<int:user_id>/', user_views.get_user_info, name='get_user_info'),
    path('userInfo/<int:user_id>/update/', user_views.update_user_info, name='update_user_info'),
    path('logout/', user_views.logout_user, name='logout'),
    path('userInfo/<int:user_id>/change_password/', user_views.change_password, name='change_password'),

    #Employer
    path("job/createJob/",job_views.create_job_view, name='create_job'),
    path("job/updateJob/<int:job_id>/",job_views.update_job_view, name='update_job'),
    path("job/jobInfo/<int:job_id>/",job_views.get_job_by_jobId_view, name='get_job_by_jobId'),
    path("job/getByEmployer/<int:employer_id>/",job_views.list_jobs_by_employer, name='get_job_by_employer_Id'),
    path("job/getAll/",job_views.list_all_jobs_view, name='get_job_all'),

    #application视图部分
    path('application/create/', apply_views.create_application_view, name='create_application'),
    path('application/update/<int:application_id>/', apply_views.update_application_status_view, name='update_application_status'),
    path('application/searchByUser/<int:user_id>/', apply_views.get_applications_by_user_view, name='get_applications_by_user'),
    path('application/searchByJob/<int:job_id>/', apply_views.get_applications_by_job_view, name='get_applications_by_job'),
    path('application/checkJob/<int:job_id>/<int:user_id>/', apply_views.check_applications, name='check_applications'),

    #feedback视图部分
    path('feedback/create/',feedback_views.add_feedback_view,name='create_feedback'),
    path('feedback/delete/<int:feedback_id>/',feedback_views.delete_feedback_view,name='delete_feedback'),
    path('feedback/getRateAverage/<int:job_id>',feedback_views.job_average_rate_view,name='get_average_view'),
    path('feedback/getByUser/<int:user_id>',feedback_views.get_feedbacks_by_user_view,name='get_feedback_by_user'),
    path('feedback/getByJob/<int:job_id>',feedback_views.get_feedbacks_by_job_view,name='get_feedback_by_job')

]
