from django.http import JsonResponse
from rest_framework.views import APIView


class Request404(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 404, 'msg': 'not found'}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 404, 'msg': 'not found'}
        return JsonResponse(ret)