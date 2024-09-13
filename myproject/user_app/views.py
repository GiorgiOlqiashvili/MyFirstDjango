from django.http import HttpResponse
from datetime import date


def show_user_info(request):
    first_name = "Giorgi"
    last_name = "Olqiashvili"
    birth_year = 2004
    current_year = date.today().year
    age = current_year - birth_year

    response_text = f"First Name: {first_name}, Last Name: {last_name}, Age: {age}"
    return HttpResponse(response_text)

