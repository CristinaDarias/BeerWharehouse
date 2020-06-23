from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_view(request):

    context = {
        'sample_var': "ejemplo",
        'otra_cosa': [2, 4, 5]
    }

    return render(request, 'beers.html', context)