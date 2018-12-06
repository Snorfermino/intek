import os


def env_hello():
    if 'fr_FR' in os.environ['LANG']:
        return "Bonjour!"
    else:
        return "Hello!"