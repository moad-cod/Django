import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body 
    print(request.GET) #url query params
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers) # request.META
    data['content_type'] = request.content_type
    return JsonResponse(data)