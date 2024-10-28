from django.urls import path

from App import views


urlpatterns = [
    path('', views.mostrar_index, name='Home'),
    path('productos/', views.mostrar_productos, name='Productos'),
    path('usuarios/', views.mostrar_usuarios, name='Usuarios'),
    path('venta_detalles/', views.mostrar_ventas_detalles, name='Ventas_detalles'),
    path('crear_usuarios/', views.crear_Usuarios, name='Crear usuarios'),
    path('crear_productos/', views.crear_Productos, name='Crear productos'),
    path('crear_ventas/', views.crear_Ventas_detalles, name='Crear Ventas_detalles'),
    path('buscar_marca_producto/', views.buscar_marca_producto, name='Buscar productos'),
    path('buscar_email_usuario/', views.buscar_usuario, name='Buscar usuarios'),
    path('buscar_ventas_detalles/', views.buscar_forma_de_pago, name='Buscar ventas_detalles'),
    path('eliminar_productos/<productos_id>/', views.eliminar_productos, name='Eliminar productos'),
    path('actualizar_productos/<productos_id>/', views.actualizar_productos, name='Actualizar productos'),
    path('eliminar_usuarios/<usuario_id>/', views.eliminar_usuarios, name='Eliminar usuarios'),
    path('actualizar_usuarios/<usuario_id>/', views.actualizar_usuarios, name='Actualizar usuarios'),
    path('eliminar_ventas_detalles/<ventas_detalles_id>/', views.eliminar_Ventas_detalles, name='Eliminar Ventas detalles'),
    path('actualizar_ventas_detalles/<ventas_detalles_id>/', views.actualizar_ventas_detalles, name='Actualizar Ventas detalles'),
    path('registro/', views.registro_usuario, name='Registro'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracias/', views.pagina_de_gracias, name='pagina_de_gracias'),
    path('mensajes/', views.listar_mensajes, name='listar_mensajes'),
    
         
]

# ... Add more URLs as needed.

    
      

