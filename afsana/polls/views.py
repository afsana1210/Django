from django.shortcuts import render,redirect,get_object_or_404
import datetime
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import signup
from django.views.generic.edit import CreateView
from .forms import SignupModelForm
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
    if request.method=='POST':
      form=SignupModelForm(request.POST or None)
      if form.is_valid():
          form.save()
          email_id=form.cleaned_data.get('email')
          password=form.cleaned_data.get('password')
          print('email ,password')
          return redirect(signin)
    #  print(form.cleaned_data)
    # context={
    #     # "title":my_title,
    #     "form":form

    #  }
    else: 
        form = SignupModelForm()
    return render(request,"polls/index.html",{'form':form})

class CreateMyModelView(CreateView):
    model = signup
    form_class = SignupModelForm
    template_name = 'polls/forms.html'
    success_url = 'polls/signin.html'

def signup_view(request):
     form=SignupModelForm()
     if request.method=='POST':
       print('hello')
       form=SignupModelForm(request.POST)
       print(request.POST)
       print("request line",form)

       if form.is_valid():
        print("form.cleaned_data")
        form.save(commit=True)
       else:
        print(form.errors)
     template_name="polls/forms.html"
     context={"form":form}
     return render(request,template_name,context)
#       first_name=request.POST.get('first_name')
#       last_name=request.POST.get('second_name')
#       email_id=request.POST.get('email_id')
#       password=request.POST.get('password')
#       data=signup(first_name=first_name,second_name=last_name,email=email_id,password=password)
    #   obj= form.save(commit=True)
    #   print(obj)
    #   obj.save()
    #     form=SignupModelForm()
    # template_name="polls/forms.html"
    # context={"form":form}
    # return render(request,template_name,context)

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

def signup_page_view(request,id):
  obj=get_object_or_404(signup,id=id)
  template_name="polls/example.html"
  context={"first_name":obj.first_name,"second_name":obj.second_name}
  return render(request,template_name,context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
