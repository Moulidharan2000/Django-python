import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, Choice
from datetime import datetime


# Create your views here.
def index(request):
    print(json.loads(request.body))
    return HttpResponse("Hello, World. You're at the polls index.")


def create_question(request):
    try:
        if not request.method == "POST":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        question = Question.objects.create(question_text=data.get("question_text"), pub_date=datetime.now())
        return JsonResponse(model_to_dict(question))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def retrieve_question(request):
    try:
        if not request.method == "GET":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        retrieve = Question.objects.get(id=data.get("id"))
        return JsonResponse(model_to_dict(retrieve))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def update_question(request):
    try:
        if not request.method == "PUT":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        question = Question.objects.get(id=data.get("id"))
        question.question_text = data.get("question_text")
        question.pub_date = datetime.now()
        question.save()
        return JsonResponse(model_to_dict(question))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def delete_question(request):
    try:
        if not request.method == "DELETE":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        question = Question.objects.get(id=data.get("id"))
        question.delete()
        return JsonResponse({"message": "question is deleted"})
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def create_choice(request):
    try:
        if not request.method == "POST":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        choice = Choice.objects.create(question_id=data.get("question"), choice_text=data.get("choice_text"), votes=data.get("votes"))
        return JsonResponse(model_to_dict(choice))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def retrieve_choice(request):
    try:
        if not request.method == "GET":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        choice = Choice.objects.filter(question=data.get("question_id"))
        data = [model_to_dict(x) for x in choice]
        return JsonResponse(data, safe=False)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def update_choice(request):
    try:
        if not request.method == "PUT":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        choice = Choice.objects.get(id=data.get("id"))
        choice.choice_text = data.get("choice_text")
        choice.votes = data.get("votes")
        choice.save()
        return JsonResponse(model_to_dict(choice))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def delete_choice(request):
    try:
        if not request.method == "DELETE":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        choice = Choice.objects.get(id=data.get("id"))
        choice.delete()
        return JsonResponse(model_to_dict(choice))
    except Exception as ex:
        return JsonResponse({"message": str(ex)})
