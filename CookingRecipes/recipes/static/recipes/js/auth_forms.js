

document.addEventListener("DOMContentLoaded",function(){
    const form=document.querySelector("form.auth-form");
    if(!form)return;

    const required = form.querySelectorAll("[required]");
    const pw1 = form.querySelector("#id_password1");
    const pw2 = form.querySelector("#id_password2");

    function validate(){
        let ok=true;

        required.forEach(function(el){
            if(!el.value.trim()){
                showError(el,"this field is required");
                ok=false;
            }
            else{
                clearError(el);
            }
        });

        return ok;
    }

    form.addEventListener("submit",function(e){
        if(!validate()) e.preventDefault();
    });

    form.querySelectorAll("input").forEach(function(el){
        el.addEventListener("input",validate);
    });

    form.addEventListener("reset",()=>{
        setTimeout(()=>{
            form.querySelectorAll("input,textarea,select").forEach(el=>{
                clearError(el);
            },0);
        });
    });



});

