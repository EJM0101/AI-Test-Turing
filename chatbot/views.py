import random
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

FAKE_REPLIES = [
    "Bonne question ! Qu'en penses-tu, toi ?",
    "Je suis d'accord, c’est assez complexe à dire.",
    "Tu poses toujours des choses intéressantes...",
]

@csrf_exempt
def index(request):
    return render(request, 'chatbot/index.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        user_msg = request.POST.get('message')
        role = request.POST.get('role')

        if role == 'fake':
            reply = random.choice(FAKE_REPLIES)
        else:
            try:
                response = requests.post(
                    "https://chat.tune.app/api/chat",
                    headers={"Content-Type": "application/json"},
                    json={"messages": [{"role": "user", "content": user_msg}]}
                )
                data = response.json()
                reply = data["message"]
            except Exception as e:
                reply = f"[Erreur TuneGPT : {str(e)} / Réponse : {response.text}]"

        return JsonResponse({'reply': reply})