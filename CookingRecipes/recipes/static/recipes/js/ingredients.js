

function getCookie(name){
    const value = `;${document.cookie}`;
    const parts = value.split(`;${name}=`);
    if (parts.length === 2){
        return parts.pop().split(';').shift()
    }
}

const csrftoken = getCookie("csrftoken")

// creating the ingredient
const createForm= document.getElementById('create-ing-form');
const createBtn = createForm.querySelector("button");
const msg = document.getElementById("ing-msg");

createBtn.addEventListener("click", async()=>{

    msg.textContent="";

    const res = await fetch(createForm.dataset.url, {
        method: "POST",
        headers:{"X-CSRFToken": csrftoken},
        body: new FormData(createForm)
    })

    const data = await res.json();


    if(!res.ok){
        msg.textContent=data.error;
        return;
    }

    //add this to the select ingredient for the recipe
    const select = document.getElementById("ingredient");



    if (!select.querySelector(`option[value="${data.id}"]`)) {

        select.add(new Option(data.name, data.id));
    }

    select.value = data.id;
    createForm.reset();
    msg.textContent = data.created ? "Ingredient created." : "Ingredient already exists.";


});

// add ingredient to the recipe
const addForm = document.getElementById("add-ing-form");
const addBtn = addForm.querySelector("button");
const list = document.getElementById("ingredients-list")

addBtn.addEventListener("click",async()=>{

    msg.textContent="";

    const res = await fetch(addForm.dataset.url,{
        method:"POST",
        headers:{"X-CSRFToken":csrftoken},
        body: new FormData(addForm),

    })

    const data = await res.json();

    if(!res.ok){
        msg.textContent=data.error;
        return;
    }

    const empty = list.querySelector(".empty-note");
    if (empty) empty.remove();

    const li = document.createElement("li");
    li.textContent = `${data.amount} ${data.unit} ${data.ingredient.name}`;
    list.appendChild(li);

    addForm.reset();
    msg.textContent="Ingredient added."

});
