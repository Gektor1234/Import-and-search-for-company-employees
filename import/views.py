from rest_framework.response import Response
from rest_framework.views import APIView
import csv
from .models import Workers
from .serializiers import WorkersSerializers

class WorkersViewByName(APIView):             #эндпоинт для поиска сотрудника по имени или фамилии
    def get(self, request, name_or_surname):
        search_by_name = Workers.objects.filter(name=name_or_surname)
        search_by_surname = Workers.objects.filter(surname=name_or_surname)
        seriliz_by_name = WorkersSerializers(search_by_name,many=True)
        seriliz_by_surname = WorkersSerializers(search_by_surname,many=True)
        data_by_name = seriliz_by_name.data[:]
        data_by_surname = seriliz_by_surname.data[:]
        return Response(data_by_name or data_by_surname)



class ImportWorkers(APIView):               # парсинг данных из csv файла и загрузка в постгрес
    def post(self, request):
        with open(r"C:\Users\User\Desktop\test_case.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for wood in row:
                    wood = wood.replace(';',' ')
                    data = wood.split()
                    created = Workers.objects.get_or_create(
                    name = (data[0]),
                    surname = (data[1]),
                    date_of_birth = (int(data[2])),
                    position = (data[3]),
                )
        return Response({"result":"ok"})

