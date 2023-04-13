import json
from django.http import HttpResponse, JsonResponse

def calculator(request):
    global answer
    if request.body:
        data = json.loads(request.body)
        print(data)
        a = data['A']
        b = data['B']
        if b == 0:
            answer = {"error": "Division by zero!"}
            return JsonResponse(answer, status=400)
        try:
            match request.path:
                case '/add/':
                    answer = a + b
                case '/subtract/':
                    answer = a - b
                case '/multiply/':
                    answer = a * b
                case '/divide/':
                    answer = a / b
            answer_as_json = json.dumps({'answer': answer})
            response = HttpResponse(answer_as_json, content_type='application/json')
            return response
        except:
            return JsonResponse({'error': 'Неверные данные'}, status=400)

