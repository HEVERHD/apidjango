(function () {
	const btnDelete = document.getElementById('.btnDelete');

	btnDelete.forEach((btn) => {
		btn.addEventListener('click', (e) => {
			const confirmation = confirm('¿delete this company?');
			if (!confirmation) {
				e.preventDefault();
			}
		});
	});
})();
