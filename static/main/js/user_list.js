"use strict";

/** @type {?Array <HTMLInputElement>} */
const checkActiveUser = Array.from(document.querySelectorAll('[data-check-user]'));


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


checkActiveUser?.map((checkElement) => {
    checkElement?.addEventListener("click", (event) => {
        const checkActiveUserAttr = checkElement?.getAttribute("data-check-user");
        switch (checkActiveUserAttr) {
            case "false":
                event.currentTarget.setAttribute("data-check-user", true);
                event.currentTarget.parentElement.children[2].textContent = "Active";
                break;
            case "true":
                event.currentTarget.setAttribute("data-check-user", false);
                event.currentTarget.parentElement.children[2].textContent = "Inactive";
                break;
        }
    });
});