from django.http import JsonResponse
from rest_framework.views import APIView


class Request404(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'code': 404, 'msg': 'not found'})

    def post(self, request, *args, **kwargs):
        return JsonResponse({'code': 404, 'msg': 'not found'})
    
    def put(self, request, *args, **kwargs):
        return JsonResponse({'code': 404, 'msg': 'not found'})
    
    def delete(self, request, *args, **kwargs):
        return JsonResponse({'code': 404, 'msg': 'not found'})