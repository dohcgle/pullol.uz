from apps.landing.models import BlogPost
from django.core.files.base import ContentFile
import requests

posts = [
    {
        'title': "Kredit tarixi: Qanday qilib 'yaxshi' bo'lib qolish mumkin?",
        'image_url': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "Kredit tarixi nima va u kelajakdagi moliyaviy imkoniyatlaringizga qanday ta'sir qiladi? Muhim maslahatlar."
    },
    {
        'title': "Biznesni 0 dan boshlash: Afsona va Haqiqat",
        'image_url': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "Sarmoyasiz biznes boshlash mumkinmi? Tajribali tadbirkorlardan real keyslar va maslahatlar."
    },
    {
        'title': "Mikrokredit vs Oddiy Kredit: Farqi nimada?",
        'image_url': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "Sizning ehtiyojlaringiz uchun qaysi kredit turi mos kelishini aniqlashga yordam beramiz."
    },
    {
        'title': "Moliyaviy savodxonlik: Pullarni boshqarish sirlari",
        'image_url': 'https://images.unsplash.com/photo-1565514020176-db8b525f056d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "Daromad va xarajatlarni to'g'ri rejalashtirish orqali boylik orttirish sirlari."
    },
    {
        'title': "Kelajak investitsiyasi: Bugun nimaga pul tikish kerak?",
        'image_url': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "2026 yilda eng daromadli sohalar va investitsiya qilish uchun eng yaxshi yo'nalishlar."
    },
     {
        'title': "Raqamli o'zgarishlar: Fintech kelajagi",
        'image_url': 'https://images.unsplash.com/photo-1533750349088-cd871a92f312?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'summary': "Fintech sohasi qanday rivojlanmoqda va bu sizga qanday qulayliklar yaratadi?"
    }
]

for post_data in posts:
    if not BlogPost.objects.filter(title=post_data['title']).exists():
        print(f"Creating post: {post_data['title']}")
        post = BlogPost(title=post_data['title'], summary=post_data['summary'])
        
        # Download image
        try:
            response = requests.get(post_data['image_url'])
            if response.status_code == 200:
                file_name = post_data['image_url'].split("/")[-1].split("?")[0] + ".jpg"
                post.image.save(file_name, ContentFile(response.content), save=False)
            else:
                print(f"Failed to download image: {post_data['image_url']}")
        except Exception as e:
            print(f"Error downloading image: {e}")
            
        post.save()
    else:
        print(f"Post already exists: {post_data['title']}")
