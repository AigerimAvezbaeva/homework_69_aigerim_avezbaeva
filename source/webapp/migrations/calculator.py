import json
from django.http import HttpResponse, JsonResponse

def add(request):
    data = {
        'A': 123,
        'B': 543}
    a = data['A']
    b = data['B']
    try:
        answer = a + b
        answer_as_json = json.dumps({'answer': answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        return response
    except:
        return JsonResponse({'error': 'Неверные данные'}, status=400)


def subtract(request):
    data = {
        'A': 123,
        'B': 543}
    a = data['A']
    b = data['B']
    try:
        answer = a - b
        answer_as_json = json.dumps({'answer': answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        return response
    except:
        return JsonResponse({'error': 'Неверные данные'}, status=400)


def multiply(request):
    data = {
        'A': 123,
        'B': 543}
    a = data['A']
    b = data['B']
    try:
        answer = a * b
        answer_as_json = json.dumps({'answer': answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        return response
    except:
        return JsonResponse({'error': 'Неверные данные'}, status=400)


def divide(request):
    data = {
        'A': 123,
        'B': 0
    }
    a = data['A']
    b = data['B']
    if b == 0:
        answer = {"error": "Division by zero!"}
        return JsonResponse(answer, status=400)
    try:
        answer = a / b
        answer_as_json = json.dumps({'answer': answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        return response
    except:
        return JsonResponse({'error': 'Неверные данные'}, status=400)
