from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import signup

from .forms import signup
from django.http import Http404


def index(request):
    # doc="<h1>{title}<h1>".format(title=title)
    # django_rendered_doc="<h1>{{title}}<h1>".format(title=title)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html')

def signin(request):
    return render(request,'polls/signin.html')

def util(request):
    return render(request,'polls/util.html')

def dashboard(request):
    return render(request,'polls/dashboard.html')

def form_view(request):
    # my_title="Hello there.."
    # print(request.POST)
    form=signup(request.POST or None)
    if form.is_valid():
     print(form.cleaned_data)
    context={
        # "title":my_title,
        "form":form

     }
    return render(request,"polls/index.html",context)


# def signup_view(request):
#     if request.method=='POST':
#     form=SignupModelForm(request.POST or None)
#     if form.is_valid():
#       first_name=request.POST.get('first_name')
#       last_name=request.POST.get('second_name')
#       email_id=request.POST.get('email_id')
#       password=request.POST.get('password')
#       data=signup(first_name=first_name,second_name=last_name,email=email_id,password=password)
#       data1= data.save()
#       print(data1)
#       form=SignupModelForm()
#     template_name="index.html"
#     context={"form":form}
#     return render(request,template_name,context)

def signups(request):
    if request.method=="POST":
      print(request.method)
      First_name=request.POST.get('first_name')
      Last_name=request.POST.get('second_name')
      email=request.POST.get('email_id')
      Password=request.POST.get('password')

      var_signup=signups(first_name=First_name,second_name=Last_name,email=email,password=Password)
      data=var_signup.save()
      print(data)

    # obj=signup.objects.filter(slug=slug)
    # template_name="signup_get.html"
    # context={"object":obj}
    # return render(request,template_name,context)
      return render(request,'polls/signin.html')
    return render(request,'polls/index.html')



# def current_datetime(request):
#     now = datetime.datetime.now()
#     x,y=e.year,e.year+1
#     print("{}-{}".format(x,y))
#     html = "<html><body>%s.</body></html>" % now
#     return HttpResponse(html)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
