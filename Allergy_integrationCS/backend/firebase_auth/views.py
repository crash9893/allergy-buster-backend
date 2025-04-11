from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import firebase_admin
from firebase_admin import auth

@csrf_exempt
def verify_firebase_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_token = data.get('idToken')

            if not id_token:
                return JsonResponse({'error': 'Missing ID token'}, status=400)

            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']

            return JsonResponse({'message': 'Token verified', 'uid': uid})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
