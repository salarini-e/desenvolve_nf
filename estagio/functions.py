from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.http import HttpResponse

def send_email_for_process(instance, historico):
    subject = "Alteração de status no seu processo de Estágio no sistema Desenvolve NF"
    email_template_name = "estagio/email_atualização_processo.txt"
    
    if instance.local_do_estagio:
        local_do_estagio = instance.local_do_estagio.local
    else:
        local_do_estagio = instance.local_do_estagio_de_pretensao.local
    c = {
        "email": instance.estudante.pessoa.user.email,
        'domain': 'desenvolve.novafriburgo.rj.gov.br/estagio/area-do-estudante/',
        'site_name': 'Desenvolve NF',
        "user": instance.estudante.pessoa.user,
        'protocol': 'https',
        'estudante': instance.estudante,
        'local_do_estagio': local_do_estagio,
        'historico': historico,
        'msg': historico.mensagem,
    }
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, instance.estudante.pessoa.user.email, [
                    instance.estudante.pessoa.user.email], fail_silently=False)
    except Exception as E:
        print(E)
        return 'Falha ao enviar email.'