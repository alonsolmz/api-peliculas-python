import os

from app import create_app

# Usa la configuración por defecto si no se especifica APP_SETTINGS_MODULE
settings_module = os.getenv('APP_SETTINGS_MODULE', 'config.default')
app = create_app(settings_module)

# Crea la BD si no existe
with app.app_context():
    from app.db import db
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)