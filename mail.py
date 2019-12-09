import smtplib
from email.mime.text import MIMEText
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

def mensagem(var1,var2):
    try:
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        username = 'email.aacd@gmail.com'
        password = 'infernus1598'

        from_addr = 'email.aacd@gmail.com'
        to_addrs = ['aacd.email@gmail.com']
        '''senha: juju1598'''

        message = MIMEText('Foi notificado que o cofre: ' +var1+ ' localizado: ' +var2+ ' está pronto para ser recolhido.')
        message['subject'] = 'Alerta de recolhimento!'
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()
        print('email Enviado!')
        
    except Exception:
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 587
        username = 'email.aacd@gmail.com'
        password = 'infernus1598'

        from_addr = 'email.aacd@gmail.com'
        to_addrs = ['aacd.email@gmail.com']

        message = MIMEText('O Cofre de id: ' +var1+ ' e endereço: ' +var2+ ' foi solicitado recolhimento.')
        message['subject'] = 'Alerta de recolhimento!'
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()
        print('email Enviado!')