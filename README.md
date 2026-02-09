# 🎬 Movie API Backend — Flask Edition

Este es el **cerebro lógico** de una plataforma de gestión cinematográfica. El proyecto no solo funciona como un catálogo de películas, sino que sirve como base para implementar prácticas de **Seguridad de Software** y **Arquitectura de Sistemas**, alineado a mis aspiraciones en **DevSecOps**.

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.x
* **Framework:** [Flask](https://flask.palletsprojects.com/) (Micro-framework para el desarrollo ágil de APIs)
* **Persistencia:** **JSON** (Manejo de datos estructurados localmente)
* **Gestión de Entorno:** **Virtualenv** (Aislamiento de dependencias)

---

## 🧠 Arquitectura e Implementación
El proyecto fue diseñado bajo el principio de **Separación de Responsabilidades**, permitiendo que la API sea escalable y fácil de auditar.

### Lo que implementé:
1. **Manejo de Datos en JSON:** Lógica para lectura y escritura de archivos planos, simulando el comportamiento de una base de datos para prototipado rápido.
2. **Validación de Entradas:** Estructuración de validaciones para asegurar la integridad de la información recibida.
3. **Modularización:** Organización del código para desacoplar las rutas de la lógica de negocio.

---

## 🛡️ Enfoque en Ciberseguridad (Aspirante a DevSecOps)
Como ingeniero con enfoque en seguridad, utilicé este proyecto para aplicar conceptos de protección de software:
* **Sanitización de Datos:** Implementación de lógica para mitigar riesgos por entradas maliciosas.
* **Manejo Seguro de Errores:** Configuración de respuestas HTTP personalizadas para evitar la exposición de la estructura interna del servidor (fuga de información).
* **Entorno Aislado:** Uso de `virtualenv` para garantizar la reproducibilidad y seguridad de las librerías.

---
