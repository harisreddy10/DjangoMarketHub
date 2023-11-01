from django.shortcuts import render, redirect
from item.models import Category, Item
def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    context={
        'categories': categories,
        'items':items,
    }
    return render(request,'polls/index.htm',context)
def contact(request):
    return render(request,'polls/contact.htm')


from . forms import SignUpForm

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form=SignUpForm()   
    
    context={
        'form':form
    }
    return render(request,'polls/signup.htm',context)


