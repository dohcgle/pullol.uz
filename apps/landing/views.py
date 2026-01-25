from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm
from .models import BlogPost

def index(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message (requires messages middleware to be set up, usually is default)
            messages.success(request, "Arizangiz muvaffaqiyatli qabul qilindi! Tez orada aloqaga chiqamiz.")
            return redirect('index')
        else:
            messages.error(request, "Xatolik yuz berdi. Iltimos, ma'lumotlarni tekshirib qaytadan urinib ko'ring.")

    blog_posts = BlogPost.objects.all().order_by('-created_at')[:6]

    context = {
        'form': form,
        'blog_posts': blog_posts
    }
    return render(request, 'landing/index.html', context)

def webapp_form(request):
    return render(request, 'landing/webapp_form.html')

