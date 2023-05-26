from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, UserHackathon, Submission
from .serializers import HackathonSerializer, UserHackathonSerializer, SubmissionSerializer
from .permissions import IsAuthorizedUser, IsAuthorizedUserExceptPost

class HackathonListCreateAPIView(APIView):
    permission_classes = [IsAuthorizedUserExceptPost]

    def get(self, request):
        hackathons = Hackathon.objects.all()
        serializer = HackathonSerializer(hackathons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HackathonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HackathonRetrieveUpdateAPIView(APIView):
    permission_classes = [IsAuthorizedUser]

    def get_hackathon(self, pk):
        try:
            return Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        hackathon = self.get_hackathon(pk)
        serializer = HackathonSerializer(hackathon)
        return Response(serializer.data)

    def put(self, request, pk):
        hackathon = self.get_hackathon(pk)
        serializer = HackathonSerializer(hackathon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserHackathonListAPIView(APIView):
    permission_classes = [IsAuthorizedUser]

    def get(self, request):
        user_hackathons = UserHackathon.objects.filter(user=request.user)
        serializer = UserHackathonSerializer(user_hackathons, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserHackathonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserSubmissionListAPIView(APIView):
    permission_classes = [IsAuthorizedUser]

    def get(self, request, hackathon_id):
        submissions = Submission.objects.filter(user=request.user, hackathon_id=hackathon_id)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request, hackathon_id):
        serializer = SubmissionSerializer(data=request.data)
        try:
            register = UserHackathon.objects.get(user=request.data["user"], hackathon=request.data["hackathon"])
        except UserHackathon.DoesNotExist:
            return Response("User is not registered for the specified hackathon.", status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(user=request.user, hackathon_id=hackathon_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)