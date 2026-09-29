from django.shortcuts import render,redirect
from .forms import AddressForm
from .models import Address

# Create your views here.
def add_address(request):
    form=AddressForm()
    if request.method == 'POST':
        form_data=AddressForm(request.POST)
        if form_data.is_valid():
            a=form_data.save(commit=False)
            a.user=request.user
            a.save()
    return render(request,'add_address.html',{'form':form})

def address_list(request):
    address=Address.objects.all()
    return render(request,'address_list.html',{'address':address})

def update_address(request,pk):
    data= Address.objects.get(id=pk)
    if request.method == 'POST':
            form_data=AddressForm(request.POST,instance=data)
            if form_data.is_valid():
                a=form_data.save(commit=False)
                a.user=request.user
                a.save()
                return redirect('address_list')
    else:
        form=AddressForm(instance=data)
        context={'form':form}
    return render(request,'update_address.html',context)



