

function toggleActive(x){
    let buttons = document.querySelectorAll(".nc-a");
    let arr = document.querySelectorAll(".all-posts");

    console.log(arr);
    buttons.forEach(e => {
        e.classList.remove("nc-a-active");
    });

    arr.forEach(e => {
        e.classList.remove("all-posts-active");
        console.log(e,"done")
    });

    buttons[x-1].classList.add("nc-a-active");
    arr[x-1].classList.add("all-posts-active");
}