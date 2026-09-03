"""
title: Inspector de Servidores y Archivos para Open WebUI
author: Ricardo Bertran
version: 1.0.0
description: Herramienta de auditoría para inspeccionar endpoints, leer archivos y analizar cabeceras de servidores locales de prueba.
"""

import requests
import re
from typing import Dict, Any

class Tools:
    def __init__(self):
        # Límite de caracteres para evitar saturar el contexto de la tarjeta gráfica
        self.max_chars = 2500

    def inspeccionar_recurso(self, url: str) -> str:
        """
        Inspecciona una URL o ruta de un servidor web local para leer su contenido, cabeceras o listar archivos expuestos.
        :param url: La URL completa o ruta del servidor a auditar (por ejemplo: http://localhost:3000/robots.txt).
        :return: El contenido del archivo o la respuesta del servidor limitada a caracteres seguros.
        """
        try:
            # Validamos que la URL sea válida
            if not url.startswith("http://") and not url.startswith("https://"):
                return "Error de validación: La URL debe comenzar por http:// o https://"

            # Petición HTTP controlada con timeout para evitar que el modelo quede bloqueado
            response = requests.get(url, timeout=5, verify=False)
            
            codigo_estado = response.status_code
            cabeceras = dict(response.headers)
            contenido = response.text

            # Filtro de longitud para proteger la memoria VRAM del agente
            if len(contenido) > self.max_chars:
                contenido_filtrado = contenido[:self.max_chars] + f"\n\n[AVISO: Salida truncada a {self.max_chars} caracteres para optimizar contexto VRAM]"
            else:
                contenido_filtrado = contenido

            resumen = (
                f"=== ESTADO: {codigo_estado} ===\n"
                f"Servidor: {cabeceras.get('Server', 'No especificado')}\n"
                f"Content-Type: {cabeceras.get('Content-Type', 'Desconocido')}\n"
                f"=== CONTENIDO DEL RECURSO ===\n"
                f"{contenido_filtrado}"
            )
            return resumen

        except requests.exceptions.RequestException as e:
            return f"Error al conectar con el servidor: {str(e)}"
