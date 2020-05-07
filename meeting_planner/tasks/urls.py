from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('students', views.students_list, name="students"),
    path('new', views.new, name="new")

]
