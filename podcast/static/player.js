function saveProgress(audioId) {
    let audio = document.getElementById(audioId);
    localStorage.setItem(audioId + "_time", audio.currentTime);
}

function toggleFavorite(id, title, audioSrc) {
    let favorite = JSON.parse(localStorage.getItem("favorite")) || [];

    if (!favorite.find(e => e.id === id)) {
        favorite.push({
            id: id,
            title: title,
            src: audioSrc
        });
        localStorage.setItem("favorite", JSON.stringify(favorite));
        alert("Added to favorite");
    } else {
        alert("Episode in favorite alredy");
    }
}

function loadFavorite() {
    let favorite = JSON.parse(localStorage.getItem("favorite")) || [];
    let list = document.getElementById("favList");

    list.innerHTML = "";

    if (favorite.length === 0) {
        list.innerHTML = "<p>No episodes in favorite yet</p>";
        return;
    }

    favorite.forEach(e => {
        let div = document.createElement("div");
        div.className = "episode";

        div.innerHTML = `
            <h3>${e.title}</h3>
            <audio controls>
                <source src="${e.src}" type="audio/mpeg">
            </audio>
        `;

        list.appendChild(div);
    });
}

function clearFavorite() {
    if (confirm("Ara you sure?")) {
        localStorage.removeItem("favorite");
        location.reload();
    }
}

window.onload = function () {

    let audios = document.getElementsByTagName("audio");
    for (let audio of audios) {
        let time = localStorage.getItem(audio.id + "_time");
        if (time) {
            audio.currentTime = time;
        }
    }

    const params = new URLSearchParams(window.location.search);
    const podcastId = params.get("podcast");

    if (podcastId) {
        const episodes = document.querySelectorAll(".episode");
        episodes.forEach(ep => {
            if (ep.dataset.podcast !== podcastId) {
                ep.style.display = "none";
            }
        });
    }

    if (document.getElementById("favList")) {
        loadFavorite();
    }
};
