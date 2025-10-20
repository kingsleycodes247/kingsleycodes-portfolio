document.addEventListener("DOMContentLoaded", () => {
  const container = document.createElement("div");
  container.classList.add("fixed", "inset-0", "z-0", "overflow-hidden", "pointer-events-none");
  document.body.appendChild(container);

  for (let i = 0; i < 6; i++) {
    const orb = document.createElement("div");
    orb.classList.add(
      "absolute", "rounded-full", "blur-3xl", "opacity-40", "animate-glow-slow",
      "bg-gradient-to-r", "from-indigo-500", "to-violet-600"
    );

    orb.style.width = `${150 + Math.random() * 200}px`;
    orb.style.height = orb.style.width;
    orb.style.left = `${Math.random() * 100}%`;
    orb.style.top = `${Math.random() * 100}%`;
    orb.style.animationDelay = `${Math.random() * 5}s`;

    container.appendChild(orb);
  }
});
