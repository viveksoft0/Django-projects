from django.urls import path

from . import views


urlpatterns = [
    path('', (views.PostShow), name='home'),
    path('bye', (views.VIEWNAME), name='go'),
    path('post/', (views.Post_view), name='Post'),
    path('signup/', (views.Registration), name='signup'),
    path('delete/<int:id>/',(views.DeletePost),name='delete'),
    path('update/<int:id>/',(views.UpdatePost),name='update'),
]
