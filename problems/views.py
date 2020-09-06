from django.shortcuts import render, redirect
from .models import Problem


def home(request):
    problem = Problem.objects.get(pk=1)
    context = {
        'problem' : problem,
    }
    return render(request, 'problems/home.html', context)


def correct(request, pk):
    problem = Problem.objects.get(pk=pk)
    context = {
        'problem' : problem,
    }
    return render(request, 'problems/correct.html', context)


def foul(request):
    return render(request, 'problems/foul.html')


def detail(request, pk):
    
    problem = Problem.objects.get(pk=pk)
    context = {
        'problem' : problem,
    }

    if pk == 1:
        return render(request, 'problems/detail.html', context)
    elif request.method == 'POST':
        p_problem = Problem.objects.get(pk=pk-1)
        ans = request.POST.get('answer')
        if ans == p_problem.answer:
            return render(request, 'problems/detail.html', context)
        else:
            return redirect('problems:detail', problem.pk-1)
    else:
        return render(request, 'problems/foul.html')


def check(request, pk):
    problem = Problem.objects.get(pk=pk)
    ans = request.POST.get('answer')
    if request.method == 'POST':
        return redirect('problems:correct', problem.pk+1)
    else:
        return render(request, 'problems/foul.html')
