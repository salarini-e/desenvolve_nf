from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from ..models import Notification
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from ..models import Notification

register = template.Library()


@register.simple_tag
def render_notification():
    notificacao = ''
    notificacoes = Notification.objects.filter(viewed=False)
    if notificacoes.exists():
        for i in notificacoes:
            url = reverse('notification:visualizar', args=[i.hash])  
            notificacao += f"""
            <a href="{url}" class="d-not d-flex p-3">
                <i class="text-success fa-solid fa-list-check my-auto me-4"></i>
                <div class="d-flex flex-column">
                  <small>{i.referencia}</small>
                  <p class="text-dark w-100 bold">{i.mensagem}</p>
                </div>
              </a>
            """
        html = f"""
        <div class="notification my-auto ms-2">
        <div class="dropdown">
          <button class="btn btn-alert dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="box-shadow: none !important;">
            <i class="fa-solid fa-bell bell-icon"></i>
          </button>
          <ul class="dropdown-menu" style="background-color: #eef6ff">
            <li>
              {notificacao}        
            </li>
          </ul>
        </div>      
      </div>
        """
    else:
        html = f""
    return mark_safe(html)
