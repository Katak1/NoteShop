from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


def index(request):
    permission_classes = [IsAuthenticated]

    return render(request, 'chat/index.html')

def room(request, room_name):
    permission_classes = [IsAuthenticated]

    return render(request, 'chat/room.html', {
        'room_name': room_name
    })