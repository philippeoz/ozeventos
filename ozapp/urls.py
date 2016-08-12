from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
#Criação das URLs relacionando-as às respectivas Views
urlpatterns = [ 
    url(r'^$', views.home), # A sequencia vazia '^$' indica que para a URL http://127.0.0.1:8000, deve-se ir para a view.home
    url(r'^cadastrar/$', views.cadastrar), # Para a URL '^cadastrar/$', deve-se ir para a view Cadastrar, onde teremos o cadastro do usuário no Sistema.
    url(r'^cadastrarevento/$', views.cadastrar_evento), #URL para o cadastro de eventos no sistema 
    url(r'^login/$', views.logar), #URL para o login do usuário no Sistema.
    url(r'^home/$', views.home), # URL da página inicial do sistema.
    url(r'^incricaoevento/$', views.incricao_evento), # URL da página inscrição de usuário em evento.
    url(r'^buscarevento/$', views.buscar_evento), # URL da página busca de eventos no Sistema.
    url(r'^logout/$', views.logout_view),
]
urlpatterns += staticfiles_urlpatterns()

''' 
Regex: 
^ cadastrar / está dizendo ao Django para pegar tudo que tenha cadastrar / no início da url (logo após o ^)
(\d+) significa que haverá um número (um ou mais dígitos) e que queremos o número capturado e extraído
/ diz para o Django que deve seguir outro /
$ indica o final da URL significando que apenas sequências terminando com o / irão corresponder a esse padrão
'''