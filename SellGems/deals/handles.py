from django.contrib import messages
from deals.models import Deal
from django.http import HttpResponseBadRequest, HttpResponse
import csv, io


def handle_uploaded_file(request):
    file = request.FILES['file']

    try:
        data_set = file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        csv_reader = csv.reader(io_string, delimiter=',')

        for line in csv_reader:
            # print(line)
            Deal.objects.create(
                customer=line[0],
                item=line[1],
                total=line[2],
                quantity=line[3],
                date=line[4]
            )
        return HttpResponse('файл был обработан без ошибок')
    except:
        return HttpResponseBadRequest('в процессе обработки файла произошла ошибка')

