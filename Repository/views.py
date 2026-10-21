
from django.shortcuts import render
from Repository.models import Questions
from Repository.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import Submissions
from Repository.serializers import SubmissionSerializer


class QuestionListCreateView(APIView):

    # GET: Retrieve all questions
    def get(self, request):
        qs = Questions.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(serializer_instance.data)

    # POST: Create a new question
    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Questions.objects.create(**actual_data)
            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(APIView):

    # GET: Retrieve one question
    def get(self, request, pk):
        qs = Questions.objects.get(id=pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(serializer_instance.data)

    # PUT: Update a question
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            Questions.objects.filter(id=pk).update(**actual_data)

            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)

    # DELETE: Delete a question
    def delete(self, request, pk):
        Questions.objects.filter(id=pk).delete()
        return Response({"message": "Question deleted successfully"})


class SubmissionsListCreateView(APIView):
    def get(self,request):
        qs=Submissions.objects.all()
        serializer_instance=SubmissionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Submissions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors) 


class SubmissionRetrieveUpdateDeleteView(APIView):

    # GET: Retrieve one submission
    def get(self, request, pk):
        qs = Submissions.objects.get(id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(serializer_instance.data)

    # PUT: Update a submission
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            Submissions.objects.filter(id=pk).update(**actual_data)

            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)

class EvaluateSubmissionView(APIView):
    def put (self, request, pk):
        form_data=request.data
        Submissions.objects.filter(id=pk).update(**form_data)

        return Response(data={
            "Message":"Updated..!"
        })





    # DELETE: Delete a submission
    def delete(self, request, pk):
        Submissions.objects.filter(id=pk).delete()
        return Response({"message": "Submission deleted successfully"})
