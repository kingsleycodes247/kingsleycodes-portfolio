module.exports = {
  darkMode: 'class',
  content: ['./templates/**/*.html', './**/templates/**/*.html'],
  theme: {
    extend: {
      animation: {
        'glow-slow': 'glow 6s ease-in-out infinite alternate',
        'gradient-x': 'gradient-x 5s ease infinite',
        'pulse-slow': 'pulse 5s ease-in-out infinite'
      },
      keyframes: {
        glow: {
          '0%, 100%': { opacity: '0.2', transform: 'scale(1)' },
          '50%': { opacity: '0.6', transform: 'scale(1.05)' }
        },
        'gradient-x': {
          '0%, 100%': { 'background-position': '0% 50%' },
          '50%': { 'background-position': '100% 50%' }
        }
      }
    }
  },
  plugins: []
}
