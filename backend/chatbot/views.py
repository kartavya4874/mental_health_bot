# Chat Views with DRF APIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .nlp_engine import detect_language_and_generate_reply

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({"error": "Message is required"}, status=400)
        reply = detect_language_and_generate_reply(message)
        return Response({"reply": reply})

