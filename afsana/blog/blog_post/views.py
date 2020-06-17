from django.shortcuts import render
from  .admin import BlogPost
# Create your views here.

def blog_post_details_page(request):
  obj=BlogPost.objects.get(id=1)
  template_name=blog_post_detail.html
  context={"object":obj}
  return render(request,template_name,context)