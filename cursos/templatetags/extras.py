from django import template
from django.utils.safestring import mark_safe
from ..models import Turma

from datetime import date

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
    # print(turmas)
    # print(turmas2)
    if len(turmas)>0:        
        for turma in turmas:
            try:
                if turma.idade_minima and turma.idade_maxima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_minima)+' até '+ str(turma.idade_maxima)
                elif turma.idade_minima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_minima)+'+'
                elif turma.idade_minima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+'Até '+str(turma.idade_maxima)
                else:
                    faixa=''
            except:
                faixa=''
            
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b>- <b class="ms-4">Horário:</b> '+''' TEM QUE FAZER UMA FUNCAO AQUI '''+'</span>'+str(faixa)+'<br>'
    if len(turmas2)>0:        
        for turma in turmas2:
            try:
                if turma.idade_minima and turma.idade_maxima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_minima)+' até '+ str(turma.idade_maxima)
                elif turma.idade_minima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_minima)+'+'
                elif turma.idade_minima:
                    faixa='<b class="ms-4">Faixa etária: </b>'+'Até '+str(turma.idade_maxima)
                else:
                    faixa=''
            except:
                faixa=''
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b>- <b class="ms-4">Horário:</b> '+''' TEM QUE MUDAR AQUI '''+'</span>'+str(faixa)+'<br>'    
    if len(turmas2)==0 and len(turmas)==0:
        response='<i class="ps-4 text-danger">Não há turmas disponíveis.</i>'
    return mark_safe(response)

@register.filter(is_safe=True)
def turmas_input(obj):
    # print(obj)
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
            try:
                if turma.idade_minima and turma.idade_maxima:
                    faixa='<span class="">Faixa etária </span>'+str(turma.idade_minima)+' até '+ str(turma.idade_maxima) +' anos'
                elif turma.idade_minima:
                    faixa='<span class="">Faixa etária </span>'+str(turma.idade_minima)+'+ anos'
                elif turma.idade_maxima:
                    faixa='<span class="">Faixa etária </span>'+'Até '+str(turma.idade_maxima)+' anos'
                else:
                    faixa=''
            except Exception as e:
                faixa=''          
            response+='''<div class="form-check mt-1 turma"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' - '''+str(turma.local)+''' - '''+str(faixa)+'''</label></div>'''
    
    if len(turmas2)>0:                
        for turma in turmas2:
            response+='''<div class="form-check mt-1 turma"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' - '''+str(turma.local)+'''
</label></div>'''
    

    if len(turmas2)==0 and len(turmas)==0:
        response='<i class="ps-4 text-secondary">Não há turmas disponíveis.</i>'
    return mark_safe(response)



@register.filter(is_safe=True)
def idade(obj):    
    birthDate=obj
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    
    return mark_safe(f'''<span class="px-3">{age}</span>''')

@register.filter(is_safe=True)
def bg_idade(obj):    
    birthDate=obj
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    if int(age)<int(18):
        return mark_safe(f'''<span class="bg-warning px-3">{age}</span>''')
    else:
        return mark_safe(f'''<span class=" px-3">{age}</span>''')