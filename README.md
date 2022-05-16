# stripe-service

Сборка:
```
docker-compose up 
```

При необходимости наличия бызы Postgresql, раскомменить настройку DATABASES в settings.py

При желании можно использовать shell скрипты в корне проекта


### Список urls:

```
buy/<str:pk>/', views.create_checkout_session
item/<str:pk>/', views.get_item

```

http://127.0.0.1:8000/api/doc/ - документация по API



