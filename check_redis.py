import os
import django
from django.conf import settings
from django.core.cache import cache
import time

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def check_redis():
    print("🔄 Redis keshini tekshirish...")
    try:
        # 1. Write
        start_time = time.time()
        cache.set('test_redis_key', 'Ishlayapti! 🚀', 60)
        write_time = time.time() - start_time
        
        # 2. Read
        start_time = time.time()
        value = cache.get('test_redis_key')
        read_time = time.time() - start_time
        
        if value == 'Ishlayapti! 🚀':
            print(f"✅ Muvaffaqiyatli! Redis javob qaytardi: '{value}'")
            print(f"⏱️ Yozish vaqti: {write_time:.4f}s")
            print(f"⏱️ O'qish vaqti: {read_time:.4f}s")
        else:
            print(f"❌ Xatolik! Kutilgan qiymat olinmadi. Olingan qiymat: {value}")
            
    except Exception as e:
        print(f"❌ Redis bilan ulanishda xatolik: {e}")

if __name__ == "__main__":
    check_redis()
