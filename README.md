# Sistema Web Flask sin módulo de citas

Este proyecto Flask incluye una página de servicios, galería, contacto, promociones y panel admin. No incluye módulo de agendar citas.

## Uso local

```bash
pip install -r requirements.txt
python app.py
```

## Despliegue en Render

- Añade un nuevo Web Service
- Carga este proyecto
- Usa Python 3.10+
- Usa `gunicorn app:app` como comando de inicio
