import movie_api
from django.http import HttpResponse


def wrong_link(request):
    return HttpResponse("Wrong link.please enter correctly")


def info(request, movie):
    info_str = movie_api.get_data(movie)
    return HttpResponse(info_str)


def err(request, movie):
    return HttpResponse("Movie name not Correct.please enter correctly")
