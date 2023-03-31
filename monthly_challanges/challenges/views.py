from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = ""
    if month == "january":
        challenge_text = "Eat no meat!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    elif month == "april":
        challenge_text = "Eat no meat!"
    elif month == "may":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "june":
        challenge_text = "Learn Django for at least 20 minutes every day!"

    return HttpResponse(challenge_text)
