"use strict";
/** @type {?HTMLButtonElement} */
const adminToggle = document.querySelector('[data-admin-toggle]');

/** @type {?HTMLDivElement} */
const adminMain = document.querySelector('[data-admin-main]');

/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemove = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

adminToggle?.addEventListener('click', ()=>{
    const adminMainAttr = adminMain?.getAttribute('data-admin-main')
    switch (adminMainAttr) {
        case 'false':
            adminMain?.setAttribute('data-admin-main', true);
            classAddRemove(adminMain, ['block'], ['hidden']);
            break;
        case 'true':
            adminMain?.setAttribute('data-admin-main', false);
            classAddRemove(adminMain, ['hidden'], ['block']);
            break;
    } 
})



