from django.urls import path
from . import views

urlpatterns = [
    path('api/companies/', views.company_list, name='company-list'),
    path('api/companies/<int:id>/', views.company_detail, name='company-detail'),
    path('api/companies/<int:id>/vacancies/', views.vacancies_by_company, name='vacancies-by-company'),
    path('api/vacancies/', views.vacancy_list, name='vacancy-list'),
    path('api/vacancies/<int:id>/', views.vacancy_detail, name='vacancy-detail'),
    path('api/vacancies/top_ten/', views.top_ten_vacancies, name='top-ten-vacancies')
]
