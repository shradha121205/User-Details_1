from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='employee_list'),  # Home page with user list and search
    path('user/<str:employee_id>/', views.employee_detail, name='employee_detail'),  # User detail page
    path('search/', views.employee_search, name='employee_search'),
]






# from django.urls import path
# from django.contrib import admin
# from . import views

# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',views.index,name='index'),
#     path('search/', views.user_search, name='user_search'),
#     path('user/<int:user_id>/', views.user_details, name='user_details'),
#     path('display-all-users/', views.display_all_users, name='display_all_users'),
#     path('user-search/', views.user_search, name='user_search'),
#     path('add-user/<str:user_id>/', views.add_user, name='add_user'),
# ]
