from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt



from todo.models import Todo, Chats
from todo.ai_response import get_response

# Create your views here.

def todo_home(request):
    todos = Todo.objects.all()
    return render(request, 'todo/home.html',{"todos":todos})

@require_http_methods(['POST'])
@csrf_exempt
def add_todo(request):
    todo = None
    title = request.POST.get("title","")

    if title:
        todo = Todo.objects.create(title=title)

    return render(request, 'todo/partials/add_todo.html', {'todo': todo})


@require_http_methods(['PUT'])
@csrf_exempt
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    return render(request, 'todo/partials/add_todo.html', {'todo': todo})

@require_http_methods(['DELETE'])
@csrf_exempt
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()

@require_http_methods(['POST', 'PUT'])
@csrf_exempt
def chat_add(request):
    chat = None
    prompt = request.POST.get("prompt")

    if prompt:
        chat= Chats.objects.create(prompt=prompt)

    response = get_response(prompt)
    chat.response = response
    chat.save()
    
    return HttpResponse()

def chats(request):
    chats = Chats.objects.all()
    for chat in chats:
        print(chat.prompt)
    return render(request, 'todo/partials/chats.html', {'chats': chats})




def delete_chats(request):
    chats = Chats.objects.all()
    number_of_chats = len(chats)
    print(number_of_chats)

    for chat in chats:
        record = Chats.objects.get(pk=chat.pk)
        record.delete()

    return HttpResponse()
