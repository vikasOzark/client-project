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



swipeToogleButton?.addEventListener('click', ()=>{
    const swipeToogleButtonAttr = swipeToogleButton?.getAttribute('data-swipe')
    switch (swipeToogleButtonAttr) {
        case 'false':
            dataMain?.setAttribute('data-main', true);
            dataAside?.setAttribute('data-aside', true);
            dataNavLogo?.setAttribute('data-navlogo', true);
            dataFooter?.setAttribute('data-footer', true);
            swipeToogleButton?.setAttribute('data-swipe', true);
            classAddRemove(swipeToogleButton.children[0], ['icon-left-arrow'], ['icon-right-arrow']);
            break;
        case 'true':
            dataMain?.setAttribute('data-main', false);
            dataAside?.setAttribute('data-aside', false);
            dataNavLogo?.setAttribute('data-navlogo', false);
            dataFooter?.setAttribute('data-footer', false);
            swipeToogleButton?.setAttribute('data-swipe', false);
            classAddRemove(swipeToogleButton.children[0], ['icon-right-arrow'], ['icon-left-arrow']);
            
        break;
    } 
})


