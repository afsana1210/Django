from django.http import  HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
# def home_page(request):
#     my_title="Hello there.."
#     return render(request,"hello_world.html",{"title":my_title})

def new_example(request):
    new_title="new example.."
    context={"title":new_title}
    template_name="title.txt"
    template_obj=get_template(template_name)
    rendered_string=template_obj.render(context)
    return render(request,"hello_world.html",{"title":rendered_string})
    #return  HttpResponse(template_obj)

def home_page(request):
    my_title="Hello there.."
    context={"title":my_title,"my_list":[1,2,3]}
    return render(request,"home.html",context)

def form_view(request):
    my_title="Hello there.."
    # print(request.POST)
    form=ContactForm(request.POST or None)
    if form.is_valid():
     print(form.cleaned_data)
    context={
        "title":my_title,
        "form":form

     }
    return render(request,"form.html",context)
