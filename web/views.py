from django.shortcuts import render
from django.http import JsonResponse, response
from django.views import View
import datetime


def calc(date):
    """
    Base function to calculate week
    """
    base = datetime.date(2019,1,6)
    days = (date - base).days
    weeks = (days // 7) + 2
    return weeks

def home(request):
    """
    Index page to enter date
    """
    return render(request, 'home.html')


class CalcView(View):
    """
    CalcView to calculate weeks and return result in html
    """
    def get(self, request, date):
        try:
            date_f = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            week = calc(date_f)

            if week > 0:
                postfix = "th"
                if week == 1: postfix = "st"
                if week == 2: postfix = "nd"
                data = {
                    "success": True,
                    "date": date,
                    "week": week,
                    "postfix": postfix
                    }
            else:
                data = {
                    "success": False,
                    "message": "Enter date after January 1, 2019." 
                }
        except:
            data = {
                "success": False,
                "message": "Invalid date format try again." 
            }
        
        return render(request, 'calc.html', context=data)


class APICalcView(View):
    """
    APICalcView to calculate weeks and return result in json
    """
    def get(self, request, date):
        try:
            date_f = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            week = calc(date_f)

            if week > 0:
                data = {
                    "status": "success",
                    "week": week
                }
                response = JsonResponse(data, status=200)
            else:
                data = {
                    "status": "success",
                    "message": "Enter date after January 1, 2019." 
                }
                response = JsonResponse(data, status=400)
        except:
            data = {
                "status": "success",
                "message": "Invalid date format try again." 
            }
            response = JsonResponse(data, status=400)
        return response
