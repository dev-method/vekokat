import Calculator from './Calculator.svelte';

const app = new Calculator({
	target: document.getElementById("svelte-container"),
	props: {
		name: 'dfggd'
	}
});

window.app = app;

export default app;