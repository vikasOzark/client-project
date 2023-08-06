"use strict";
/** @type {?HTMLButtonElement} */
const buttonToggleMobile = document.querySelector('[data-toggle-mobile]');

/** @type {?HTMLButtonElement} */
const buttonCloseMobile = document.querySelector('[data-close-mobile]');

/** @type {?HTMLDivElement} */
const toggleMobileMenu = document.querySelector('[data-mobile-menu]');


/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveMobile = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

buttonToggleMobile?.addEventListener('click', ()=>{
    classAddRemoveMobile(toggleMobileMenu, ['block'], ['hidden']);
})

buttonCloseMobile?.addEventListener('click', ()=>{
    classAddRemoveMobile(toggleMobileMenu, ['hidden'], ['block']);
})

