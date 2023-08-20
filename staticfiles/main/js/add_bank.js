"use strict";

/** @type {?HTMLButtonElement} */
const buttonAddBank = document.querySelector('[data-add-bank-button]');

/** @type {?HTMLDivElement} */
const addBankMain = document.querySelector('[data-addbank-acc]');

/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveBank = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

buttonAddBank?.addEventListener('click', ()=>{
    const addBankMainAttr = addBankMain?.getAttribute('data-addbank-acc')
    switch (addBankMainAttr) {
        case 'false':
            addBankMain?.setAttribute('data-addbank-acc', true);
            classAddRemoveBank(addBankMain, ['block'], ['hidden']);
            break;
        case 'true':
            addBankMain?.setAttribute('data-addbank-acc', false);
            classAddRemoveBank(addBankMain, ['hidden'], ['block']);
            break;
    } 
})
