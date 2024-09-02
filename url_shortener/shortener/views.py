from django.shortcuts import redirect
from django.http import JsonResponse
from .models import URLMapping
import random
import string

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_code = generate_short_code()
        URLMapping.objects.create(long_url=long_url, short_code=short_code)
        return JsonResponse({'short_url': f'http://localhost:8000/{short_code}'})

def redirect_to_long_url(request, short_code):
    try:
        url_mapping = URLMapping.objects.get(short_code=short_code)
        return redirect(url_mapping.long_url)
    except URLMapping.DoesNotExist:
        return JsonResponse({'error': 'URL not found'}, status=404)



