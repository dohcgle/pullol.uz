# Django + PostgreSQL + Docker Boilerplate

Ushbu loyiha Django, PostgreSQL va Docker texnologiyalari asosida qurilgan boshlang'ich shablon (boilerplate).

## Talablar

Loyihani ishga tushirish uchun quyidagi dasturlar o'rnatilgan bo'lishi kerak:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## O'rnatish va Ishga Tushirish (Step-by-step)

### 1-qadam: Loyiha fayllarini tekshirish
Loyihaning barcha fayllari (`Dockerfile`, `docker-compose.yml`, `requirements.txt` va boshqalar) mavjudligiga ishonch hosil qiling.

### 2-qadam: Docker konteynerlarini qurish va ishga tushirish
Terminalni oching va loyiha papkasida quyidagi buyruqni bering:

```bash
docker-compose up --build
```

Bu buyruq quyidagilarni bajaradi:
1. Python va kerakli kutubxonalarni o'z ichiga olgan rasmni (image) quradi.
2. PostgreSQL ma'lumotlar bazasini yuklab oladi va ishga tushiradi.
3. Django serverini `0.0.0.0:8000` portida ishga tushiradi.

### 3-qadam: Ilovani tekshirish
Brauzerda [http://localhost:8000](http://localhost:8000) manziliga kiring. Agar hammasi to'g'ri bo'lsa, siz Django-ning standart "The install worked successfully!" sahifasini ko'rasiz.

### 4-qadam: Superuser yaratish (Ixtiyoriy)
Admin panelga kirish uchun superuser yaratishingiz mumkin. Buning uchun yangi terminal oynasida loyiha papkasida turib:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
buyruqlarini bajaring va kerakli ma'lumotlarni kiriting.

## Loyiha Tuzilmasi

- `apps/` - Django ilovalari (apps) shu yerda joylashadi.
- `core/` - Loyihaning asosiy sozlamalari (`settings.py`, `urls.py`).
- `docker-compose.yml` - Docker xizmatlari konfiguratsiyasi.
- `Dockerfile` - Python muhitini yaratish qoidalari.
# pullol.uz
