from abc import ABC, abstractmethod
from datetime import datetime
import time

class CanalNotificaciones(ABC):
    # Método concreto (no abstracto)
    def registrar_log(self, destinatario):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"[LOG {hora_actual}] Iniciando proceso de envío para {destinatario}")

    @abstractmethod
    def enviar(self, mensaje, destinatario): 
        pass

# Clases concretas (no abstractas)
class NotificacionEmail(CanalNotificaciones):
    def enviar(self, mensaje, destinatario):
        self.registrar_log(destinatario)
        print(f"Conectando al servidor de correos SMTP...")
        print(f" -> Enviando Email a {destinatario} con el texto: \n{mensaje}\n")

class NotificacionSMS(CanalNotificaciones):
    def enviar(self, mensaje, destinatario):
        self.registrar_log(destinatario)
        print(f"Conectando a la BTS...")
        print(f" -> Enviando SMS al {destinatario} con el texto: \n{mensaje}\n")


# ----- PRUEBAS -----
def alertar_usuario(canal, mensaje, contacto):
    canal.enviar(mensaje, contacto)

# Instanciamos
email = NotificacionEmail()
sms = NotificacionSMS()

print("ALERTAS DEL SISTEMA".center(50, '-'))
print()

alertar_usuario(email, "Tu factura está lista", "usuario@empresa.com.mx")
# Dejar pasar 10 segundos
time.sleep(10)
alertar_usuario(sms, "Tu código de seguridad es 8923", "+52 55 12 34 55 66")
