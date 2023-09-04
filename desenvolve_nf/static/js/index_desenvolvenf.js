/*Definindo a lógica por trás do dropdown do nav:*/
document.addEventListener("click", e=>{
    const isDropDownButton = e.target.matches("[data-dropdown-button]");
    if(!isDropDownButton && e.target.closest("[data-dropdown]") != null) return;
    
    let currentDropDown = null;
    if(isDropDownButton){
        currentDropDown = e.target.closest("[data-dropdown]");
        currentDropDown.classList.toggle("activate");
    }

    document.querySelectorAll("[data-dropdown].activate").forEach(dropDown=>{
        if(dropDown == currentDropDown) return;
        dropDown.classList.remove("activate");
    })
});