from django.shortcuts import render
from django.http import HttpResponse
from .forms import ChaiVarityForm
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import ChaiVarity , Store
def all_chai(request ) :
    chais = ChaiVarity.objects.all()
    return render(request ,'chai/all_chai.html', {'chais': chais})

def chai_detials (request , chai_id) :
    chai = get_object_or_404(ChaiVarity , pk=chai_id)
    return render (request , 'chai/chai_details.html' , {'chai':chai})



def chai_store_view(request):
    stores =None 
    if request.method =='POST' :
        form = ChaiVarityForm(request.POST)

        if form.is_valid() :
            chai_variety = form.cleaned_data['chai_varity_form']
            stores = Store.objects.filter(chai_varities=chai_variety)
            print(stores)
    else :
        form = ChaiVarityForm()
    return render (request,'chai/chai_stores.html', {'stores ': stores , 'form' : form})
