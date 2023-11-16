# OCP (Open/Close principle) o Principio de abierto/cerrado
# Las entidades de software debe estar abierta para la extensión pero cerrada para la modificación

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError # si no se implementa, lanzará un error

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}")

class NotificarTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")