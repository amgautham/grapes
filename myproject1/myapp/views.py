from django.shortcuts import render,redirect,get_object_or_404
from . forms import my_form
from . models import my_table
def add_form(request):
    if request.method == 'POST':
        form=my_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('show')
    else:
        form=my_form()

    return render(request,'forms.html',{'form':form})
# Create your views here.
def show_table(request):
    return render(request,'show_table.html',{'show':my_table.objects.all()})

def update_table(request,pk):
    my_item=get_object_or_404(my_table,pk=pk)
    if request.method=='POST':
        form=my_form(request.POST,instance=my_item)
        if form.is_valid():
            form.save()
            return redirect ('show')
    else:
            form=my_form(instance=my_item)
    return render(request,'update_form.html',{'form':form,'item':my_item})

def delete_table(request,pk):
    my_item=get_object_or_404(my_table,pk=pk)
    if request.method=='POST':
        form=my_form(request.POST,instance=my_item)
        my_item.delete()
        return redirect ('show')
    return render(request,'delete_table.html',{'item':my_item})