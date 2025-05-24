import os
import random
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

FAKE_REPLIES = [
    "Bonne question ! Qu'en penses-tu, toi ?",
    "Je suis d'accord, c’est assez complexe à dire.",
    "Je t’avoue que je ne sais pas trop.",
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
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://ton-site.com",  # facultatif
                        "X-Title": "TuringBot",  # nom de ton app
                    },
                    json={
                        "model": "openai/gpt-3.5-turbo",
                        "messages": [{"role": "user", "content": user_msg}],
                        "temperature": 0.7,
                    }
                )
                data = response.json()
                reply = data["choices"][0]["message"]["content"]
            except Exception as e:
                reply = f"[Erreur OpenRouter : {str(e)}]"

        return JsonResponse({'reply': reply})