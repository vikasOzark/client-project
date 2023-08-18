"use strict";
/** @type {?HTMLButtonElement} */
const buttonToggleMobileWebsite = document.querySelector('[data-toggle-mobile-website]');

/** @type {?HTMLButtonElement} */
const buttonCloseMobileWebsite = document.querySelector('[data-close-mobile-website]');

/** @type {?HTMLDivElement} */
const toggleMobileMenuWebsite = document.querySelector('[data-toggle-menu-website]');


/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveWebsite = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

buttonToggleMobileWebsite?.addEventListener('click', ()=>{
    classAddRemoveWebsite(toggleMobileMenuWebsite, ['block'], ['hidden']);
})

buttonCloseMobileWebsite?.addEventListener('click', ()=>{
    classAddRemoveWebsite(toggleMobileMenuWebsite, ['hidden'], ['block']);
})

