'use strict';

// Notification

const notificationAlert = function () {
	/** @type {?HTMLDivElement} */
	const alertArea = document.querySelectorAll('[data-alert]');
	/** @type {?HTMLDivElement} */
	const alertButton = document.querySelectorAll('[data-alert-close]');
	
	let count = 0;
	setInterval(() => {
		count++;
		if (count === 100) {
			for (const index of alertArea) {
				index.remove();
			}
			clearInterval();
		}
	}, 80);
	for (const alertBtn of alertButton) {
		alertBtn?.addEventListener('click', (event) => {
			event.currentTarget.closest('[data-alert]').remove();
		});
	}
};
notificationAlert();