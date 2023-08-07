"use strict";

/** @type {?HTMLSelectElement} */
const paymentSelect = document.querySelector('#payment_channel');

/** @type {?HTMLButtonElement} */
const paymentBack = document.querySelector('[data-back]');

/** @type {?HTMLInputElement} */
const inputAmmount = document.querySelector('[data-ammount]');

/** @type {?HTMLDivElement} */
const selectStepOne = document.querySelector('[data-stepOne]');

/** @type {?HTMLDivElement} */
const selectStepTwo = document.querySelector('[data-stepTwo]');

/** @type {?HTMLDivElement} */
const selectStepBank = document.querySelector('[data-bank]');

/** @type {?HTMLDivElement} */
const selectStepUPI = document.querySelector('[data-upi]');

/** @type {?HTMLDivElement} */
const copyUPI = document.querySelector('[data-copy]');

/** @type {?HTMLSpanElement} */
const copyUPIItem = document.querySelector('[data-copyItem]');

/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveDeposite = function (element, addClass, removeClass) {
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
			case 'upi':
				classAddRemoveDeposite(selectStepUPI, ['block'], ['hidden']);
				classAddRemoveDeposite(selectStepBank, ['hidden'], ['block']);
				classAddRemoveDeposite(selectStepOne, ['!hidden'], ['lg:grid']);
				classAddRemoveDeposite(selectStepTwo, ['lg:grid'], ['!hidden']);
				break;
			case 'bank':
				classAddRemoveDeposite(selectStepOne, ['!hidden'], ['lg:grid']);
				classAddRemoveDeposite(selectStepTwo, ['lg:grid'], ['!hidden']);
				classAddRemoveDeposite(selectStepBank, ['block'], ['hidden']);
				classAddRemoveDeposite(selectStepUPI, ['hidden'], ['block']);
				break;
			default:
				classAddRemoveDeposite(selectStepUPI, ['hidden'], ['block']);
				classAddRemoveDeposite(selectStepBank, ['hidden'], ['block']);
		}
	})
}

inputAmmount.addEventListener("keyup", ()=>{
	const inputAmmountValue = inputAmmount.value;
	if (isNaN(inputAmmountValue) || inputAmmountValue === '') {
		document.querySelector('#ammount').innerHTML = '<i class="icon-info"> </i> Please Enter Numbric Value..'
		paymentSelect.setAttribute('disabled', '')
	} else {
		document.querySelector('#ammount').innerHTML = ''
		paymentSelect.removeAttribute('disabled', '')
		fetchData();
	}
})

document.addEventListener("keypress", (event)=> {
	if (event.key === "Enter"){
		event.preventDefault();
	}
})


paymentBack.addEventListener("click", ()=>{
	const paymentBackValue = paymentBack.getAttribute('data-back');
	switch(paymentBackValue){
		case 'true':
			paymentBack.setAttribute('data-back', 'false');
			classAddRemoveDeposite(selectStepUPI, ['hidden'], ['block']);
			classAddRemoveDeposite(selectStepBank, ['hidden'], ['block']);
			classAddRemoveDeposite(selectStepOne, ['lg:grid'], ['!hidden']);
			classAddRemoveDeposite(selectStepTwo, ['!hidden'], ['lg:grid']);
			paymentSelect.setAttribute('disabled', '')
			break;
		case 'false':
			paymentBack.setAttribute('data-back', 'true');
			classAddRemoveDeposite(selectStepUPI, ['hidden'], ['block']);
			classAddRemoveDeposite(selectStepBank, ['hidden'], ['block']);
			classAddRemoveDeposite(selectStepOne, ['lg:grid'], ['!hidden']);
			classAddRemoveDeposite(selectStepTwo, ['!hidden'], ['lg:grid']);
			paymentSelect.setAttribute('disabled', '')
			break;
	}
})

const copyContent = async () => {
	const textCopied = document.querySelector('#text_copied');
    try {
		await navigator.clipboard.writeText(copyUPIItem.textContent);
		classAddRemoveDeposite(textCopied, ['block'], ['hidden']);
      	textCopied.textContent = 'Content copied to clipboard!';
    } catch (err) {
		classAddRemoveDeposite(textCopied, ['hidden'], ['block']);
		textCopied.textContent = `Failed to copy: ${err}`
    }
	setTimeout(()=>{
		classAddRemoveDeposite(textCopied, ['hidden'], ['block']);
	},1000)
}

copyUPI.addEventListener("click", ()=>{
	copyContent()
})