from django.http import JsonResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = list(companies.values('id', 'name', 'description', 'city', 'address'))
    return JsonResponse(data, safe=False)

def company_detail(request, id):
    company = Company.objects.filter(id=id).first()
    if company is None:
        return JsonResponse({'error': 'Company not found'}, status=404)
    data = {
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }
    return JsonResponse(data)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = list(vacancies.values('id', 'name', 'description', 'salary', 'company_id'))
    return JsonResponse(data, safe=False)

def vacancy_detail(request, id):
    vacancy = Vacancy.objects.filter(id=id).first()
    if vacancy is None:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    data = {
        'id': vacancy.id,
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company_id': vacancy.company.id
    }
    return JsonResponse(data)

def vacancies_by_company(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    data = list(vacancies.values('id', 'name', 'description', 'salary', 'company_id'))
    return JsonResponse(data, safe=False)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    data = list(vacancies.values('id', 'name', 'description', 'salary', 'company_id'))
    return JsonResponse(data, safe=False)
