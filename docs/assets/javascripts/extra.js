// Forzar descarga de notebooks desde GitHub
(function() {
    'use strict';
    
    function forceDownload(event) {
        event.preventDefault();
        event.stopPropagation();
        
        const link = event.currentTarget;
        const url = link.getAttribute('href');
        const filename = url.split('/').pop() || 'notebook.ipynb';
        
        // Usar fetch para descargar el archivo
        fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/octet-stream'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.blob();
        })
        .then(blob => {
            // Crear un enlace temporal para descargar
            const downloadUrl = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = downloadUrl;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            
            // Limpiar después de un momento
            setTimeout(() => {
                document.body.removeChild(a);
                window.URL.revokeObjectURL(downloadUrl);
            }, 100);
        })
        .catch(error => {
            console.error('Error descargando archivo:', error);
            // Fallback: intentar descarga directa
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.target = '_blank';
            document.body.appendChild(a);
            a.click();
            setTimeout(() => document.body.removeChild(a), 100);
        });
        
        return false;
    }
    
    // Ejecutar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDownloadHandlers);
    } else {
        initDownloadHandlers();
    }
    
    function initDownloadHandlers() {
        // Encontrar todos los enlaces que apuntan a GitHub raw con .ipynb
        const downloadLinks = document.querySelectorAll('a.download-notebook, a[href*="github.com"][href*="raw"][href*=".ipynb"]');
        
        downloadLinks.forEach(function(link) {
            // Remover listeners anteriores si existen
            link.removeEventListener('click', forceDownload);
            // Agregar nuevo listener con capture phase para interceptar antes
            link.addEventListener('click', forceDownload, true);
            // También prevenir el comportamiento por defecto
            link.onclick = forceDownload;
        });
    }
    
    // También escuchar cambios dinámicos en el DOM
    const observer = new MutationObserver(function(mutations) {
        initDownloadHandlers();
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();

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