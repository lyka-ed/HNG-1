from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def bio(request):
    if request.method == 'GET':
        return Response({"slackUsername": "lykaokpos",
        "backend": True,
        "age": 24,
        "bio": "My name is Glory but I rather be called Lyka. I'm a big time foodie. Googling, YouTube and reading of articles from daily devs are what I enjoy doing effortlessly. I love playing chess even thou I ain't a pro yet."
    })
                        
                        


                    