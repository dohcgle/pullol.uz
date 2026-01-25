from django.db import models

class Application(models.Model):
    REGION_CHOICES = [
        ('toshkent_sh', 'Toshkent shahri'),
        ('toshkent_vil', 'Toshkent viloyati'),
        ('andijon', 'Andijon viloyati'),
        ('buxoro', 'Buxoro viloyati'),
        ('fargona', 'Farg\'ona viloyati'),
        ('jizzax', 'Jizzax viloyati'),
        ('namangan', 'Namangan viloyati'),
        ('navoiy', 'Navoiy viloyati'),
        ('qashqadaryo', 'Qashqadaryo viloyati'),
        ('samarqand', 'Samarqand viloyati'),
        ('sirdaryo', 'Sirdaryo viloyati'),
        ('surxondaryo', 'Surxondaryo viloyati'),
        ('xorazm', 'Xorazm viloyati'),
        ('qoraqalpogiston', 'Qoraqalpog\'iston Respublikasi'),
    ]

    COLLATERAL_CHOICES = [
        ('mashina', 'Avtomobil (Tezkor)'),
        ('tilla', 'Tilla buyumlar (Ishonchli)'),
        ('uy_joy', 'Ko\'chmas mulk (Katta summa)'),
    ]

    SOURCE_CHOICES = [
        ('website', 'Veb-sayt'),
        ('telegram', 'Telegram Bot'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="FISH")
    phone_number = models.CharField(max_length=13, verbose_name="Telefon raqam")
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name="Hudud")
    credit_amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Kredit summasi")
    collateral = models.CharField(max_length=20, choices=COLLATERAL_CHOICES, verbose_name="Garov")
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='website', verbose_name="Manba")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.full_name} - {self.credit_amount} so'm"


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    summary = models.TextField(verbose_name="Qisqa mazmun")
    content = models.TextField(verbose_name="Maqola matni", blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ['-created_at']
