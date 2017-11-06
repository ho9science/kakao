from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from quickstart.MyApp import MessageClass, KeyboardClass
from rest_framework.parsers import JSONParser

# from konlpy.tag import Mecab
from .models import Kknouns, Klog

from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        # Any URL parameters get passed in **kw
        myClass = MessageClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        get_arg1 = request.POST.get("arg1",None)
        get_arg2 = request.data
        
        # mecab = Mecab()

        print(get_arg2)
        get_arg1 = get_arg2.get('content')
        if get_arg1=="welcome yapp":
            myClass = MessageClass(get_arg1, *args, **kw)
            result = myClass.do_work()
            response = Response(result, status=status.HTTP_200_OK)
            return response
        #get_arg1 = mecab.nouns(get_arg1)
        # local start
        get_arg1 = ['실력','개발','요구']
        #local end
        kkma_list=get_arg1
        return_value = []
        temp_id = []
        i = 0
        query = Q()
        answer = "no answer"
        for keyword in kkma_list:
            if i==0:
                return_value = Kknouns.objects.values_list('id',flat=True).filter(indexing__contains=keyword)
            else:
                return_value = Kknouns.objects.values_list('id',flat=True).filter(query, indexing__contains=keyword)
            print("return:{}".format(return_value))
            if return_value:
                temp_id=return_value
                queries = [Q(id=value) for value in return_value]
                query = queries.pop()
                for item in queries:
                    query |= item
                print("query:{}".format(query))

                
            i=i+1
        # print("mecab:{}".format(temp_id))
        if temp_id:
            for gold in temp_id:
                answer1 = Kknouns.objects.values_list('answer').filter(id=gold).first()
                print(gold)
                answer = ''.join(str(e) for e in answer1)
                break
        
        Klog.object.create()

        myClass = MessageClass(answer, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)

        return response

class KeyboardView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        # Any URL parameters get passed in **kw
        myClass = KeyboardClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response