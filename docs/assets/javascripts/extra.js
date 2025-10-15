// Botón volver arriba
document.addEventListener('DOMContentLoaded', function () {
    // Crear el botón
    const backToTopButton = document.createElement('a');
    backToTopButton.innerHTML = '↑';
    backToTopButton.className = 'back-to-top';
    backToTopButton.href = '#';
    backToTopButton.title = 'Volver arriba';

    // Agregar al body
    document.body.appendChild(backToTopButton);

    // Mostrar/ocultar según scroll
    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });

    // Scroll suave al hacer click
    backToTopButton.addEventListener('click', function (e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Animación de entrada para tarjetas
document.addEventListener('DOMContentLoaded', function () {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    // Observar todas las tarjetas
    const cards = document.querySelectorAll('div[style*="border-radius"][style*="padding"]');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
});