from django import template
from django.utils.safestring import mark_safe
from ..models import Turma

register = template.Library()


@register.filter(is_safe=True)
def turmas(obj):
    try:        
        turmas=Turma.objects.filter(curso=obj, status='pre')
    except Exception as E:
        print(E)
        turmas=[]
    try:        
        turmas2=Turma.objects.filter(curso=obj, status='acc')
    except Exception as E:
        print(E)
        turmas2=[]
    
    response=''
    print(turmas)
    print(turmas2)
    if len(turmas)>0:        
        for turma in turmas:
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+' '+str(turma.id)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b> Horário: <b>'+str(turma.horario)+'</b></span><br>'
    if len(turmas2)>0:        
        for turma in turmas2:
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+' '+str(turma.id)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b> Horário: <b>'+str(turma.horario)+'</b></span><br>'    
    if len(turmas2)==0 and len(turmas)==0:
        response='<i class="ps-4 text-danger">Não há turmas disponíveis.</i>'
    return mark_safe(response)

@register.filter(is_safe=True)
def turmas_input(obj):
    print(obj)
    try:        
        turmas=Turma.objects.filter(curso=obj, status='pre')
    except Exception as E:
        print(E)
        turmas=[]
    try:        
        turmas2=Turma.objects.filter(curso=obj, status='acc')
    except Exception as E:
        print(E)
        turmas2=[]
    
    response=''
    
    if len(turmas)>0:                
        for turma in turmas:            
            response+='''<div class="form-check mt-1"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' '''+str(turma.id)+''' - '''+str(turma.local)+''' - '''+ str(turma.horario)+'''
</label></div>'''
    
    if len(turmas2)>0:                
        for turma in turmas2:
            response+='''<div class="form-check mt-1"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' '''+str(turma.id)+''' - '''+str(turma.local)+''' - '''+ str(turma.horario)+'''
</label></div>'''
    
    if len(turmas2)==0 and len(turmas)==0:
        response='<i class="ps-4 text-secondary">Não há turmas disponíveis.</i>'
    return mark_safe(response)