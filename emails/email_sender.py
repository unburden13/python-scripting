import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Chulo'
email['to'] = 'gonzalez.juandavid13@gmail.com'
email['subject'] = 'Nice to meet you.'

email.set_content(html.substitute(name='Juan'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # extended HELO
    smtp.starttls()  # encryption
    smtp.login('chulo.chirrete@gmail.com', 'kkswtafkqcthdvmj')
    # for gmail, credential errors most probably occur because no app-passwords have been created
    smtp.send_message(email)
    print('zero kills')