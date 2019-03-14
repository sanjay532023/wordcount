from django.http import HttpResponse
from django.shortcuts import render, redirect
import operator


def homepage(request):
    #return HttpResponse('<h1>Welcome to Homepage</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Enter Text To Count :'})


def user_login(request):
    #return HttpResponse('<h1> Contact page</h1></br> This is contact page')
    # uname = "sanjay"
    # psword = "sanjay"
    # #login = {}
    # name = request.POST['uname']
    # pword = request.POST['pword']
    # if name == uname and pword == psword:
    return render(request, 'user_login.html', {'name': 'Hi this is login page :', 'Welcome': "Welcome to login page"})
    # else:
    #     return HttpResponse('You have enter a wrong password')
    #

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_length = len(word_list)

    worddict = {}
    for word in word_list:
        if word in worddict:
            # increase value by 1
            worddict[word] += 1
        else:
            #add to the word dosctinary.
            worddict[word] = 1
    sorted_list = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText': data, 'word': list_length, 'wordDictionary': sorted_list})


def about_us(request):
    return render(request, 'about_us.html')