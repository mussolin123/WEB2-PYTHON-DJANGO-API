from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Aluno
from .serializers import AlunoSerializer
import face_recognition
from django.http import JsonResponse, HttpResponse

# View para a página inicial
def home(request):
    return HttpResponse("Bem-vindo ao sistema de reconhecimento facial!")

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
@permission_classes([AllowAny])
def reconhecer_aluno(request):
    if 'foto' in request.FILES:
        foto_enviada = request.FILES['foto']
        foto_enviada_imagem = face_recognition.load_image_file(foto_enviada)
        encodings_foto_enviada = face_recognition.face_encodings(foto_enviada_imagem)

        if not encodings_foto_enviada:
            return JsonResponse({'erro': 'Nenhuma face detectada'}, status=400)

        for aluno in Aluno.objects.all():
            if aluno.features:
                features_aluno = eval(aluno.features)
                matches = face_recognition.compare_faces([features_aluno], encodings_foto_enviada[0])

                if matches[0]:
                    return JsonResponse({'matricula': aluno.matricula, 'nome': aluno.nome})

        return JsonResponse({'erro': 'Aluno não reconhecido'}, status=404)
    else:
        return JsonResponse({'erro': 'Nenhuma foto foi enviada'}, status=400)
