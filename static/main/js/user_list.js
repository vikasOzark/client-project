"use strict";

/** @type {?Array <HTMLInputElement>} */
const checkActiveUser = Array.from(document.querySelectorAll('[data-check-user]'));
// const csrfToken = Array.from(document.getElementById('[name="csrfmiddlewaretoken"]'));
const url = Array.from(document.getElementById('action-url'));



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

const call_active_inactive = (pk) => {
    fetch(`accout-operation/?user=${pk}`)
    .then(data => {
        window.location.reload()
    })
}


checkActiveUser?.map((checkElement) => {
    checkElement?.addEventListener("click", (event) => {
        const checkActiveUserAttr = checkElement?.getAttribute("data-check-user");
        const userID = event.currentTarget.getAttribute("data-user-id");
        switch (checkActiveUserAttr) {
            case "false":
                event.currentTarget.setAttribute("data-check-user", true);
                event.currentTarget.parentElement.children[2].textContent = "Active";
                call_active_inactive(userID)
                break;
            case "true":
                event.currentTarget.setAttribute("data-check-user", false);
                event.currentTarget.parentElement.children[2].textContent = "Inactive";
                call_active_inactive(userID)
                break;
        }
    });
});

