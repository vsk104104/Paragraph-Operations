from django.shortcuts import render
from django.http import HttpResponse
import string
# Create your views here.
def text_display(request):
    f = open("D:\projects\practise\practise\Document.txt", "r+")
    st=''
    for i in f:
        st += '<p>'+i+'</p>'
    return HttpResponse(st)

def show_links(request):
    links =['https://docs.djangoproject.com/en/4.1/ref/contrib/admin/','https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7']
    st='' 
    for i in links:
        st += '<a href='+i+'> link </a>'
    return HttpResponse(st)

def show_page(request):
    param ={'name':'Bhadur','place':'Bihar','country':'India'}
    
    return render(request,'1.html',param)

def show_page2(request):
    return render(request,'2.html')

def para_opp(request):
    # get the text
    dict={}
    mytext = request.POST.get('text','This is default Value')
    r_p = request.POST.get('r_p','off')
    full_cap= request.POST.get('f_c','off')
    newln_rem = request.POST.get('n_r','off')
    ch_countr= request.POST.get('c_r','off')
    ex_space_remove = request.POST.get('s_r','off')
    print(r_p)
    # Analazing the Text
    dict['mytext']=mytext
    print(r_p =='on')
    if ch_countr=='on':
        strg=""
        for ch in mytext:
            if ch!=" " and ch!="\n" and ch!='\r': # when \n is transported \r(carriagr return) is used for transportation
                strg+=ch
        dict['char_count']=len(strg)
    
    if r_p =='on':
        punc = string.punctuation
        st=''
        for ch in mytext:
            if ch not in punc:
                st+=ch
        mytext=st
                
    if full_cap=='on':
        st=''
        for ch in mytext:
            st+=ch.upper()
        mytext=st    
    if newln_rem=='on':
        st=""
        st=' '.join(mytext.splitlines())
        mytext=st
        
    if ex_space_remove=='on':
        st=""
        for index,ch in enumerate(mytext):
            if not (mytext[index]==" " and mytext[index+1]==" " ):
                st+=ch
        mytext=st
    dict['anlayzed_text']=mytext   
    return render(request,'result.html',dict)
