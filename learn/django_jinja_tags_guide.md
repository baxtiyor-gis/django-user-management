# 🧩 Django Template (Jinja-style) Taglar — Soddalashgan Qo‘llanma

Django templating tili (ko‘p jihatdan Jinja2 ga o‘xshash) HTML ichida Python kodining soddalashtirilgan ko‘rinishini ishlatadi.  
Quyida eng ko‘p ishlatiladigan **taglar** va **filtrlar** soddaroq misollar bilan keltirilgan.

---

## ⚙️ 1. Asosiy Sintaksis

| Element | Sintaksis | Ma’nosi |
|----------|------------|----------|
| **O‘zgaruvchi** | `{{ variable }}` | O‘zgaruvchi qiymatini chiqaradi |
| **Tag** | `{% tag_name %}` | Mantiqiy amallar bajaradi (if, for, block va boshqalar) |
| **Izoh (comment)** | `{# bu izoh #}` | HTML’da chiqmaydi |

---

## 🔹 2. O‘zgaruvchilar

```html
<p>Salom, {{ user.username }}!</p>
<p>Bugun: {{ today }}</p>
```

Agar `user.username = "Bakhtiyor"` bo‘lsa, natija:  
👉 `Salom, Bakhtiyor!`

---

## 🔹 3. If / Else shartlari

```html
{% if user.is_authenticated %}
  <p>Salom, {{ user.username }}!</p>
{% else %}
  <p>Iltimos, tizimga kiring.</p>
{% endif %}
```

Shuningdek:
```html
{% if age > 18 %}
  Kattalar uchun
{% elif age > 13 %}
  O‘smirlar uchun
{% else %}
  Bolalar uchun
{% endif %}
```

---

## 🔹 4. For sikl

```html
<ul>
{% for student in students %}
  <li>{{ student.name }} — {{ student.age }} yosh</li>
{% endfor %}
</ul>
```

Qo‘shimcha:
```html
{% for item in items %}
  {{ forloop.counter }}. {{ item }}
{% endfor %}
```
> `forloop.counter` → 1 dan boshlab sanaydi

---

## 🔹 5. Include (boshqa faylni qo‘shish)

```html
{% include "partials/header.html" %}
```

Bu `partials/header.html` faylini shu joyga joylashtiradi.

---

## 🔹 6. Block va Extends (template meros olish)

### base.html
```html
<html>
  <body>
    <h1>{% block title %}Sarlavha{% endblock %}</h1>
    {% block content %}{% endblock %}
  </body>
</html>
```

### home.html
```html
{% extends "base.html" %}

{% block title %}Bosh sahifa{% endblock %}
{% block content %}
  <p>Salom, bu bosh sahifa!</p>
{% endblock %}
```

---

## 🔹 7. Commentlar

```html
{# Bu izoh, sahifada ko‘rinmaydi #}
```

---

## 🔹 8. Filtrlar ({{ ... | filter }})

| Filtr | Ma’nosi | Misol |
|--------|----------|--------|
| **upper** | Barcha harflarni katta qiladi | `{{ name|upper }}` → `BAKHTIYOR` |
| **lower** | Barcha harflarni kichik qiladi | `{{ name|lower }}` |
| **title** | Har bir so‘zni katta harf bilan | `{{ name|title }}` |
| **length** | Elementlar soni | `{{ items|length }}` |
| **default:"Noma’lum"** | Bo‘sh bo‘lsa, default qiymat | `{{ user.email|default:"Noma’lum" }}` |
| **date:"Y-m-d"** | Sanani formatlash | `{{ today|date:"d-m-Y" }}` |
| **truncatechars:20** | Matnni 20 belgigacha qisqartiradi | `{{ text|truncatechars:20 }}` |
| **safe** | HTML ni ekranga chiqaradi (escape qilmaydi) | `{{ html|safe }}` |

---

## 🔹 9. Static fayllarni ulash

Faylning boshida:
```html
{% load static %}
```

Keyin:
```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## 🔹 10. URL tag

```html
<a href="{% url 'home' %}">Bosh sahifa</a>
<a href="{% url 'user_profile' user.id %}">Profil</a>
```

> URL nomlari `urls.py` faylidagi `name='home'` yoki `name='user_profile'` ga mos bo‘lishi kerak.

---

## 🔹 11. Template ichida arifmetika (cheklangan)

```html
{{ value|add:5 }}
```
> `add` filtri raqam yoki stringga qo‘shadi.

---

## 🔹 12. Custom tag va filter yaratish (ixtiyoriy)

**my_tags.py** (app ichida `templatetags/` papkada):
```python
from django import template

register = template.Library()

@register.filter
def shout(value):
    return value.upper() + '!!!'
```

Template’da ishlatish:
```html
{% load my_tags %}
{{ "salom"|shout }}   →  SALOM!!!
```

---

## 💡 Foydali maslahatlar

- Har doim `{{ }}` — o‘zgaruvchilar uchun, `{% %}` — kod (tag) uchun.  
- `extends` va `block` — template’lar uchun **asosiy strukturaviy elementlar**.  
- `safe` filtri bilan ehtiyot bo‘ling (faqat ishonchli HTML uchun).  
- `forloop.counter`, `forloop.first`, `forloop.last` kabi maxsus o‘zgaruvchilar mavjud.

---

## 📚 Qo‘shimcha manbalar
- [Django Template Language Docs](https://docs.djangoproject.com/en/stable/ref/templates/language/)
- [Jinja2 Template Guide](https://jinja.palletsprojects.com/en/latest/templates/)
