from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Etudiant


def index(request):
    etds = Etudiant.objects.all()
    context = {
        'etds': etds,
    }
    return render(request, 'administration/index.html', context)


def detail(request, Etudiant_id):
    try:
        etd = Etudiant.objects.get(pk=Etudiant_id)
    except Etudiant.DoesNotExist:
        raise Http404("pas d'étudiant")
    return render(request, 'administration/detail.html', {'etd': etd})
