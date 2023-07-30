"use strict";

/** @type {?HTMLBodyElement}  */
const LoadingAnimation = document.querySelector('#onLoadAnimation');

/** @type {?HTMLDivElement}  */
const LoadingAnimationGIF = document.querySelector('#loading');

window.addEventListener("load", () => {
  setTimeout(()=>{
    LoadingAnimationGIF?.remove();
  },100)
});