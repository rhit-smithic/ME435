async function sendCommand(command) {
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;
}

function main() {
    document.querySelector("#ledon").onclick = () => {
        sendCommand("LED ON");
    }
    document.querySelector("#ledoff").onclick = () => {
        sendCommand("LED OFF");
    }
    document.querySelector("#flash").onclick = () => {
        var count = document.querySelector("#count").value;
        var period = document.querySelector("#period").value;
        sendCommand(`FLASH ${count} ${period}`);
    }
}

main();