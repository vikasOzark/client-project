'use strict';

/** @type {?HTMLAnchorElement[]} */
const navItems = Array.from(document.querySelectorAll('[data-option]'));

/** @type {?HTMLAnchorElement} */
const navLogout = document.querySelector('[data-logout]');

/** @type {?HTMLAnchorElement} */
const navLogo = document.querySelector('[data-logo]');

const classListSpan = ["!text-white", "lg:w-14", "lg:h-14", "w-9", "h-9", "lg:border-4", "border-2", "border-gray-900" ,"rounded-full", "bg-gray-700" ,"inline-flex", "items-center", "justify-center"];


navItems?.map((element) => {
	element.addEventListener('click', (event) => {
		const navValue = event.currentTarget.getAttribute('data-option');
		sessionStorage.setItem('currentNavItem', navValue);
	});
});


const sessionValueStore = function () {
	const getSessionValue = sessionStorage.getItem('currentNavItem');
	switch (getSessionValue) {
		case 'dashboard':
			document.querySelector('[data-option="dashboard"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.add('hidden')
			break;
		case 'bank':
			document.querySelector('[data-option="bank"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="bank"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="bank"]')?.children[1].classList.add('hidden')
			break;
		case 'deposite':
			document.querySelector('[data-option="deposite"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="deposite"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="deposite"]')?.children[1].classList.add('hidden')
			break;
		case 'withdraw':
			document.querySelector('[data-option="withdraw"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="withdraw"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="withdraw"]')?.children[1].classList.add('hidden')
			break;
		case 'tasks':
			document.querySelector('[data-option="tasks"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="tasks"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="tasks"]')?.children[1].classList.add('hidden')
			break;
        case 'profile':
            document.querySelector('[data-option="profile"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="profile"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="profile"]')?.children[1].classList.add('hidden')
            break;
		case 'userlist':
			document.querySelector('[data-option="userlist"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="userlist"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="userlist"]')?.children[1].classList.add('hidden')
			break;
		case 'userdetails':
			document.querySelector('[data-option="userdetails"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="userdetails"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="userdetails"]')?.children[1].classList.add('hidden')
			break;
		case 'tasksview':
			document.querySelector('[data-option="tasksview"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="tasksview"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="taskview"]')?.children[1].classList.add('hidden')
			break;
		default:
            document.querySelector('[data-option="dashboard"]')?.classList.add('currentNavItem');
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.remove(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[0].classList.add(...classListSpan)
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.remove('hidden')
			document.querySelector('[data-option="dashboard"]')?.children[1].classList.add('hidden')

	}
};
sessionValueStore();

navLogout?.addEventListener('click', () => {
	sessionStorage.removeItem('currentNavItem');
});

navLogo?.addEventListener('click', () => {
	sessionStorage.removeItem('currentNavItem');
});
