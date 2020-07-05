from .forms import signup
from django.shortcuts import render

def form_view(request):
    my_title="Hello there.."
    # print(request.POST)
    form=signup(request.POST or None)
    if form.is_valid():
     print(form.cleaned_data)
    context={
        "title":my_title,
        "form":form

     }
    return render(request,"forms.html",context)
