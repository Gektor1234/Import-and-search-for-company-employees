from django.urls import path
from .views import WorkersViewByName,ImportWorkers


app_name = 'worker'
# создаем urls для наших эндпоинтов api
urlpatterns = [
    path('information by name or surname/<str:name_or_surname>',WorkersViewByName.as_view()),
    path('loaddata',ImportWorkers.as_view()),
]