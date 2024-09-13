from django.http import HttpResponse
import datetime


def show_date(request):
    today = datetime.date.today()
    response_text = f"Year: {today.year}, Month: {today.month}, Day: {today.day}"
    return HttpResponse(response_text)