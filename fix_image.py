import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.landing.models import BlogPost
from django.core.files.base import ContentFile
import requests

title = "Moliyaviy savodxonlik: Pullarni boshqarish sirlari"
# Alternative reliable image URL (Coins/Savings)
image_url = "https://images.unsplash.com/photo-1579621970795-87facc2f976d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"

try:
    post = BlogPost.objects.get(title=title)
    print(f"Found post: {post.title}")
    
    response = requests.get(image_url)
    if response.status_code == 200:
        file_name = "financial_literacy_fixed.jpg"
        post.image.save(file_name, ContentFile(response.content), save=True)
        print("Image updated successfully.")
    else:
        print(f"Failed to download image: {response.status_code}")

except BlogPost.DoesNotExist:
    # If partial match needed or encoding issues, try matching start
    post = BlogPost.objects.filter(title__startswith="Moliyaviy savodxonlik").first()
    if post:
        print(f"Found post (fuzzy): {post.title}")
        response = requests.get(image_url)
        if response.status_code == 200:
            file_name = "financial_literacy_fixed.jpg"
            post.image.save(file_name, ContentFile(response.content), save=True)
            print("Image updated successfully.")
        else:
            print(f"Failed to download image: {response.status_code}")
    else:
        print("Post not found.")
except Exception as e:
    print(f"Error: {e}")
