

function clearError(el){
    el.removeAttribute("aria-invalid");
    const err = el.parentElement.querySelector(".form-error");
    if(err) err.remove();
}


function showError(el,msg){
    clearError(el);
    el.setAttribute("aria-invalid","true");

    const err = document.createElement("div");
    err.className="form-error";
    err.textContent = msg;

    el.parentElement.appendChild(err);
}

function isPositiveInt(value){
    if(value==="") return true;
    const number = Number(value);

    if(Number.isNaN(number)){
        return false;
    }

    if(!Number.isInteger(number)){
        return false;
    }

    return number > 0;
}
