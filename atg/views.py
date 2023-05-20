from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from simplet5 import SimpleT5
import torch
from chats.models import ChatMessage

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SimpleT5()
model.load_model("t5", "./savedmodels/simplet5-epoch-79-train-loss-0.0741-val-loss-6.0122")

def index(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    chat_messages = ChatMessage.objects.all()

    if request.method == 'POST':
        text = request.POST.get('text')
        prediction = model.predict(text)
        prediction = str(prediction)

        chat_message = ChatMessage(sender='User', message=text)
        chat_message.save()

        chat_message = ChatMessage(sender='Chatbot', message=prediction)
        chat_message.save()

        context = {'prediction': prediction, 'chat_messages': chat_messages}
        return render(request, 'index.html', context)

    context = {'chat_messages': chat_messages}
    return render(request, 'index.html', context)
