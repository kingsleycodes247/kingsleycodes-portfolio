// Theme toggle + auto detect
(function(){
const html = document.documentElement;
const toggle = document.getElementById('theme-toggle');
const userPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const saved = localStorage.getItem('theme');
function applyTheme(theme){
if(theme === 'dark') html.classList.add('dark');
else html.classList.remove('dark');
}
const initial = saved || (userPrefersDark ? 'dark' : 'light');
applyTheme(initial);
toggle.addEventListener('click', ()=>{
const now = html.classList.contains('dark') ? 'light' : 'dark';
applyTheme(now);
localStorage.setItem('theme', now);
});
})();