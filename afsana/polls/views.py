from django.shortcuts import render,redirect,get_object_or_404
import datetime
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponseRedirect
from django.template import loader
from .models import signup
from django.views.generic.edit import CreateView
from .forms import SignupModelForm
from django.http import Http404
from django.db.models import Q
from django.contrib.auth import authenticate


def index(request):
    # doc="<h1>{title}<h1>".format(title=title)
    # django_rendered_doc="<h1>{{title}}<h1>".format(title=title)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html')
@login_required(login_url='/login/')
def signin(request):
    if request.method == "POST":
        email= request.POST.get('email_id')
        password = request.POST.get('password')
        print(email,password)

        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            if user.is_authenticated:
                signin(request, user)
                return HttpResponseRedirect('polls/dashboard.html')
            else:
                return HttpResponse("This user is not active. Please contact support@company.com")
        else:
             return HttpResponseRedirect('polls/signin.html')
    return render(request, "polls/signin.html", {})
#   return HttpResponseRedirect('/login/')
#     return render(request, "app/login.html", {})
    # form=SignupModelForm()
    # if request.method=='POST':
    #     # user=request.POST.get('user')
    #     email=request.POST.get('email_id')
    #     password=request.POST.get('password')
    #     print(email,password)

    #     data=authenticate(request,email=email,password=password)
    #     print(data)
    #     # if data is not None and user=='provider':
    #     #      return render(request,'polls/dashboard.html')
    #     # else:
    #     #             print("errors")
    #     template_name="polls/signin.html"
    #     context={"form":form}
    #     return render(request,template_name,context)
    #   form=SignupModelForm()
    #     #  user = get_user_model()
    #   def authenticate(self,email=None,password=None,**kwargs):
    #     try:
    #         # below line gives query set,you can change the queryset as per your requirement
    #         data = signup.objects.filter(
    #             Q(user__iexact=user)   |
    #             Q(email__iexact=email) |
    #             Q(passwqord__iexact=password)
    #         ).distinct()
    #     except signup.DoesNotExist:
    #         return None
        # print('hello')
        # qs=signup.objects.filter(email__iexact=email,user__iexact=user,password__iexact=password)
        # #    form=SignupModelForm(request.POST)
        
        # print(request.POST)
        # print("request line",form)

        # if form.is_valid():
        #     print("form.cleaned_data")
        #     if email==email and user=='provider' and password==password:
        #                 form.save(commit=True)
        #                 return render(request,'polls/dashboard.html')
        #     else:
        #             print(form.errors)
        # template_name="polls/signin.html"
        # context={"form":form}
        # return render(request,template_name,context)
    # return render(request,'polls/signin.html')
def signin_view(request):
    # if request.method=='POST':
        obj=signup.objects.filter(email_id=Email)
        for object_list in obj:
            print(object_list)
        context={"email":obj.email_id}
        print(obj)
        return render(request,"polls/signin.html",context)
        user = User.objects.get(email__exact='usermail@example.com')

This would generate SQL that looks like this:

SELECT ... WHERE email = 'usermail@example.com';

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

def signup_list_view(request):
    #list out objects
    #could be search
    qs=signup.objects.all()
    # qs=BlogPost.objects.filter(title__icontains="NEW")
    # qs=BlogPost.objects.filter(title__icontains="MY")
    template_name='polls/example.html'
    context={"objects_list":qs}
    return render(request,template_name,context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
