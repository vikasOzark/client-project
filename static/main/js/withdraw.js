"use strict";

/** @type {?HTMLSelectElement} */
const paymentSelect = document.querySelector('#payment_channel');

/** @type {?HTMLInputElement} */
const inputAmmount = document.querySelector('[data-ammount]');

/** @type {?HTMLDivElement} */
const mainUPI = document.querySelector('[data-idUPI]');

/** @type {?HTMLDivElement} */
const mainBANK = document.querySelector('[data-idBank]');

/** @type {?HTMLButtonElement} */
const cancelButton = document.querySelector('[data-cancel-payment]');

/** @type {?HTMLButtonElement} */
const proceedButton = document.querySelector('[data-payment]');

/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveWithdraw = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

const fetchData =  ()=>{
	paymentSelect.addEventListener("change", ()=> {
		const paymentOption = paymentSelect.selectedOptions[0];
		switch(paymentOption.value){
			case 'UPI':
				classAddRemoveWithdraw(mainUPI, ['lg:grid'], ['!hidden']);
				classAddRemoveWithdraw(mainBANK, ['!hidden'], ['lg:grid']);
                proceedButton.removeAttribute('disabled', '');
				break;
			case 'BANK':
				classAddRemoveWithdraw(mainBANK, ['lg:grid'], ['!hidden']);
				classAddRemoveWithdraw(mainUPI, ['!hidden'], ['lg:grid']);
                proceedButton.removeAttribute('disabled', '');
				break;
			default:
				classAddRemoveWithdraw(mainUPI, ['!hidden'], ['lg:grid']);
				classAddRemoveWithdraw(mainBANK, ['!hidden'], ['lg:grid']);
                proceedButton.setAttribute('disabled', '');
		}
	})
}

inputAmmount?.addEventListener("keyup", ()=>{
	const inputAmmountValue = inputAmmount.value;
	if (isNaN(inputAmmountValue) || inputAmmountValue === '') {
		document.querySelector('#ammount').innerHTML = '<i class="icon-info"> </i> Please Enter Numbric Value..'
		paymentSelect.setAttribute('disabled', '');
	} else {
		document.querySelector('#ammount').innerHTML = ''
		paymentSelect.removeAttribute('disabled', '');
		fetchData();
	}
})

document?.addEventListener("keypress", (event)=> {
	if (event.key === "Enter"){
		event.preventDefault();
	}
})

cancelButton?.addEventListener("click", ()=>{
	classAddRemoveWithdraw(mainUPI, ['!hidden'], ['lg:grid']);
	classAddRemoveWithdraw(mainBANK, ['!hidden'], ['lg:grid']);
	proceedButton.setAttribute('disabled', '');
	paymentSelect.setAttribute('disabled', '')
})