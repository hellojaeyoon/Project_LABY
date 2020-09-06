from django.shortcuts import render, redirect

# Create your views here.

def problem1(request):
    return render(request, 'problems/problem1.html')


def problem2(request):
    return render(request, 'problems/problem2.html')


def check(request):
    ans = request.POST.get('answer1')

    if ans == 'yoga':
        return redirect('problems:problem2')
    else:
        return redirect('problems:problem1')


def check2(request):
    ans = request.POST.get('answer2')

    if ans == 'tetris':
        return redirect('problems:problem3')
    else:
        return redirect('problems:problem2')


def check3(request):
    ans = request.POST.get('answer3')

    if ans == '잠바핫바':
        return redirect('problems:endpage')
    else:
        return redirect('problems:problem3')

def problem3(request):
    return render(request, 'problems/problem3.html')


def endpage(request):
    return render(request, 'problems/endpage.html')