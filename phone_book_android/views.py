from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, get_token
from django_demo_list.utils import get_int_value
from phone_book_android.models import Phone


@require_http_methods(['GET', 'POST'])
def get_my_token(request):
    token = get_token(request=request)
    return JsonResponse({'token':token}, content_type='application/json', safe=False)


def get_phone_detail(records):
    phone_list = []
    for record in records:
        phone_list.append({
            'id': record.id,
            'name':record.name,
            'phone': record.phone,
            'image': record.image.url if record.image else ''
        })
    return phone_list


@require_http_methods(['GET'])
def get_phone_list(request):
    results = {
        'phone_list': [],
        'total': 0,
    }
    records = Phone.objects.all()
    results['phone_list'] = get_phone_detail(records)
    results['total'] = len(records)
    return JsonResponse(results)


@require_http_methods(['GET'])
def get_phone_by_id(request, id):
    results = {}
    records = Phone.objects.filter(id=id)
    if len(records) > 0:
        results = get_phone_detail(records)[0]
    return JsonResponse(results)


@require_http_methods(['POST'])
def add_phone(request):
    results = {
        'status': 'error',
        'message': '',
    }
    name = request.POST.get('name', None)
    phone = request.POST.get('phone', None)
    image = request.FILES.get('image', None)
    if not name or not phone:
        results['message'] = 'Lack of name or phone field.'
        return JsonResponse(results)
    try:
        record = Phone(name=name,phone=phone,image=image)
        record.save()
        results['status'] = 'success'
    except Exception as e:
        results['message'] = str(e)
    return JsonResponse(results)


@require_http_methods(['POST'])
def delete_phone(request):
    results = {
        'status': 'error',
        'message': '',
    }
    phone_id = get_int_value(request.POST.get('id', None), None)
    if not phone_id:
        results['message'] = 'Invalid phone id field.'
    records = Phone.objects.filter(id=phone_id).delete()
    results['status'] = 'success'
    return JsonResponse(results)


@require_http_methods(['POST'])
def update_phone(request):
    results = {
        'status': 'error',
        'message': '',
    }
    phone_id = get_int_value(request.POST.get('id', None), None)
    if not phone_id:
        results['message'] = 'Invalid phone id field.'
    name = request.POST.get('name', None)
    phone = request.POST.get('phone', None)
    image = request.FILES.get('image', None)
    
    try:
        record = Phone.objects.get(id=phone_id)
    except Exception as e:
        results['message'] = str(e)
        return JsonResponse(results)
    if name:
        record.name = name
    if phone:
        record.phone = phone
    if image:
        record.image = image
    try:
        record.save()
        results['status'] = 'success'
    except Exception as e:
        results['message'] = str(e)
    return JsonResponse(results)
