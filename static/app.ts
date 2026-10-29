let list = document.getElementById("containerList");

async function load() {
    let response = await fetch("/api/containers");
    let data = await response.json();
    console.log(data);
    if (list) {
        for (let c of data) {
            let item = document.createElement("li");
            let icon = c.status === "running" ? "🟢" : "🔴";
            item.innerText = icon + " " + c.name + " (" + c.status + ")";
            list.appendChild(item);
        }
    }
}
load();
