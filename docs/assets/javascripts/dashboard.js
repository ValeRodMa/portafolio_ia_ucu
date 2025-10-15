// Dashboard Interactivo - JavaScript

class DashboardAnimations {
    constructor() {
        this.init();
    }

    init() {
        this.setupIntersectionObserver();
        this.updateLastUpdateTime();
        this.startRealTimeUpdates();
    }

    setupIntersectionObserver() {
        const observerOptions = {
            threshold: 0.3,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateElement(entry.target);
                }
            });
        }, observerOptions);

        // Observar elementos animables
        document.querySelectorAll('.metric-card').forEach(card => observer.observe(card));
        document.querySelectorAll('.unit-card').forEach(card => observer.observe(card));
        document.querySelectorAll('.tech-category').forEach(category => observer.observe(category));
        document.querySelectorAll('.dataset-card').forEach(card => observer.observe(card));
        document.querySelectorAll('.achievement').forEach(achievement => observer.observe(achievement));
    }

    animateElement(element) {
        if (element.classList.contains('metric-card')) {
            this.animateMetricCard(element);
        } else if (element.classList.contains('unit-card')) {
            this.animateUnitCard(element);
        } else if (element.classList.contains('tech-category')) {
            this.animateTechCategory(element);
        } else if (element.classList.contains('dataset-card')) {
            this.animateDatasetCard(element);
        } else if (element.classList.contains('achievement')) {
            this.animateAchievement(element);
        }
    }

    animateMetricCard(card) {
        const numberElement = card.querySelector('.metric-number');
        const progressBar = card.querySelector('.progress-bar');

        if (numberElement && !numberElement.classList.contains('animated')) {
            const target = parseInt(numberElement.dataset.target);
            this.animateCounter(numberElement, target);
            numberElement.classList.add('animated');
        }

        if (progressBar && !progressBar.classList.contains('animated')) {
            const progress = parseInt(progressBar.dataset.progress);
            setTimeout(() => {
                progressBar.style.width = `${progress}%`;
            }, 500);
            progressBar.classList.add('animated');
        }
    }

    animateUnitCard(card) {
        const progressFill = card.querySelector('.unit-progress-fill');

        if (progressFill && !progressFill.classList.contains('animated')) {
            const progress = parseInt(progressFill.dataset.progress);
            setTimeout(() => {
                progressFill.style.width = `${progress}%`;
            }, 300);
            progressFill.classList.add('animated');
        }

        // Animar tags con delay escalonado
        const tags = card.querySelectorAll('.topic-tag');
        tags.forEach((tag, index) => {
            tag.style.opacity = '0';
            tag.style.transform = 'translateY(10px)';
            setTimeout(() => {
                tag.style.transition = 'all 0.3s ease';
                tag.style.opacity = '1';
                tag.style.transform = 'translateY(0)';
            }, 600 + (index * 100));
        });
    }

    animateTechCategory(category) {
        const techFills = category.querySelectorAll('.tech-fill');

        techFills.forEach((fill, index) => {
            if (!fill.classList.contains('animated')) {
                const width = parseInt(fill.dataset.width);
                setTimeout(() => {
                    fill.style.width = `${width}%`;
                }, index * 200);
                fill.classList.add('animated');
            }
        });
    }

    animateDatasetCard(card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';

        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    }

    animateAchievement(achievement) {
        if (achievement.classList.contains('unlocked')) {
            achievement.style.opacity = '0';
            achievement.style.transform = 'scale(0.9)';

            setTimeout(() => {
                achievement.style.transition = 'all 0.4s ease';
                achievement.style.opacity = '1';
                achievement.style.transform = 'scale(1)';
            }, 100);
        }
    }

    animateCounter(element, target) {
        const duration = 2000;
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;

        const updateCounter = () => {
            if (current < target) {
                current += increment;
                element.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        };

        updateCounter();
    }

    updateLastUpdateTime() {
        const lastUpdateElement = document.getElementById('last-update');
        if (lastUpdateElement) {
            const now = new Date();
            const timeString = now.toLocaleString('es-ES', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            });
            lastUpdateElement.textContent = timeString;
        }
    }

    startRealTimeUpdates() {
        // Simular actualizaciones en tiempo real
        setInterval(() => {
            this.updateLastUpdateTime();
            this.simulateDataUpdates();
        }, 60000); // Actualizar cada minuto
    }

    simulateDataUpdates() {
        // Simular pequeñas variaciones en las métricas
        const metricNumbers = document.querySelectorAll('.metric-number');

        metricNumbers.forEach(number => {
            if (Math.random() < 0.1) { // 10% de probabilidad de actualización
                const currentValue = parseInt(number.textContent);
                const variation = Math.random() > 0.5 ? 1 : -1;
                const newValue = Math.max(0, currentValue + variation);

                // Animación sutil de cambio
                number.style.transform = 'scale(1.1)';
                number.style.color = '#e74c3c';

                setTimeout(() => {
                    number.textContent = newValue;
                    number.style.transform = 'scale(1)';
                    number.style.color = '#2c3e50';
                }, 200);
            }
        });
    }

    // Método para agregar interactividad a las tarjetas
    addCardInteractivity() {
        document.querySelectorAll('.metric-card, .dataset-card, .achievement').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-5px) scale(1.02)';
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) scale(1)';
            });
        });
    }

    // Método para agregar tooltips informativos
    addTooltips() {
        const tooltipData = {
            '.metric-card.practices': 'Prácticas completadas del curso de Ingeniería de Datos',
            '.metric-card.datasets': 'Datasets únicos analizados en profundidad',
            '.metric-card.visualizations': 'Gráficos y visualizaciones creadas',
            '.metric-card.tools': 'Herramientas y tecnologías dominadas'
        };

        Object.entries(tooltipData).forEach(([selector, text]) => {
            const element = document.querySelector(selector);
            if (element) {
                element.title = text;
            }
        });
    }

    // Método para filtrar contenido
    addFiltering() {
        // Agregar botones de filtro si es necesario
        const filterButtons = document.querySelectorAll('.filter-btn');

        filterButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                const filter = e.target.dataset.filter;
                this.filterContent(filter);
            });
        });
    }

    filterContent(filter) {
        const cards = document.querySelectorAll('.dataset-card, .achievement');

        cards.forEach(card => {
            if (filter === 'all' || card.classList.contains(filter)) {
                card.style.display = 'block';
                card.style.opacity = '1';
            } else {
                card.style.opacity = '0.3';
            }
        });
    }

    // Método para exportar métricas
    exportMetrics() {
        const metrics = {
            practices: document.querySelector('.metric-card.practices .metric-number').textContent,
            datasets: document.querySelector('.metric-card.datasets .metric-number').textContent,
            visualizations: document.querySelector('.metric-card.visualizations .metric-number').textContent,
            tools: document.querySelector('.metric-card.tools .metric-number').textContent,
            lastUpdate: document.getElementById('last-update').textContent
        };

        console.log('Portfolio Metrics:', metrics);
        return metrics;
    }
}

// Función para crear gráficos simples con ASCII
class SimpleCharts {
    static createProgressChart(container, data) {
        const maxValue = Math.max(...data.values);
        const chart = data.labels.map((label, index) => {
            const value = data.values[index];
            const percentage = (value / maxValue) * 100;
            const barLength = Math.floor(percentage / 5);
            const bar = '█'.repeat(barLength) + '░'.repeat(20 - barLength);
            return `${label.padEnd(15)} ${bar} ${value}`;
        }).join('\n');

        if (container) {
            container.innerHTML = `<pre>${chart}</pre>`;
        }
    }
}

// Inicializar dashboard cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    const dashboard = new DashboardAnimations();
    dashboard.addCardInteractivity();
    dashboard.addTooltips();

    // Agregar funcionalidad de exportar métricas (para debugging)
    window.exportMetrics = () => dashboard.exportMetrics();

    // Agregar smooth scroll mejorado
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Agregar efectos de parallax sutil
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.metric-card');

        parallaxElements.forEach((element, index) => {
            const speed = 0.5 + (index * 0.1);
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
});





