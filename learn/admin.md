# 🧭 Django Admin — Asosiy Parametrlar Qo‘llanmasi

Django Admin — bu sizning modellarni (jadval ma’lumotlarini) boshqarish uchun tayyor web-interfeys.  
`admin.ModelAdmin` klassi yordamida har bir modelning admin paneldagi ko‘rinishini moslashtirish mumkin.

---

## ⚙️ 1. Asosiy tuzilma

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    list_filter = ('age',)
    search_fields = ('name',)
    ordering = ('name',)
```

---

## 📋 2. Eng muhim `ModelAdmin` parametrlar

| Parametr | Ma’nosi | Misol |
|-----------|----------|--------|
| **list_display** | Jadvalda ko‘rinadigan ustunlar | `('name', 'email', 'age')` |
| **list_display_links** | Qaysi ustun bosilganda tahrir sahifasiga olib o‘tsin | `('name',)` |
| **list_filter** | Chap tomonda filtr bo‘limi | `('age', 'gender')` |
| **search_fields** | Qidirish uchun maydonlar | `('name', 'email')` |
| **ordering** | Jadvalni tartiblash | `('-age',)` → kamayish tartibi |
| **list_per_page** | Har sahifada nechta yozuv chiqsin | `list_per_page = 20` |
| **readonly_fields** | Faqat o‘qish uchun maydonlar | `('created_at',)` |
| **fields** | Formada faqat shu maydonlar ko‘rinsin | `('name', 'email')` |
| **exclude** | Formada ko‘rinmasin degan maydonlar | `exclude = ('secret_code',)` |
| **date_hierarchy** | Yuqorida sana bo‘yicha filtr | `date_hierarchy = 'created_at'` |
| **prepopulated_fields** | Avtomatik to‘ldiriladigan maydonlar | `{'slug': ('title',)}` |
| **inlines** | Bog‘langan (related) modellarning ichki ko‘rinishi | (masalan: `BookInline`) |
| **actions** | Tanlangan obyektlarga maxsus amallar (delete, export, boshqalar) | `actions = ['export_csv']` |

---

## 🧠 3. Amaliy misol

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')
    list_display_links = ('name',)
    list_filter = ('age',)
    search_fields = ('name', 'email')
    ordering = ('name',)
    list_per_page = 10
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    empty_value_display = '—'
```

> ✅ Natija:
> - Jadvalda `name`, `email`, `age` ko‘rinadi  
> - Chapda `age` bo‘yicha filtr  
> - Yuqorida `search` maydoni (`name`, `email` bo‘yicha)  
> - 10 tadan yozuv sahifada  
> - `created_at` ni o‘zgartirib bo‘lmaydi  
> - Bo‘sh maydonlar `—` bilan chiqadi

---

## 🧩 4. Qo‘shimcha foydali parametrlar

| Parametr | Tavsif | Misol |
|-----------|--------|--------|
| **save_on_top** | Saqlash tugmasi yuqorida ham chiqadi | `save_on_top = True` |
| **empty_value_display** | Bo‘sh maydonlar uchun matn | `empty_value_display = "Noma’lum"` |
| **list_editable** | Jadvalda to‘g‘ridan-to‘g‘ri tahrirlash | `list_editable = ('age',)` |
| **show_full_result_count** | Katta ma’lumotda tezroq ishlaydi | `show_full_result_count = False` |
| **list_select_related** | ForeignKey ma’lumotlarini tez olish | `list_select_related = ('group',)` |

---

## 🔗 5. Bog‘langan model (InlineAdmin) misoli

```python
from django.contrib import admin
from .models import Author, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # nechta bo‘sh qator chiqsin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [BookInline]
```

---

## 🎨 6. Username (yoki har qanday maydon) ni link qilish

```python
from django.utils.html import format_html
from django.urls import reverse

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username_link', 'email', 'is_active')

    def username_link(self, obj):
        url = reverse('user_profile', args=[obj.id])
        return format_html('<a href="{}">{}</a>', url, obj.username)

    username_link.short_description = "Username"
```

---

## 💡 7. Foydali maslahatlar

- ✅ `@admin.register(ModelName)` — bu `admin.site.register(ModelName, ModelAdmin)` ning qisqa shakli.  
- ⚙️ `USE_TZ = True` bo‘lsa, vaqt har doim UTC’da saqlanadi, lekin sizning `TIME_ZONE` bo‘yicha ko‘rsatiladi.  
- 👁 `readonly_fields` — `auto_now_add` maydonlari uchun juda foydali.  
- 🚀 `list_select_related` — `ForeignKey`li jadvalda “N+1 query” muammosini hal qiladi.  

---

## 📚 8. Qo‘shimcha o‘qish uchun
- [Django Docs — ModelAdmin API](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#modeladmin-options)
- [Django InlineModelAdmin Docs](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#inlinemodeladmin-objects)
