class AppErrorBaseClass(Exception):
    """Clase base para errores de la aplicación"""
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ObjectNotFound(AppErrorBaseClass):
    """Excepción cuando un objeto no es encontrado"""
    def __init__(self, message="Objeto no encontrado"):
        super().__init__(message, status_code=404)
