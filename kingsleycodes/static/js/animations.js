// Lightweight animations: entrance, small neon pulse
document.addEventListener('DOMContentLoaded', ()=>{
document.querySelectorAll('section').forEach((el, i)=>{
el.style.opacity = 0;
setTimeout(()=>{ el.style.transition = 'opacity 600ms ease-out'; el.style.opacity = 1; }, 100 * i);
});


// Simple hero canvas glow animation
const hero = document.getElementById('hero-canvas');
if(hero) {
let t = 0;
setInterval(()=>{
t += 0.02;
hero.style.background = `radial-gradient(circle at ${50 + Math.sin(t)*10}% ${50 + Math.cos(t)*6}%, rgba(34,211,238,0.18), transparent 40%), linear-gradient(135deg, rgba(15,23,42,0.9), rgba(10,10,20,0.6))`;
}, 40);
}
});

document.addEventListener("DOMContentLoaded", () => {
  const fadeElements = document.querySelectorAll(".animate-fade-in");
  fadeElements.forEach((el, i) => {
    el.style.opacity = 0;
    setTimeout(() => {
      el.style.transition = "opacity 1s ease-in-out";
      el.style.opacity = 1;
    }, 300 * i);
  });

  const slideUpElements = document.querySelectorAll(".animate-slide-up");
  slideUpElements.forEach((el, i) => {
    el.style.transform = "translateY(50px)";
    el.style.opacity = 0;
    setTimeout(() => {
      el.style.transition = "all 1s ease-out";
      el.style.transform = "translateY(0)";
      el.style.opacity = 1;
    }, 400 * i);
  });
});
