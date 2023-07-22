"use strict";

/**
 * @param {?HTMLElement} element
 * @param {Array<string>} addClass
 * @param {Array<string>} removeClass
 */
const classAddRemoveUser = function (element, addClass, removeClass) {
	if (addClass) {
		element?.classList.add(...addClass);
	}
	if (removeClass) {
		element?.classList.remove(...removeClass);
	}
};

/** @type {?HTMLButtonElement} */
const buttonCancelProfile = document.querySelector('[data-cancelpro-button]');

/** @type {?HTMLButtonElement} */
const buttonEditProfile = document.querySelector('[data-editpro-button]');

/** @type {?HTMLDivElement} */
const changePasswordMain = document.querySelector('[data-change-password]');

/** @type {?HTMLDivElement} */
const editProfileMain = document.querySelector('[data-edit-profile]');

buttonEditProfile?.addEventListener("click", ()=> {
    const editProfileAttr = editProfileMain?.getAttribute('data-edit-profile');
    switch(editProfileAttr){
        case 'false':
            editProfileMain?.setAttribute('data-edit-profile', true);
            classAddRemoveUser(editProfileMain, ['block'], ['hidden']);
            buttonEditProfile?.setAttribute('disabled', true);
            buttonCancelProfile?.removeAttribute('disabled');
            changePasswordMain?.setAttribute('data-change-password', false);
            classAddRemoveUser(changePasswordMain, ['hidden'], ['block']);
            break;
        case 'true':
            editProfileMain?.setAttribute('data-edit-profile', false);
            classAddRemoveUser(editProfileMain, ['hidden'], ['block']);
            break;
    }
    
})

buttonCancelProfile?.addEventListener("click", ()=> {
    const changePasswordAttr = changePasswordMain?.getAttribute('data-change-password');
    switch(changePasswordAttr){
        case 'false':
            changePasswordMain?.setAttribute('data-change-password', true);
            classAddRemoveUser(changePasswordMain, ['block'], ['hidden']);
            editProfileMain?.setAttribute('data-edit-profile', false);
            classAddRemoveUser(editProfileMain, ['hidden'], ['block']);
            buttonEditProfile?.removeAttribute('disabled');
            buttonCancelProfile?.setAttribute('disabled', true);
            break;
        case 'true':
            changePasswordMain?.setAttribute('data-change-password', false);
            classAddRemoveUser(changePasswordMain, ['hidden'], ['block']);
            editProfileMain?.setAttribute('data-edit-profile', true);
            classAddRemoveUser(editProfileMain, ['block'], ['hidden'])
            break;
    }
})