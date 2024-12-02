from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request,'myapp/index.html')

def employee_list(request):
    query = request.GET.get('query', '')
    employees = Employee.objects.filter(
        Q(employee_id__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
    )
    
    paginator = Paginator(employees, 5)  # Show 5 employees per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_list.html', {'employees': page_obj})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    return render(request, 'user_data.html', {'employee': employee})

def employee_search(request):
    query = request.GET.get('query', '')
    if query:
        employees = Employee.objects.filter(first_name__icontains=query) | Employee.objects.filter(last_name__icontains=query)
    else:
        employees = Employee.objects.all()
    
    return render(request, 'user_list.html', {'employees': employees})




# from django.shortcuts import render,get_object_or_404,redirect
# from .models import User

# def index(request):
#     return render(request, 'myapp/index.html')

# def user_search(request):
#     if request.method == "GET":
#         user_id = request.GET.get('user_id', None)
#         if user_id:
#             try:
#                 user = User.objects.get(user_id=user_id)
#                 return render(request, 'user_data.html', {'user': user})
#             except User.DoesNotExist:
#                 return redirect('add_user', user_id=user_id)
#         return render(request, 'user_search.html')



# def user_details(request, user_id):
#     user = get_object_or_404(User, user_id=user_id)  # Get user by user_id
#     return render(request, 'user_data.html', {'user': user})  # Pass 'user' to template
# def display_all_users(request):
#     users = User.objects.all()  # Fetch all users
#     return render(request, 'user_search.html', {'users': users})
# def add_user(request, user_id):
#     if request.method == 'POST':
#         # Collect data from the form
#         name = request.POST.get('name')
#         nationality = request.POST.get('nationality')
#         city = request.POST.get('city')
#         latitude = request.POST.get('latitude')
#         longitude = request.POST.get('longitude')
#         gender = request.POST.get('gender')
#         ethnic_group = request.POST.get('ethnic_group')
#         age = request.POST.get('age')
#         english_grade = request.POST.get('english_grade')
#         math_grade = request.POST.get('math_grade')
#         science_grade = request.POST.get('science_grade')
#         language_grade = request.POST.get('language_grade')
#         portfolio_rating = request.POST.get('portfolio_rating')
#         cover_letter_rating = request.POST.get('cover_letter_rating')
#         ref_letter_rating = request.POST.get('ref_letter_rating')

#         # Save new user to the database
#         new_user = User(
#             user_id=user_id,
#             name=name,
#             nationality=nationality,
#             city=city,
#             latitude=latitude,
#             longitude=longitude,
#             gender=gender,
#             ethnic_group=ethnic_group,
#             age=age,
#             english_grade=english_grade,
#             math_grade=math_grade,
#             science_grade=science_grade,
#             language_grade=language_grade,
#             portfolio_rating=portfolio_rating,
#             cover_letter_rating=cover_letter_rating,
#             ref_letter_rating=ref_letter_rating,
#         )
#         new_user.save()
#         return redirect('user_search')  # Redirect back to the search page after adding

#     return render(request, 'add_user.html', {'user_id': user_id})



