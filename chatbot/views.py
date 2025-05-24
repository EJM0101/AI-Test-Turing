import random
import requests
import os
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
            hf_response = requests.post(
                'https://api-inference.huggingface.co/models/gpt2',
                headers={{
                    'Authorization': f"Bearer {os.getenv('HF_API_KEY', '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')}",
                    'Content-Type': 'application/json',
                }},
                json={{"inputs": user_msg}}
            )
            data = hf_response.json()
            reply = data[0]['generated_text'] if isinstance(data, list) else "[Erreur GPT]"

        return JsonResponse({{'reply': reply}})
