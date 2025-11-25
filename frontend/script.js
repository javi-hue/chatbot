const chatbox = document.getElementById("chatbox");
const msgInput = document.getElementById("msg");

async function sendMessage() {
    const text = msgInput.value;
    if (text.trim() === "") return;

    chatbox.innerHTML += `<div class='user'><b>Tú:</b> ${text}</div>`;
    msgInput.value = "";

    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    chatbox.innerHTML += `<div class='bot'><b>Bot:</b> ${data.response}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}
