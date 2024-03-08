

function toggleActive(x){
    let buttons = document.querySelectorAll(".nc-a");
    console.log(buttons)
    buttons.forEach(e => {
        e.classList.remove("nc-a-active");
    });
    buttons[x-1].classList.add("nc-a-active");
}