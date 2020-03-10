from django.contrib import admin

from .models import Workers

admin.site.register(Workers) # регистрация модели в админ панельке джанго(не обязательно,если вы ее не используете)
