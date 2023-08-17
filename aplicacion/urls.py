from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', paginaprincipal, name="inicio"),
    
    path('zonanorte/', ZonaNorteList.as_view(), name="zona norte"),
    path('zonasur/', ZonaSurList.as_view(), name="zona sur"),
    path('zonaoeste/', ZonaOesteList.as_view(), name="zona oeste"),
    path('caba/', CabaList.as_view(), name="caba"),
    
    path('create_zonanorte/', ZnCreate.as_view(), name="create_zonanorte"),
    path('create_zonaoeste/', ZoCreate.as_view(), name="create_zonaoeste"),
    path('create_zonasur/', ZsCreate.as_view(), name="create_zonasur"),
    path('create_caba/', CabaCreate.as_view(), name="create_caba"),
    
    path('detail_zonanorte/<int:pk>/', ZnDetail.as_view(), name="detail_zonanorte"),
    path('detail_zonaoeste/<int:pk>/', ZoDetail.as_view(), name="detail_zonaoeste"),
    path('detail_zonasur/<int:pk>/', ZsDetail.as_view(), name="detail_zonasur"),
    path('detail_caba/<int:pk>/', CabaDetail.as_view(), name="detail_caba"),
    
    path('update_zonanorte/<int:pk>/', ZnUpdate.as_view(), name="update_zonanorte"),
    path('update_zonaoeste/<int:pk>/', ZoUpdate.as_view(), name="update_zonaoeste"),
    path('update_zonasur/<int:pk>/', ZsUpdate.as_view(), name="update_zonasur"),
    path('update_caba/<int:pk>/', CabaUpdate.as_view(), name="update_caba"),
 
    path('delete_zonanorte/<int:pk>/', ZnDelete.as_view(), name="delete_zonanorte"),
    path('delete_zonaoeste/<int:pk>/', ZoDelete.as_view(), name="delete_zonaoeste"),  
    path('delete_zonasur/<int:pk>/', ZsDelete.as_view(), name="delete_zonasur"),  
    path('delete_caba/<int:pk>/', CabaDelete.as_view(), name="delete_caba"),  
    
    path('znbuscar/', znbuscar, name="znbuscar"),
    path('znbuscar2/', znbuscar2, name="znbuscar2"),
    path('zsbuscar/', zsbuscar, name="zsbuscar"),
    path('zsbuscar2/', zsbuscar2, name="zsbuscar2"),
    path('zobuscar/', zobuscar, name="zobuscar"),
    path('zobuscar2/', zobuscar2, name="zobuscar2"),
    path('cababuscar/', cababuscar, name="cababuscar"),
    path('cababuscar2/', cababuscar2, name="cababuscar2"),


    path('login/', log_in, name='login'),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout'),
    path('register', register, name="register"),
    path('editar_form', user_edit, name="editar_form"),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    
    
    #-----------------------------------------
    path('comentariozn/<int:zona_norte_id>/', comentariozn, name="comentariozn"),
   
    ]