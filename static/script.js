function createElement(className, emoji) {
    const el = document.createElement("div");
    el.className = className;
    el.innerHTML = emoji;
    el.style.left = Math.random() * window.innerWidth + "px";
    el.style.animationDuration = (Math.random() * 3 + 2) + "s";
    document.body.appendChild(el);

    setTimeout(() => el.remove(), 5000);
}

setInterval(() => {
    createElement("star", "✨");
    createElement("love", "💖");
    createElement("flower", "🌸");
}, 400);
