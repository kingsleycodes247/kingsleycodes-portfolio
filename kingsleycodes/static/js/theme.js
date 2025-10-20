// theme.js — robust theme toggle with correct icon initialization
document.addEventListener("DOMContentLoaded", function () {
  const html = document.documentElement;
  const toggleBtn = document.getElementById("theme-toggle");
  const themeIcon = document.getElementById("theme-icon");

  // Helper to set icon classes
  function setIcon(isDark) {
    if (!themeIcon) return;
    // Remove both classes first to avoid duplicates
    themeIcon.classList.remove("fa-moon", "fa-sun");
    if (isDark) {
      themeIcon.classList.add("fa-sun");
    } else {
      themeIcon.classList.add("fa-moon");
    }
  }

  // Determine initial theme from localStorage or system preference
  const storedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  const isDark = storedTheme ? (storedTheme === "dark") : prefersDark;

  // Apply initial theme
  if (isDark) {
    html.classList.add("dark");
  } else {
    html.classList.remove("dark");
  }
  setIcon(isDark);

  // Toggle on click
  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      const nowDark = html.classList.toggle("dark");
      localStorage.setItem("theme", nowDark ? "dark" : "light");
      setIcon(nowDark);
    });
  }
});
