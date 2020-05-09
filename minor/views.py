from django.http import JsonResponse

def index(request):
    responseData = {
        'name': 'Test Response',
    }

    return JsonResponse(responseData)