

document.addEventListener("DOMContentLoaded",function(){
    const form=document.querySelector("form.recipe-form");
    if(!form)return;

    const name = form.querySelector("#id_name");
    const prep = form.querySelector("#id_prep_time");

    function validate(){
        let ok = true;

        if(name){
            if(name.value.trim().length<3){
                showError(name,"Name must be at least 3 characters");
                ok=false;
            }else{
                clearError(name);
            }
        }

        if(prep){
            const v=prep.value.trim();
            if(isPositiveInt(v) && Number(v)>=1){

                clearError(prep);
            }else{
                showError(prep,"Prep time must be a positive int");
                ok = false;
            }
        }
        return ok;
    }

    form.addEventListener("submit",function(e){
        if(!validate()) e.preventDefault();
    });

    form.querySelectorAll("input").forEach(function(el){
        el.addEventListener("input",validate);
    })





});