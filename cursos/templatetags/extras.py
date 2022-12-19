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
                if turma.idade_min and turma.idade_max:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_min)+' até '+ str(turma.idade_max)
                elif turma.idade_min:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_min)+'+'
                elif turma.idade_min:
                    faixa='<b class="ms-4">Faixa etária: </b>'+'Até '+str(turma.idade_max)
                else:
                    faixa=''
            except:
                faixa=''
            
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b>- <b class="ms-4">Horário:</b> '+str(turma.horario)+'</span>'+str(faixa)+'<br>'
    if len(turmas2)>0:        
        for turma in turmas2:
            try:
                if turma.idade_min and turma.idade_max:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_min)+' até '+ str(turma.idade_max)
                elif turma.idade_min:
                    faixa='<b class="ms-4">Faixa etária: </b>'+str(turma.idade_min)+'+'
                elif turma.idade_min:
                    faixa='<b class="ms-4">Faixa etária: </b>'+'Até '+str(turma.idade_max)
                else:
                    faixa=''
            except:
                faixa=''
            response+='<br><b class="ps-4">'+str(turma.curso.nome)+'</b><span class="ps-4">-<b class="ms-4 me-3">'+str(turma.local)+'</b>- <b class="ms-4">Horário:</b> '+str(turma.horario)+'</span>'+str(faixa)+'<br>'    
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
                if turma.idade_min and turma.idade_max:
                    faixa='<span class="">Faixa etária </span>'+str(turma.idade_min)+' até '+ str(turma.idade_max) +' anos'
                elif turma.idade_min:
                    faixa='<span class="">Faixa etária </span>'+str(turma.idade_min)+'+ anos'
                elif turma.idade_max:
                    faixa='<span class="">Faixa etária </span>'+'Até '+str(turma.idade_max)+' anos'
                else:
                    faixa=''
            except Exception as e:
                faixa=''          
            response+='''<div class="form-check mt-1 turma"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' - '''+str(turma.local)+''' - '''+ str(turma.horario)+''' - '''+str(faixa)+'''</label></div>'''
    
    if len(turmas2)>0:                
        for turma in turmas2:
            response+='''<div class="form-check mt-1 turma"><label class="form-check-label" for="id_turmas_'''+str(turma.id)+'''">                                        
    <input class="form-check-input" id="id_turmas_'''+str(turma.id)+'''" name="turmas" title="" type="checkbox" value="'''+str(turma.id)+'''">
    '''+str(turma.curso.nome)+''' - '''+str(turma.local)+''' - '''+ str(turma.horario)+'''
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