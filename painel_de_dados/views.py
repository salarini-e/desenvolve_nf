from django.shortcuts import render
from datetime import datetime
def index(request):
    data_atual = datetime.now()
    context={
        'data_atual': data_atual.strftime('%d/%m/%Y %H:%M'),
    }
    return render(request, 'painel_de_dados/index.html', context)