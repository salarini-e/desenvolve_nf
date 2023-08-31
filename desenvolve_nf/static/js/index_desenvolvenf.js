//Definindo a lógica por trás do dropdown do nav
const dropDownElemento = document.querySelector(".dropDown");
dropDownElemento.addEventListener("click", evento=>{
    const dropDownContentElemento = document.querySelector(".dropDownContent");
    dropDownContentElemento.style.display=="none" ? dropDownContentElemento.style.display="block" : dropDownContentElemento.style.display="none";  
})
