from main import models
from main.tools import myPaginator
from django.core import serializers
from vote_manage import settings
import os


class Common:
    def search(self, tableName, searchKey, searchValue):
        searchKey = searchKey + '__icontains'

        table = getattr(models, tableName, None)
        if table is None:
            return [{},]
        data = table.objects.filter(**{searchKey: searchValue})
        return data
    
    def getData(self, request, tableName, *args, **kwargs):
        searchKey = request.GET.get('search_key', None)
        searchValue = request.GET.get('search_value', None)
        pageNum = request.GET.get('page_num', 1)

        if searchKey:
            data = self.search(tableName, searchKey, searchValue)   
        else:
            table = getattr(models, tableName, None)
            data =[{},] if table is None else table.objects.all()

        maxSize = kwargs.get('maxsize', 10) 
        data, pageCount = myPaginator(data, maxSize, pageNum)
        data = serializers.serialize('json', data, use_natural_foreign_keys=True)
        return data, pageCount

    def uploadFile(self, request):
        # file = request.FILES.get('file', None)
        # fileObj = models.TempFile.objects.create(file=file)
        # return str(fileObj.file)

        file = request.FILES.get('file')
        category = request.POST.get('category', 'img') + '/'
        category = category.replace('.', '')
        f = open(os.path.join(settings.MEDIA_ROOT, category + file.name), 'wb')
    
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return category + file.name