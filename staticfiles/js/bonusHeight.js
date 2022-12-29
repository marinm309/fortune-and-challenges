const inputs = document.querySelectorAll('input')
const arr = [].slice.call(inputs)
let cnt = 0

arr.forEach((x) => {
	x.addEventListener('focus', increase)
	x.addEventListener('focusout', decrease)
})

function increase() {
	if (cnt > 0) {
		document.body.style.height = '210vh'
		document.querySelector('.bg').style.height = '210vh'
	}
	cnt++
}

function decrease() {
	document.body.style.height = '100vh'
	document.querySelector('.bg').style.height = '100vh'
}