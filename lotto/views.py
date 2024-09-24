from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import GuessNumbers

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # querySet이라는 타입으로 반환해줌
    return render(request, 'lotto/default.html', {'lottos': lottos})


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #filled form

        if form.is_valid(): #user가 입력한 값이 유효한지 검사
            lotto = form.save(commit=False) #commit=False로 하면 저장은 할건데 DB에 아직 저장 확정은 아닌 상태
            # form.save()를 하면 저장된 행 전체 반환받을 수 있음(=GuessNumbers 클래스의 객체변수)
            lotto.generate()

            return redirect('index')
    else:
        form = PostForm()

        return render(request, 'lotto/form.html', {'form': form})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>hello</h1>")


def detail(request, lottoKey): # request는 path함수가 넘겨주는 http 요청을 받아내는 것
    lotto = GuessNumbers.objects.get(id=lottoKey)

    return render(request, 'lotto/detail.html', {'lotto':lotto})