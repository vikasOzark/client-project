"use strict"

/** @type {?HTMLAnchorElement} */
const textCopied = document.querySelector("[data-invitation]");

/** @type {?HTMLSpanElement} */
const textValue = document.querySelector("[data-text]");

textCopied?.addEventListener("click", ()=> {
    const textCopiedValue = textCopied.getAttribute("data-invitation");
    navigator.clipboard.writeText(textCopiedValue);
    textValue?.classList.remove("hidden");
    setTimeout(()=>{
        textValue?.classList.add("hidden");
    }, 2000)
})
