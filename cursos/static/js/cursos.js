let filtros=[]
function filtro(event){
    if(event.checked){
        filtros.push(event.value)
    }else{
        for(i=0; i<filtros.length; i++){
            if(filtros[i]==event.value){
                filtros.splice(i, 1)
            }
        }
    }
    
    console.log(filtros);
}

window.onload=()=>{
    let btnfilter = document.querySelector(".btnfiltro")
    let div = document.querySelector(".filtragem")
    let favicon = document.querySelector(".fv")
    let spn = document.querySelector("#txt")
    btnfilter.addEventListener('click', ()=>{
        if(div.classList.contains("visually-hidden")){
            div.classList.remove("visually-hidden");
            favicon.classList.remove("fa-filter")
            favicon.classList.add("fa-filter-circle-xmark")
            spn.innerText = "Remover filtro"
        }
        else{
        filtros=[];
        console.log(filtros)
        div.classList.add("visually-hidden");
        favicon.classList.remove("fa-filter-circle-xmark")
        favicon.classList.add("fa-filter")
        spn.innerText = "Filtro"
        }
    })
}