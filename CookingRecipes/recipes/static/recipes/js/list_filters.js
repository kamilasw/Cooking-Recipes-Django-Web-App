

document.addEventListener("DOMContentLoaded",function(){

    const form = document.querySelector("form.filters");
    if(!form) return;

    const q = form.querySelector("#q");
    const maxTime = form.querySelector("#max_time");

    function validate(){
        let ok = true;

        if(q){
            if(q.value.trim().length ===1){
                showError(q,"Enter at least 2 characters.");
                ok = false;
            }
            else{
                clearError(q);
            }
        }

        if(maxTime){

            if(isPositiveInt(maxTime.value.trim())){
                clearError(maxTime);
            }else
            {
                showError(maxTime,"Max time must be a int positive");
                ok = false;

            }
        }

        return ok;

    }




    form.addEventListener("submit",function(e){
        if(!validate()) e.preventDefault();
    });

    [q,maxTime].forEach(function(el){
        if(!el)return;
        el.addEventListener("input",validate);
    });



});