from django.urls import path
from .viewsets import *
from . import views

# from rest_framework.routers import SimpleRouter



# routes = SimpleRouter()

# # AUTHENTICATION
# routes.register('auth/login', LoginViewSet, basename='auth-login')
# routes.register('auth/register', RegistrationViewSet, basename='auth-register')
# routes.register('auth/refresh', RefreshViewSet, basename='auth-refresh')


urlpatterns = [
    path('user/', UserDetailView.as_view()),

    # path('api/article/', ArticleView.as_view({'post': 'create'})),
    # path('api/stripe/', ArticleView.as_view({'get': 'list'})),


    # path('buy/<str:pk>/', create_checkout_session),
    # path('item/<str:pk>/', get_item),


    path('buy/<str:pk>/', views.create_checkout_session),
    path('item/<str:pk>/', views.get_item),



    # path('item/<str:pk>/', ArticleView.as_view({'get': 'retrieve'})),

    # path('api/comment/', CommentView.as_view({'post': 'create'})),
    # path('api/comments/', CommentView.as_view({'get': 'list'})),
    # path('api/comments/<str:pk>/', CommentView.as_view({'get': 'list'})),
    # path('api/comment/<str:pk>/', CommentView.as_view({'get': 'retrieve'})),


    # *routes.urls
]