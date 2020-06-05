# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello")
#
# def navigation(request):
#     return HttpResponse('''
#     <a href="https://www.google.co.in" target="_blank"> Click to go to Google </a></br>
#     <a href="https://www.yahoo.co.in" target="_blank"> Click to go to Yahoo </a></br>
#     <a href="https://www.rediff.com" target="_blank"> Click to go to Rediff </a></br>
#     <a href="https://www.santabanta.com" target="_blank"> Click to go to SantaBanta </a> ''')
#
#
# # def about(request):
# #     return HttpResponse("Hello Bro from about")
#
# def about(request):
#     with open("xyx.txt") as f:
#         a = f.read()
#         return HttpResponse(a)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    #return HttpResponse("Home")

def analyzer(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''/[-[\]{}<>()*+?.,\\^$|#\]/,;'"\\$&"'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Puntuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Removed', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
             if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'New Live Removed', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if charcounter == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose':'Total character count', 'analyzed_text':analyzed}
        # return render(request, "analyze.html", params)
    #
    # else:
    #     return HttpResponse("Error")

    return render(request, "analyze.html", params)


