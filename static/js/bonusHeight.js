const inputs = document.querySelectorAll('input')
const arr = [].slice.call(inputs)

arr.forEach((x) => {
	x.addEventListener('focus', increase)
	x.addEventListener('focusout', decrease)
})

function increase() {
	document.body.style.height = '210vh'
	document.querySelector('.bg').style.height = '210vh'
}

function decrease() {
	document.body.style.height = '100vh'
	document.querySelector('.bg').style.height = '100vh'
}