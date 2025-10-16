document.addEventListener("DOMContentLoaded", function () {
  const html = document.documentElement;
  const toggleBtn = document.getElementById("theme-toggle");
  const icon = document.getElementById("theme-icon");

  function setIcon(isDark) {
    icon.innerHTML = isDark
      ? '<path d="M10 2a8 8 0 100 16 8 8 0 010-16zM10 0v2m0 16v2m8-10h2M0 10H2m13.657-6.343l1.414 1.414M3.929 16.071l1.414-1.414m0-9.9L3.929 3.93m13.142 13.142l-1.414-1.414"/>'
      : '<path d="M17.293 13.293A8 8 0 116.707 2.707a8 8 0 0010.586 10.586z"/>';
  }

  const userPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const storedTheme = localStorage.getItem("theme");

  const isDark = storedTheme
    ? storedTheme === "dark"
    : userPrefersDark;

  html.classList.toggle("dark", isDark);
  setIcon(isDark);

  toggleBtn.addEventListener("click", () => {
    html.classList.toggle("dark");
    const nowDark = html.classList.contains("dark");
    localStorage.setItem("theme", nowDark ? "dark" : "light");
    setIcon(nowDark);
  });
});