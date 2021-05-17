import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

#notify("Se acabo el tiempo!", "Tómate 5 minutos")