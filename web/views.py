import logging

from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

    @request_mapping("/iot", method="get")
    def iot(self, request):
        id = request.GET['id'];
        temp = request.GET['temp'];
        el = request.GET['el'];
        #---------------------------------
        el_logger = logging.getLogger('el_file');
        el_logger.debug(id+','+temp+','+el);
        #---------------------------------

        return render(request, 'ok.html');


    @request_mapping("/login", method="get")
    def login(self,request):
        context = {
            'center':'login.html'
        };
        return render(request,'home.html', context);

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self,request):
        # id, pwd를 프로그램을 확인한다.
        id = request.POST['id']; #post방식이므로 post[]방식으로 가져온다.
        pwd = request.POST['pwd']; #post방식이므로 post[]방식으로 가져온다.
        # id를 이용하여 DB에 사용자 정보를 조회
        # id 정보가 존재하지 않으면 로그인 실패
        # id가 존재하면 PWD 검사
        # PWD가 틀리면 로그인 실패
        # PWD가 맞으면 로그인 성공
        context={};


        try:
            cust = Cust.objects.get(id=id);
            if pwd==cust.pwd:
                request.session['sessionid']=cust.id;
                request.session['sessionname']=cust.name;
                context['center']='loginok.html';
            else:
                raise Exception;

        except:
            context['center']='loginfail.html';



        #
        # if (id =='qq') and (pwd=='11'):
        #     request.session['sessionid']=id;
        #     context['center']='loginok.html';
        # else:
        #     context['center']='loginfail.html';
        # 서버에 로그인을 했다는 정보를 심어놓는다? 저장한다.
        # 성공 페이지로 이동

        return render(request,'home.html', context);

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return render(request, 'home.html');

    @request_mapping("/register", method="get")
    def register(self,request):
        context = {
            'center':'register.html'
        };
        return render(request,'home.html', context);

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self,request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        print(id,pwd, name);
        context={};
        try:
            Cust.objects.get(id=id);
            context['center'] = 'registerfail.html'
        except:
            Cust(id=id, pwd=pwd, name=name).save();
            context['center'] = 'registerok.html'
            context['rname'] = name;

        return render(request,'home.html', context);