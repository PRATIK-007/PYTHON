from urllib.request import urlopen
from django.http import HttpResponse
from django.shortcuts import render
from .models import Word_cal
import itertools
import bs4
def base(request):
	return render(request,'base.html')

def frequency(request):
	return render(request,'frequency.html')

def result(request):

    model = Word_cal

    url = request.POST['url_p']

    mo = model.objects.filter(url_l =url)
    print(type(mo))
    for i in mo:
        print(i)
    if not mo:

        common_words = "a about all also and as at be because but by can come could day do even find first for from get give go have " \
             "he her here him his how I if in  into it its just know like look make man many me more my new no not now of " \
             "on one only or other our out people say see she so some take tell than that the their them then there these " \
             "they thing think this those time to two up use very want way we well what when which who will with would year" \
             " you your 1 2 3 4 5 6 7 8 9 >>> = "
        common_words_list = common_words.split(" ")
        str = ""
        html = urlopen(url).read()
        soup = bs4.BeautifulSoup(html,features="html.parser")

        for script in soup(["script", "style"]):
            script.decompose()
            # print(script,"\n\n\n\n\n\n\n\n")


        strips = list(soup.stripped_strings)
        # print(strips[:])

        for i in strips:
            str = str + i + " "

        str = [x.replace("\r\n","") for x in str]

        special_char = "!@#$%^&*()_<>{}[]=/*-+/?|,.:;''1234567890"
        str1 = ''.join([i for i in str if ((i.isalpha() or " " ) and (i not in special_char) )  ] )
        str1.replace(""" \n """," ")
        print(str1)

        worlist = str1.split(' ')
        # print(str1)

        worddict = {}

        for i in worlist:
            if i not in common_words_list:
                if i in worddict:
                    worddict[i]+=1
                else:
                    worddict[i]=1


        worddict1 = {k: v for k, v in sorted(worddict.items(), key=lambda item: item[1],reverse=True)}
        worddict2  = dict(itertools.islice(worddict1.items(), 10))

        for key,item in worddict2.items():
            b = model(url_l=url, words=key, count=item)
            b.save()

        return render(request,'result.html',{ 'len' :"PROCESSED" , 'worly' : worddict2 })

    else:
        print("from database")
        lw = list(mo.values())
        print(lw)
        print(lw[:5][0]['words'])
        worddi = {}
        for i in range(0,9):
            # print(lw[2]['words'],":  lw")
            # print(lw[:5]['words'])



            worddi[lw[i]['words']] = lw[i]['count']

        print(worddi)
        worddict3 = {k: v for k, v in sorted(worddi.items(), key=lambda item: item[1], reverse=True)}
        worddict4 = dict(itertools.islice(worddict3.items(), 10))
        return render(request, 'result.html', {'len': "From Database", 'worly': worddict4})







