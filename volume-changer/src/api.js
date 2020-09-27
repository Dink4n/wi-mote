export const handleKeyPress = async (key) => {
	await fetch(`/keypress?key=${key}`).then((response) =>
		response.json().then((data) => {
			console.log(`key: ${data.key}`);

			if (data.status === "OK") {
				console.log(`%cstatus: ${data.status}`, "color:green;");
			} else {
				console.log(`%cstatus: ${data.status}`, "color:red;");
			}
		})
	);
};
