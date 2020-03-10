Приложение для загрузки спарсенных данных из CSV файла в базу данных и поиска сотрудников по имени или фамилии.
Написано на языке PYTHON с помощью фреймворка DJANGO и библиотеки Django Rest Framework, в качестве СУБД использовался PostgreSQL.
INSTALLITION: 
  pip install django
  pip install djangorestframework
  В файле "settings" указываем свои параметры СУБД(если имеется PostgreSQL просто меняем данные и название бд)
  DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_case',
        'USER' : 'postgres',
        'PASSWORD' : '',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}
после настроек нужно создать таблицу в бд командами: manage.py makemigrations и manage.py migrate
Главный файл manage.py 
Сервер запускается командой manage.py runserver(нужно находиться в директории приложения).
При запуске через студию просто прописываем в параметрах запуска файла manage.py команду runserver.
Для корректной работы программы CSV файл должен содержать четыре записи соответствующие данным работника
пример:
Ivan	Ivanov	23021982	engineer
Anatoliy	Burcev	10101995	manager
Тесты на два апи метода находятся в папке "Test_Request".
