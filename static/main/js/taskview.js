"use strict";

const buttonModal = Array.from(document.querySelectorAll("[data-toggle-button]"));
const modalMain = document.querySelector("[data-modal]");
const closeButton = document.querySelector("[data-close-button]");
const resetButton = document.querySelector("[data-reset-button]");
const toggleModal = (userId) =>{
    document.getElementById("userId").value = userId
    modalMain.classList.remove("hidden")
}

buttonModal.map((buttonModalEle) => {
    buttonModalEle.addEventListener("click", (event) => {
    const currentElement = event.currentTarget;
    toggleModal(currentElement.dataset.userId)
    })
});
const closeModal = (userId) =>{
        modalMain.classList.add("hidden")
    }
closeButton.addEventListener("click",  closeModal);
resetButton.addEventListener("click",  closeModal);
