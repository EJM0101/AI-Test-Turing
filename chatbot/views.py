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
            try:
                hf_response = requests.post(
                    'https://api-inference.huggingface.co/models/gpt2',
                    headers={
                        'Authorization': f"Bearer {os.getenv('HF_API_KEY', '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')}",
                        'Content-Type': 'application/json',
                    },
                    json={"inputs": user_msg}
                )

                # Tente de décoder la réponse
                data = hf_response.json()

                # Vérifie si c’est une liste avec texte généré
                if isinstance(data, list) and "generated_text" in data[0]:
                    reply = data[0]['generated_text']
                else:
                    reply = f"[Réponse inattendue Hugging Face : {data}]"

            except Exception as e:
                reply = f"[Erreur API Hugging Face : {str(e)} / Réponse brute : {hf_response.text}]"

        return JsonResponse({'reply': reply})