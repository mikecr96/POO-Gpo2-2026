"""
EN RESUMEN:
Si usamos Singleton, no usamos __init__
"""

class Portapapeles:
    _unica_instancia = None

    # Método constructor
    # No se DEBE hacer override al new
    # __new__ -> __init__ -> ...
    def __new__(cls):
        if cls._unica_instancia is None:
            print("[SISTEMA]: Creando el portapapeles.")
            cls._unica_instancia = super(Portapapeles, cls).__new__(cls)
            cls.texto_guardado = ""
            # SIEMPRE debe retornar al objeto
        return cls._unica_instancia

    def copiar(self, texto):
        self.texto_guardado = texto
        print(f"Texto ({texto}) copiado al portapapeles")        
    
    def pegar(self):
        return self.texto_guardado
        
if __name__ == "__main__":
    app_word = Portapapeles()
    app_word.copiar("Hola mundo mundial. Saludos a todos.")
    print(f"Word tiene copiado en memoria: {app_word.pegar()}")

    app_browser = Portapapeles()
    print(f"Browser tiene copiado en memoria: {app_browser.pegar()}")
    print(f"Word tiene copiado en memoria: {app_word.pegar()}")
