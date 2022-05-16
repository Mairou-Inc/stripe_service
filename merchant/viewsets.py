from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework import generics
from merchant.models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def create_checkout_session(request, pk):
#     session = stripe.checkout.Session.create(
#     line_items=[{
#         'price_data': {
#         'currency': 'usd',
#         'product_data': {
#             'name': 'T-shirt',
#         },
#         'unit_amount': 2000,
#         },
#         'quantity': 1,
#     }],
#     mode='payment',
#     success_url='https://example.com/success',
#     cancel_url='https://example.com/cancel',
#     )
#     print(session.url)
#     return redirect(session.url, code=303)


# @api_view(['GET'])
# def get_item(request, pk):
#     renderer_classes = [TemplateHTMLRenderer]
#     return Response({'user': 1}, template_name='templates/item.html')



class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)

    def get(self, request):
        serializer = UserSerializer(User.objects.get(id=request.user.id))
        return Response(serializer.data)



# class ArticleView(viewsets.ModelViewSet):
#     serializer_class = stripeerializer
#     queryset = Article.objects.all()
#     # permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = (TokenAuthentication, BasicAuthentication)

#     def list(self, request, pk=None):
#         """Список статей"""
#         queryset = Article.objects.all()
#         serializer = stripeerializer(queryset, context={'request': request}, many = True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         """Конкретная статья по id"""
#         return super().retrieve(request)

# class CommentView(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#     # permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = (TokenAuthentication, BasicAuthentication)

#     def list(self, request, pk=None):

#         if pk:
#             """Список комментариев по id article"""
#             queryset = Comment.objects.filter(article_id=pk)
#         else:   
#             """Список комментариев"""

#             queryset = Comment.objects.all()
#         serializer = CommentSerializer(queryset, context={'request': request}, many = True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         """Конкретный комментарий по id"""
#         return super().retrieve(request)


#     def create(self, request):
#         try:
#             queryset = Comment.objects.create(comment_id=request.data['comment'])
#             serializer = CommentSerializer(queryset, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return super().create(request)

