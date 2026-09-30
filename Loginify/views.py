from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from Loginify.forms import LoginForm
from Loginify.models import UserDetails
from rest_framework.parsers import JSONParser
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt
from .serializers import LoginSystemSerializer

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")


# Task 3

def login_view(request):

    if request.method == 'POST':

        # reading the data from the form
        user_details = request.POST

        user_email = user_details.get('email')
        user_password = user_details.get('password')


        try:
            user = UserDetails.objects.get(email=user_email)

            if user.password == user_password:
                return render(request, 'Loginify/login-success.html', {'user': user})
                # return JsonResponse({'message': 'Login successful!'}, status=200)
            else:
                return JsonResponse(
                    {'message': 'Invalid email or password!'}, status=400
                )
        except UserDetails.DoesNotExist:
            return JsonResponse({'message': 'User not found! Please sign up. '}, status=404)

    elif request.method == 'GET':
            
        return render(request, 'Loginify/login.html')



def signup_view(request):


    if request.method == 'POST':

        # reading the data from the form
        form = LoginForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('login')

            # return render(request, 'Loginify/login.html', {'message': 'User created successfully! Please log in.'})

            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']

            # saving the data to the database
            # user = UserDetails(name=name, email=email, password=password)
            # user.save()

        else:
            return render(request, 'Loginify/signup.html', {'form': form, 'message': 'Invalid data! Please try again.'})

            # return JsonResponse({'message': 'User created successfully!'}, status=200)



    
    elif request.method == 'GET':
        form = LoginForm()
        
        return render(request, 'Loginify/signup.html', {'form': form})


# Task 5

'''
CRUD Operations for LoginSystem

C -> Create -> POST()
R -> Read -> GET()
U -> Update -> PUT()
D -> Delete -> DELETE()
'''

@csrf_exempt
def AllUsersData(request):
    try:
        all_users_data = UserDetails.objects.all()
    except UserDetails.DoesNotExist:
        data = {
            "message": "No data found in the database!",
            "status": 404
        }

        return JsonResponse(data, status=404)

    if request.method == "GET":
        all_users_data_s = LoginSystemSerializer(all_users_data, many=True)

        return JsonResponse(all_users_data_s.data, safe=False, status=200)
    
    elif request.method == "POST":
        input_data = JSONParser().parse(request)
        user_data_s = LoginSystemSerializer(data=input_data) 
        if user_data_s.is_valid():
            user_data_s.save()
    
            return JsonResponse(user_data_s.data, status=201)
        else:
            return JsonResponse(user_data_s.errors, status=400)


   

@csrf_exempt
def SingleUserData(request, username):
    try:
        single_user_data = UserDetails.objects.get(username=username)
    except UserDetails.DoesNotExist:
        data = {
            "message": "No data found in the database!",
            "status": 404
        }

        return JsonResponse(data, status=404)

    if request.method == "GET":
        single_user_data_s = LoginSystemSerializer(single_user_data)

        return JsonResponse(single_user_data_s.data, safe= False, status=200)

    elif request.method == "PUT":
        input_data = JSONParser().parse(request)
        user_data_s = LoginSystemSerializer(single_user_data, data=input_data)

        if user_data_s.is_valid():
            user_data_s.save()

            return JsonResponse(user_data_s.data, status=200)
        else:
            return JsonResponse(user_data_s.errors, status=400)
        
    elif request.method == "DELETE":
        single_user_data.delete()
        data1 = {
            "message": "Data deleted successfully!",
            "status": 200
        }

        return JsonResponse(data1, status=200)
