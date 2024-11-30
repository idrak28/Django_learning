from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
# Create your views here.
from .models import ChaiVarity
def all_chai(request ) :
    chais = ChaiVarity.objects.all()
    return render(request ,'chai/all_chai.html', {'chais': chais})

def chai_detials (request , chai_id) :
    chai = get_object_or_404(ChaiVarity , pk=chai_id)
    return render (request , 'chai/chai_details.html' , {'chai':chai})