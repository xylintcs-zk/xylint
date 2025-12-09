document.addEventListener("DOMContentLoaded", () => {
    const chat = document.getElementById("chat");
    const form = document.getElementById("chat-form");
    const input = document.getElementById("cmd");

    function scrollToBottom() {
        chat.scrollTop = chat.scrollHeight;
    }

    scrollToBottom();

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const cmd = input.value.trim();
        if (!cmd) return;

        input.value = "";

        const formData = new FormData();
        formData.append("cmd", cmd);

        const response = await fetch("/command", {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        });

        const botText = await response.text();

        if (cmd.toLowerCase() === "clear chat" || botText === "CLEAR") {
            window.location.reload();
        } else {
            const userMsg = document.createElement("p");
            userMsg.className = "my-msg";
            userMsg.textContent = cmd;
            chat.appendChild(userMsg);

            const botMsg = document.createElement("p");
            botMsg.className = "response";
            botMsg.textContent = botText;
            chat.appendChild(botMsg);
            chat.scrollTop = chat.scrollHeight;
        }
    });
});