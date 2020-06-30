from django.shortcuts import render
from  .admin import BlogPost
from .models import BlogPost
from .forms import BlogPostModelForm
# Create your views here.

def blog_post_details_page(request):
  obj=BlogPost.objects.get(id=1)
  template_name=blog_post_detail.html
  context={"object":obj}
  return render(request,template_name,context)

def blog_post_create_view(request):
    form=BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=BlogPostModelForm()
    template_name="form.html"
    context={"form":form}
    return render(request,template_name,context)

