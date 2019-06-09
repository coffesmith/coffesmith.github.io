from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext'] #홈의 풀텍스트를 가져오는데 가져오는 것을 텍스트라는 변수를 정의해준다.
    words = text.split() #우리가 작성 한 원문을 공백 기준으로 나눠서 리스트로 만들어 준다.
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()}) #왼쪽 키값, 오른쪽 밸류 세번째 인자 사전형 객체