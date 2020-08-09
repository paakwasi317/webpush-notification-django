import json

from django.conf import settings
# from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from webpush import send_user_notification
from Users.models import Users as User


@require_GET
# @csrf_exempt
def home(request):
    # webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = "BG2Kb97s399EpFuQJvxKj5AaNR7HvThUGwTx8K9GZ_suy-Lk8n0CaFhhilVZhH7WtibrSGD04kSNocKvFXiKbcM"
    print(type(vapid_key))
    print(request)
    user = request.user
    print(user)
    return render(request, 'home.html', {user: user, 'vapid_key': vapid_key})
    # data = {"user": user.id, "vapid_key": vapid_key}
    # return JsonResponse(status=200, data=data)

@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data and 'body' not in data and 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']

        # print(user_id)

        user = get_object_or_404(User, pk=user_id)
        print(user)

        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})

    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})
