from django.shortcuts import render, render_to_response
from django.views.decorators import csrf
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect    #防止出现403问题
import json

def judge(request):
    return render(request, "judge/home.html")


@csrf_exempt
def getex(request):

    room = request.POST['roo']
    print(room)
    code=1
    sent="The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code"
    ex = json.dumps({"code":code, "sent":sent})
    return HttpResponse(ex)

@csrf_exempt
def send(request):
    room_num=request.POST['room_num']
    print(type(room_num))
    result=json.dumps(room_num)
    return HttpResponse(result)


def entity(request):
    return render(request, "judge/entity.html")

@csrf_exempt
def getchou(request):

    room = request.POST['roo']
    print(room)
    code=1
    sent="The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code"
    ex = json.dumps({"code":code, "sent":sent})
    return HttpResponse(ex)

@csrf_exempt
def sendchou(request):
    room_num=request.POST['room_num']
    print(type(room_num))

    result=json.dumps(room_num)
    return HttpResponse(result)


def concept(request):
    return render(request, "judge/concept.html")

@csrf_exempt
def getconcept(request):

    room = request.POST['roo']
    print(room)
    code=1
    sent="The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code"
    ex = json.dumps({"code":code, "sent":sent})
    return HttpResponse(ex)

@csrf_exempt
def sendconcept(request):
    room_num=request.POST['room_num']
    print(type(room_num))

    result=json.dumps(room_num)
    return HttpResponse(result)
