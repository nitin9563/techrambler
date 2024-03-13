

function toggleActive(x){
    let buttons = document.querySelectorAll(".nc-a");

    if (x==4){
        buttons[x-1].classList.add("nc-a-active");
        buttons.forEach(e => {
            e.classList.remove("nc-a-active");
        });
    }

    
}
