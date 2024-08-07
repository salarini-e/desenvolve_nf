from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from ..models import BoletosRequerimentoISS, RequerimentoISS

register = template.Library()

@register.simple_tag
def render_button_atualizar_documento(n_protocolo, doc, nome_doc, status):
    url = reverse('processos_empreendedor:atualizar_documento_processo', kwargs={'n_protocolo': n_protocolo, 'doc': doc})
    if status == '2':
        html = f"""
        <div class="col d-flex flex-column"> 
            <a href="{url}" class="border py-2" style="border-radius: 20px;">
                Atualizar {nome_doc}
            </a>               
        </div>
        """
    else:
        html = f"""
        <div class="col d-flex flex-column"> 
            
        </div>
        """
    return mark_safe(html)

@register.simple_tag
def boleto(requerimento_id, tipo):
    requerimento = RequerimentoISS.objects.get(id=requerimento_id)
    boleto = BoletosRequerimentoISS.objects.filter(requerimento=requerimento)
    if boleto.exists():
        boleto = boleto.first()
        if tipo == 'ambiental':
            if boleto.boleto_licenca_ambiental and not boleto.comprovante_licenca_ambiental:
                url = boleto.boleto_licenca_ambiental.url
                return mark_safe(f"""
                <a class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Ver boleto atual
                </a>
                <label for="formFile" class="form-label">Envie ou atualize o boleto</label>
                <input name="boleto-{tipo}" class="form-control" type="file" id="formFile">
                <button onclick="enviarBoleto('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
            else:
                return mark_safe(f"""
                <a class="btn btn-primary w-100 mb-3" href="{boleto.comprovante_licenca_ambiental.url}">
                    <i class="fa-solid fa-receipt me-2"></i></i> Analisar comprovante
                </a>""")
        elif tipo == 'sanitario':
            if boleto.boleto_licenca_sanitaria and not boleto.comprovante_licenca_sanitaria:
                url = boleto.boleto_licenca_sanitaria.url
                return mark_safe(f"""
                <a class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Ver boleto atual
                </a>
                <label for="formFile" class="form-label">Envie ou atualize o boleto</label>
                <input name="boleto-{tipo}" class="form-control" type="file" id="formFile">
                <button onclick="enviarBoleto('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
            else:
                return mark_safe(f"""
                <a class="btn btn-primary w-100 mb-3" href="{boleto.comprovante_licenca_sanitaria.url}">
                    <i class="fa-solid fa-receipt me-2"></i></i> Analisar comprovante
                </a>""")
        else:
            if boleto.boleto_requerimento:
                url = boleto.boleto_requerimento.url
                return mark_safe(f"""
                <a class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Ver boleto atual
                </a>
                <label for="formFile" class="form-label">Envie ou atualize o boleto</label>
                <input name="boleto-{tipo}" class="form-control" type="file" id="formFile">
                <button onclick="enviarBoleto('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
    
    return mark_safe(f"""<label for="formFile" class="form-label">Envie ou atualize o boleto</label>
    <input name="boleto-{tipo}" class="form-control" type="file" id="formFile">
    <button onclick="enviarBoleto('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          """)

@register.simple_tag
def boleto_usuario(requerimento_id, tipo):
    requerimento = RequerimentoISS.objects.get(id=requerimento_id)
    boleto = BoletosRequerimentoISS.objects.filter(requerimento=requerimento)
    if boleto.exists():
        boleto = boleto.first()
        if tipo == 'ambiental':
            if boleto.boleto_licenca_ambiental and not boleto.comprovante_licenca_ambiental:
                url = boleto.boleto_licenca_ambiental.url
                return mark_safe(f"""
                <a target="_blank" class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Baixar boleto
                </a>
                <label for="formFile" class="form-label remover-{tipo}">Envie comprovante de pagamento</label>
                <input name="comprovante-{tipo}" class="form-control remover-{tipo}" type="file" id="formFile">
                <button onclick="enviarComprovante('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100 remover-{tipo}" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
            else:
                return mark_safe(f"""
                <a class="btn btn-primary w-100 mb-3" href="{boleto.comprovante_licenca_ambiental.url}">
                    <i class="fa-solid fa-receipt me-2"></i></i> Analisar comprovante
                </a>""")
        elif tipo == 'sanitario':
            if boleto.boleto_licenca_sanitaria and not boleto.comprovante_licenca_sanitaria:
                url = boleto.boleto_licenca_sanitaria.url
                return mark_safe(f"""
                <a target="_blank" class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Baixar boleto
                </a>
                <label for="formFile" class="form-label remover-{tipo}">Envie comprovante de pagamento</label>
                <input name="comprovante-{tipo}" class="form-control remover-{tipo}" type="file" id="formFile">
                <button onclick="enviarComprovante('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100 remover-{tipo}" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
            else:
                return mark_safe(f"""
                <a class="btn btn-primary w-100 mb-3" href="{boleto.comprovante_licenca_sanitaria.url}">
                    <i class="fa-solid fa-receipt me-2"></i></i> Analisar comprovante
                </a>""")
        else:
            if boleto.boleto_requerimento:
                url = boleto.boleto_requerimento.url
                return mark_safe(f"""
                <a target="_blank" class="btn btn-success w-100 mb-3" href="{url}">
                    <i class="fa-solid fa-paperclip me-2"></i> Baixar boleto
                </a>
                <label for="formFile" class="form-label remover-{tipo}">Envie comprovante de pagamento</label>
                <input name="comprovante-{tipo}" class="form-control remover-{tipo}" type="file" id="formFile">
                <button onclick="enviarComprovante('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100 remover-{tipo}" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          
                """)
    
    return mark_safe(f"""<label for="formFile" class="form-label">Envie comprovante de pagamento</label>
    <input name="comprovante-{tipo}" class="form-control remover-{tipo}" type="file" id="formFile">
    <button onclick="enviarComprovante('{tipo}', '{requerimento.processo.id}')" class="btn btn-light mt-3 w-100 remover-{tipo}" style="border: 1px solid rgba(0, 0, 0, 0.445);"><i class="fa-solid fa-file-import me-2"></i>Enviar</button>          """)