const inputEl = document.getElementById("userInput");
const outputEl = document.getElementById("vectorOutput");
const buttonEl = document.getElementById("embedBtn");

async function fetchEmbedding() {
	const text = inputEl.value.trim();

	if (!text) {
		outputEl.value = "Please enter some text first.";
		return;
	}

	buttonEl.disabled = true;
	buttonEl.textContent = "Loading...";
	outputEl.value = "Fetching vector...";

	try {
		const response = await fetch(`/embed?documents=${encodeURIComponent(text)}`);

		if (!response.ok) {
			throw new Error(`Request failed with status ${response.status}`);
		}

		const data = await response.json();
		outputEl.value = JSON.stringify(data.vector ?? [], null, 2);
	} catch (error) {
		outputEl.value = `Error: ${error.message}`;
	} finally {
		buttonEl.disabled = false;
		buttonEl.textContent = "Get Vector";
	}
}

buttonEl.addEventListener("click", fetchEmbedding);
