from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "jan": "hi jan",
    "feb": "hi feb"
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month number")
    redirected_month = months[month - 1]
    redirected_path = reverse("month-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirected_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, "month": month.capitalize()
        })
    except:
        return HttpResponseNotFound("invalid")
