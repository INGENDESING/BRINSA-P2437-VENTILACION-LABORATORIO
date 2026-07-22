document.addEventListener("DOMContentLoaded", () => {
    // Interacción suave: efecto de resplandor que sigue al ratón en las tarjetas
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
            card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(56, 189, 248, 0.05) 0%, rgba(30, 41, 59, 0.4) 50%)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.background = `rgba(30, 41, 59, 0.4)`;
        });
    });
});
