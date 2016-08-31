import webapp2
# caesar.py

ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text, rotation):
    answer = ""
    for char in text:
        answer += rotate_char(char, rotation)
    return answer

form="""
<form method = "post">
    <br>
    <label>
        rotate by
        <input type = "number", name = "rotate-by">
    </label>
    <label>
        What's your message
        <input type = "text", name = "message">
        <input type = "submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    def post(self):
        rotateBy = self.request.get("rotate-by")
        message = self.request.get("message")
        print (message)
        print (rotateBy)
        self.response.write(encrypt (message, int(rotateBy)))

app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
