from django.shortcuts import render
from django.http import HttpResponse
import random
import numpy as np
from game.models import all_results

# Create your views here.

def index(request):
    try:
        print(request.GET)
        answer=request.POST['answer']
        number=np.floor(random.random()*9)
        if 0<=number<=2:
            computer_answer='rock'
        elif 3<=number<=5:
            computer_answer='paper'
        else:
            computer_answer='scissors'
        
        if answer=='rock':
            if computer_answer=='rock':
                result='Draw!'
            elif computer_answer=='paper':
                result='You Lost!'
            else:
                result='You Win!'
        elif answer=='paper':
            if computer_answer=='rock':
                result='You Win!'
            elif computer_answer=='paper':
                result='Draw!'
            else:
                result='You Lost!'
        else:
            if computer_answer=='rock':
                result='You Lost!'
            elif computer_answer=='paper':
                result='You Win!'
            else:
                result='Draw!'
        result += " - David rocks!"
        res=all_results(computer=computer_answer,person=answer,result=result)
        res.save()

        data=all_results.objects.all()
        #print(data is defined)


    except:
        answer=None
        result=None
        computer_answer=None
        data=all_results.objects.all()
    return render(request,'index.html',dict([('result',result),('computer_answer',computer_answer),('person_answer',answer),('data',data)]))
    #return HttpResponse('sss')