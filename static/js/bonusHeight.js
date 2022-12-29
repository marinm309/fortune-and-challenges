const inputs = document.querySelectorAll('input')
	inputs[inputs.length - 1].addEventListener('focus', function(){
		document.body.style.height = '150vh'
		document.querySelector('.bg').style.height = '150vh'
	})
	inputs[inputs.length - 1].addEventListener('focusout', function(){
		document.body.style.height = '100vh'
		document.querySelector('.bg').style.height = '100vh'
	})