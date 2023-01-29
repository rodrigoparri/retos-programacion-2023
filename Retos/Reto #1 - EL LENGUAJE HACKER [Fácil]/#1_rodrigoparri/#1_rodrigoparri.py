
class HackerTranslater:

    dictionary = {
        "a":"4",
        "b":"i3",
        "c":"[",
        "d":")",
        "e":"3",
        "f":"|=",
        "g":"&",
        "h":"#",
        "i":"1",
        "j":",_|",
        "k":">|",
        "l":"1",
        "m":"/\/",
        "n":"^/",
        "ñ":"~/",
        "o":"0",
        "p":"|*",
        "q":"(_,)",
        "r":"l2",
        "s":"5",
        "t":"7",
        "u":"(_)",
        "v":"\/",
        "w":"\/\/",
        "x":"><",
        "y":"j",
        "z":"2"
    }

    def __init__(self, path_in, path_out):
        self.path_in = path_in
        self.path_out = path_out

    def translate(self):
        text_out = ""
        with open(self.path_in, "r") as file:

            for line in file:
                line = line.strip().replace(" ","")

                for letter in line:
                    letter = letter.lower()

                    if letter in self.dictionary:
                        line = line.replace(letter, self.dictionary[letter])

                line = line + "\n"
                text_out += line

        return text_out

    def exporter(self, text):

        with open(self.path_out, "w") as file:
            file.write(text)


if __name__ == "__main__":

    msg = HackerTranslater("conversion_text", "translated_text")
    translation = msg.translate()
    msg.exporter(translation)