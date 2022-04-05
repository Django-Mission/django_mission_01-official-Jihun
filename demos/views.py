from lib2to3.refactor import get_all_fix_names
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def calculator(request):
    # return HttpResponse('계산기 기능 시작입니다.')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # num1 = int(num1)
    # num2 = int(num2)

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2);
    elif operators == '/':
        result = int(num1) / int(num2);
    else:
        result = 0

    # 3. 응답


    return render(request, 'calculator.html', {'result':result})



def lottery(request):

    # lotto_list = []
    # for i in range(7):
    #     while True:
    #         tmp = random.randint(1,45)
    #         if(tmp not in lotto_list):
    #             lotto_list.append(tmp)
    #             break
    
    # lotto_list = sorted(lotto_list)


    return render(request, 'lottery.html')

def lottery_result(request):
    games_num = request.GET.get('games')
    result = []

    for i in range(int(games_num)):
        lotto_list = []
        for j in range(7):
            while True:
                tmp = random.randint(1,45)
                if(tmp not in lotto_list):
                    lotto_list.append(tmp)
                    break
        
        lotto_list = sorted(lotto_list)
        result.append(lotto_list)
    
    print(result)
    
    

    return render(request, 'lottery_result.html', {'games_num' : games_num, 'result' : result })

