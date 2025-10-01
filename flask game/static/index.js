const addEventControllers = () => {
    const clueControl = document.getElementById("clue-control");
    clueControl.addEventListener("click", () => {
        const clueModel = document.getElementById("clue-model");
        clueModel.classList.remove("hidden");
        clueControl.classList.add("hidden");
    });

    const closeModel = document.getElementById("close-model");
    closeModel.addEventListener("click", () => {
        const clueModel = document.getElementById("clue-model");
        clueModel.classList.add("hidden");
        clueControl.classList.remove("hidden");
    });
}

addEventControllers();