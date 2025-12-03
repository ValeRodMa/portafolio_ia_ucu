/**
 * Widget de Chatbot para MkDocs
 * Integración del chatbot con IA en el portfolio
 */

(function() {
    'use strict';

    // Configuración
    // Detectar si estamos en producción o desarrollo
    const isProduction = window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1';
    // Si tienes un backend desplegado, cambia esta URL por la de tu servicio (ej: Render, Railway, etc.)
    const API_URL = isProduction 
        ? 'https://portafolio-ia-ucu.onrender.com/chat'  // URL de producción en Render
        : 'http://localhost:5000/chat';
    const CHATBOT_ID = 'portfolio-chatbot';

    // Crear HTML del chatbot
    function createChatbotHTML() {
        const chatbotHTML = `
            <div id="${CHATBOT_ID}" class="portfolio-chatbot">
                <div class="chatbot-header">
                    <h3>¿Dudas? ¡Pregúntame!</h3>
                    <button class="chatbot-close" onclick="toggleChatbot()">×</button>
                </div>
                <div class="chatbot-messages" id="chatbot-messages">
                    <div class="chatbot-message bot">
                        <p>¡Hola! 👋 Soy el asistente de Valentín. Puedo responder preguntas sobre las prácticas, técnicas, datasets y contenido del portfolio. ¿En qué puedo ayudarte?</p>
                        ${isProduction ? '<p style="margin-top: 10px; font-size: 12px; color: #666;"><em>Nota: Puede que tu respuesta tarde un poco en aparecer, por favor espera un momento mientras se procesa.</em></p>' : ''}
                    </div>
                </div>
                <div class="chatbot-input-container">
                    <input 
                        type="text" 
                        id="chatbot-input" 
                        placeholder="Pregunta sobre el portfolio..."
                        onkeypress="handleChatbotKeyPress(event)"
                    />
                    <button onclick="sendChatbotMessage()">Enviar</button>
                </div>
            </div>
            <button class="chatbot-toggle" onclick="toggleChatbot()">
                💬
            </button>
        `;

        // Agregar al body
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
    }

    // CSS del chatbot
    function addChatbotCSS() {
        const style = document.createElement('style');
        style.textContent = `
            .portfolio-chatbot {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 400px;
                height: 600px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                display: none;
                flex-direction: column;
                z-index: 1000;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
            
            .portfolio-chatbot.active {
                display: flex;
            }
            
            .chatbot-header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px;
                border-radius: 12px 12px 0 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .chatbot-header h3 {
                margin: 0;
                font-size: 16px;
                font-weight: 600;
            }
            
            .chatbot-close {
                background: none;
                border: none;
                color: white;
                font-size: 24px;
                cursor: pointer;
                padding: 0;
                width: 30px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .chatbot-messages {
                flex: 1;
                overflow-y: auto;
                padding: 20px;
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            
            .chatbot-message {
                max-width: 80%;
                padding: 12px 16px;
                border-radius: 12px;
                line-height: 1.5;
            }
            
            .chatbot-message.user {
                align-self: flex-end;
                background: #667eea;
                color: white;
            }
            
            .chatbot-message.bot {
                align-self: flex-start;
                background: #f0f0f0;
                color: #333;
            }
            
            .chatbot-message .sources {
                margin-top: 10px;
                font-size: 12px;
                color: #666;
            }
            
            .chatbot-message .sources a {
                color: #667eea;
                text-decoration: none;
                margin-right: 8px;
            }
            
            .chatbot-input-container {
                display: flex;
                padding: 15px;
                border-top: 1px solid #e0e0e0;
                gap: 10px;
            }
            
            .chatbot-input-container input {
                flex: 1;
                padding: 10px;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                font-size: 14px;
            }
            
            .chatbot-input-container button {
                padding: 10px 20px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 600;
            }
            
            .chatbot-input-container button:hover {
                background: #5568d3;
            }
            
            .chatbot-toggle {
                position: fixed;
                bottom: 90px;
                right: 20px;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                font-size: 24px;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                z-index: 998;
            }
            
            .chatbot-toggle:hover {
                transform: scale(1.1);
                transition: transform 0.2s;
            }
            
            .chatbot-loading {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid #f3f3f3;
                border-top: 3px solid #667eea;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
    }

    // Funciones globales
    window.toggleChatbot = function() {
        const chatbot = document.getElementById(CHATBOT_ID);
        const toggle = document.querySelector('.chatbot-toggle');
        
        if (chatbot.classList.contains('active')) {
            chatbot.classList.remove('active');
            toggle.style.display = 'block';
        } else {
            chatbot.classList.add('active');
            toggle.style.display = 'none';
        }
    };

    window.sendChatbotMessage = function() {
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        // Agregar mensaje del usuario
        addMessage(message, 'user');
        input.value = '';
        
        // Deshabilitar input mientras procesa
        input.disabled = true;
        
        // Mostrar loading con ID único más robusto
        const loadingId = 'loading-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
        addMessage('', 'bot', true, loadingId);
        
        // Enviar a la API
        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remover loading ANTES de agregar respuesta
            const loadingElement = document.getElementById(loadingId);
            if (loadingElement) {
                loadingElement.remove();
            }
            
            // Rehabilitar input
            input.disabled = false;
            input.focus();
            
            // Agregar respuesta
            // Procesar el texto de la respuesta con Markdown
            const responseHTML = markdownToHTML(data.response);
            
            // Agregar fuentes como HTML directo (sin procesar Markdown)
            let sourcesHTML = '';
            if (data.sources && data.sources.length > 0) {
                sourcesHTML = '<div class="sources"><strong>Fuentes:</strong> ';
                sourcesHTML += data.sources.map(s => 
                    `<a href="${s.url}" target="_blank">${s.title}</a>`
                ).join(', ');
                sourcesHTML += '</div>';
            }
            
            // Agregar mensaje con HTML ya procesado
            addMessageHTML(responseHTML + sourcesHTML, 'bot');
        })
        .catch(error => {
            // Remover loading en caso de error
            const loadingElement = document.getElementById(loadingId);
            if (loadingElement) {
                loadingElement.remove();
            }
            
            // Rehabilitar input
            input.disabled = false;
            input.focus();
            
            // Mensaje más amigable según el tipo de error
            let errorMessage = 'Lo siento, hubo un error al procesar tu pregunta. ';
            if (isProduction) {
                errorMessage += 'El servicio del chatbot no está disponible en este momento. Por favor, intenta más tarde.';
            } else {
                errorMessage += 'Asegúrate de que el servidor backend esté corriendo en http://localhost:5000';
            }
            
            addMessage(errorMessage, 'bot');
            console.error('Error:', error);
        });
    };

    window.handleChatbotKeyPress = function(event) {
        if (event.key === 'Enter') {
            sendChatbotMessage();
        }
    };

    // Función para convertir Markdown básico a HTML
    function markdownToHTML(markdown) {
        if (!markdown) return '';
        
        // Escapar HTML existente para evitar XSS (pero preservar estructura)
        let html = markdown
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
        
        // Primero procesar código inline para protegerlo
        const codeBlocks = [];
        html = html.replace(/`([^`]+)`/g, (match, code) => {
            const id = `CODE_${codeBlocks.length}`;
            codeBlocks.push(code);
            return id;
        });
        
        // Negritas: **texto** o __texto__
        html = html.replace(/\*\*([^*]+?)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/__(.+?)__/g, '<strong>$1</strong>');
        
        // Cursiva: *texto* o _texto_ (solo si no está al inicio de línea con espacio después)
        html = html.replace(/([^\n*])\*([^*\n]+?)\*([^\n*])/g, '$1<em>$2</em>$3');
        html = html.replace(/([^\n_])_([^_\n]+?)_([^\n_])/g, '$1<em>$2</em>$3');
        
        // Restaurar código inline
        codeBlocks.forEach((code, i) => {
            html = html.replace(`CODE_${i}`, `<code style="background: #f0f0f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em;">${code}</code>`);
        });
        
        // Dividir en líneas para procesar listas y párrafos
        const lines = html.split('\n');
        const processedLines = [];
        let inList = false;
        let listType = null;
        let listItems = [];
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const trimmed = line.trim();
            
            // Detectar listas no ordenadas: - item o * item (al inicio de línea)
            const ulMatch = trimmed.match(/^[\-\*]\s+(.+)$/);
            // Detectar listas ordenadas: 1. item
            const olMatch = trimmed.match(/^\d+\.\s+(.+)$/);
            
            if (ulMatch) {
                if (!inList || listType !== 'ul') {
                    // Cerrar lista anterior si existe
                    if (inList) {
                        processedLines.push(`<${listType} style="margin: 10px 0; padding-left: 20px;">${listItems.join('')}</${listType}>`);
                        listItems = [];
                    }
                    inList = true;
                    listType = 'ul';
                }
                listItems.push(`<li>${ulMatch[1]}</li>`);
            } else if (olMatch) {
                if (!inList || listType !== 'ol') {
                    // Cerrar lista anterior si existe
                    if (inList) {
                        processedLines.push(`<${listType} style="margin: 10px 0; padding-left: 20px;">${listItems.join('')}</${listType}>`);
                        listItems = [];
                    }
                    inList = true;
                    listType = 'ol';
                }
                listItems.push(`<li>${olMatch[1]}</li>`);
            } else {
                // Cerrar lista si estamos en una
                if (inList) {
                    processedLines.push(`<${listType} style="margin: 10px 0; padding-left: 20px;">${listItems.join('')}</${listType}>`);
                    listItems = [];
                    inList = false;
                    listType = null;
                }
                
                // Procesar línea normal
                if (trimmed) {
                    processedLines.push(`<p style="margin: 8px 0;">${trimmed}</p>`);
                } else if (i < lines.length - 1) {
                    // Línea vacía entre párrafos
                    processedLines.push('');
                }
            }
        }
        
        // Cerrar lista si quedó abierta
        if (inList) {
            processedLines.push(`<${listType} style="margin: 10px 0; padding-left: 20px;">${listItems.join('')}</${listType}>`);
        }
        
        html = processedLines.join('');
        
        // Limpiar párrafos vacíos consecutivos
        html = html.replace(/(<p style="margin: 8px 0;"><\/p>\s*)+/g, '');
        
        return html;
    }

    function addMessage(text, type, isLoading = false, customId = null) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageId = customId || 'msg-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
        
        let contentHTML;
        if (isLoading) {
            contentHTML = '<div class="chatbot-loading"></div>';
        } else {
            // Convertir Markdown a HTML
            contentHTML = markdownToHTML(text);
        }
        
        const messageHTML = `
            <div class="chatbot-message ${type}" id="${messageId}">
                ${contentHTML}
            </div>
        `;
        
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        return messageId;
    }

    // Función para agregar mensaje con HTML ya procesado (sin Markdown)
    function addMessageHTML(html, type, customId = null) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageId = customId || 'msg-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
        
        const messageHTML = `
            <div class="chatbot-message ${type}" id="${messageId}">
                ${html}
            </div>
        `;
        
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        return messageId;
    }

    function removeMessage(messageId) {
        const message = document.getElementById(messageId);
        if (message) {
            message.remove();
        } else {
            // Fallback: buscar por clase si no se encuentra por ID
            const loadingMessages = document.querySelectorAll('.chatbot-loading');
            loadingMessages.forEach(msg => {
                if (msg.closest('.chatbot-message')) {
                    msg.closest('.chatbot-message').remove();
                }
            });
        }
    }

    // Inicializar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        addChatbotCSS();
        createChatbotHTML();
    }

})();

