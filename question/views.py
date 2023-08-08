import json

from django.db import connection
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from .models import Question, Choice
from datetime import datetime


# Create your views here.
# def index(request):
#     print(json.loads(request.body))
#     return HttpResponse("Hello, World. You're at the polls index.")


def create_question(request):
    try:
        if not request.method == "POST":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # question = Question.objects.create(question_text=data.get("question_text"), pub_date=datetime.now())
        with connection.cursor() as cursor:
            cursor.execute("INSERT into question_question (question_text, pub_date) VALUES(%s, %s )",
                           [data.get("question_text"), datetime.now()])
            cursor.execute("SELECT * from question_question order by id desc limit 1")
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
        return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def retrieve_question(request):
    try:
        if not request.method == "GET":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # retrieve = Question.objects.get(id=data.get("id"))
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from question_question WHERE id=%s", [data.get("id")])
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
        return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def update_question(request):
    try:
        if not request.method == "PUT":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # question = Question.objects.get(id=data.get("id"))
        # question.question_text = data.get("question_text")
        # question.pub_date = datetime.now()
        # question.save()
        # return JsonResponse(model_to_dict(question))
        with connection.cursor() as cursor:
            cursor.execute("UPDATE question_question SET question_text=%s, pub_date=%s WHERE id=%s",
                           [data.get("question_text"), datetime.now(), data.get("id")])
            cursor.execute("SELECT * from question_question order by id desc limit 1")
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
            return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def delete_question(request):
    try:
        if not request.method == "DELETE":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # question = Question.objects.get(id=data.get("id"))
        # question.delete()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM question_question WHERE id=%s", [data.get("id")])
            return JsonResponse({"message": "question is deleted"})
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def create_choice(request):
    try:
        if not request.method == "POST":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # choice = Choice.objects.create(question_id=data.get("question"),
        #                                choice_text=data.get("choice_text"), votes=data.get("votes"))
        # return JsonResponse(model_to_dict(choice))
        with connection.cursor() as cursor:
            cursor.execute("INSERT into question_choice (choice_text, votes, question_id) VALUES(%s, %s, %s)",
                           [data.get("choice_text"), data.get("votes"), data.get("question")])
            cursor.execute("SELECT * from question_choice order by id desc fetch first 1 row only")
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
            return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def retrieve_choice(request):
    try:
        if not request.method == "GET":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # choice = Choice.objects.filter(question=data.get("question_id"))
        # data = [model_to_dict(x) for x in choice]
        # return JsonResponse(data, safe=False)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from question_choice WHERE id=%s", [data.get("id")])
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
            return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def update_choice(request):
    try:
        if not request.method == "PUT":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # choice = Choice.objects.get(id=data.get("id"))
        # choice.choice_text = data.get("choice_text")
        # choice.votes = data.get("votes")
        # choice.save()
        # return JsonResponse(model_to_dict(choice))
        with connection.cursor() as cursor:
            cursor.execute("UPDATE question_choice SET choice_text=%s, votes=%s WHERE id=%s",
                           [data.get("choice_text"), data.get("votes"), data.get("id")])
            cursor.execute("SELECT * FROM question_choice where id=%s", [data.get("id")])
            row = cursor.fetchone()
            column = [x[0] for x in cursor.description]
            result = dict(zip(column, row))
            return JsonResponse(result)
    except Exception as ex:
        return JsonResponse({"message": str(ex)})


def delete_choice(request):
    try:
        if not request.method == "DELETE":
            raise Exception("Method not allowed")
        data = json.loads(request.body)
        # choice = Choice.objects.get(id=data.get("id"))
        # choice.delete()
        # return JsonResponse(model_to_dict(choice))
        with connection.cursor() as cursor:
            cursor.execute("DELETE from question_choice where id=%s", [data.get("id")])
            return JsonResponse({"message": "choice is deleted"})
    except Exception as ex:
        return JsonResponse({"message": str(ex)})
