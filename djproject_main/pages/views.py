from django.http import response
from django.shortcuts import render

# Create your views here.




def home_view(request):
    #print(request.user)
    return render(request,'home.html',{})


def about_view(request):
    
    my_context={
        "key":"value",
        "Title":"this is a title",
    }
    
    
    return render(request,"about.html",{})

