export const handleKeyPress = async (key) => {
	await fetch(`/keypress?key=${key}`)

	console.log(`Key : ${key}`)
};
