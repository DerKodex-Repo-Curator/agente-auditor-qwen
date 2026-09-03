# 🛡️ Agente Auditor de Vulnerabilidades con Qwen 3.8 y Open WebUI

Herramienta en Python diseñada para conectar modelos locales (Ollama) con entornos de pruebas mediante Tool Calling nativo en Open WebUI.

## 🚀 Cómo usar esta herramienta en Open WebUI

1. En tu Open WebUI, ve a **Workspace (Espacio de trabajo)** -> **Tools (Herramientas)**.
2. Pulsa en el botón **+** para crear una nueva herramienta.
3. Copia y pega el código íntegro del archivo `inspector.py` de este repositorio.
4. Guarda los cambios.
5. Ve a **Modelos**, edita tu agente de Qwen (o crea uno nuevo) y en la sección **Herramientas (Tools)** activa esta función.
6. ¡Listo! Al pedirle que audite una ruta local o web de pruebas, el modelo ejecutará la herramienta de forma autónoma.
