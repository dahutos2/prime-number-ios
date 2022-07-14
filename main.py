import kivy
import japanize_kivy
import timeout_decorator
kivy.require('2.0.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.utils import get_color_from_hex


# Registering the custom fonts
def mersenne(x):
    num = x+1
    count = 0
    while num != 1:
        if num%2 == 0:
            num = num//2
            count += 1
        else:
            return False
    return count
@timeout_decorator.timeout(3)
def prime_count(number):
    mersenne_num = mersenne(number)
    if mersenne_num:
        s = 4
        M = (2**mersenne_num) - 1
        for n in range(2,mersenne_num):
            s = (s**2 -2) % M
        if s == 0:
            return str(number) + "*1"
    if number < 2:
        return str(number) + "*1"
    elif number == 2:
        return str(number) + "*1"
    prime_num_list = []
    first_num = number
    while number != 1:
        if number%2 == 0:
            number = number//2
            prime_num_list.append(2)
            continue
        for count in range(3, int(number**0.5) + 1, 2):
            if number % count == 0:
                prime_num_list.append(count)
                number = number//count
                break
        else:
            prime_num_list.append(number)
            number = 1
    if len(prime_num_list) == 1:
        return str(prime_num_list[0]) + "*1"
    prime_set = sorted(list(set(prime_num_list)))
    prime_set_list = []
    for set_num in prime_set:
        set_count = prime_num_list.count(set_num)
        if set_count != 1:
            prime_set_list.append(str(set_num) + "**" + str(set_count))
        else:
            prime_set_list.append(str(set_num))
    prime_num = str(prime_set_list).replace(
                ',', '*').translate(str.maketrans(
                {"'": None, "[": None, "]": None}))
    return prime_num

class Calkvlator(App):
    clear_bool = BooleanProperty(False)

    def print_number(self, number):
        if self.clear_bool:
            self.clear_display()

        text = "{}{}".format(self.root.display.text, number)
        self.root.display.text = text
    @timeout_decorator.timeout(3)
    def code_change(self):
        if self.clear_bool:
            self.clear_bool = False
        try:
            text = str(eval(self.root.display.text + "*" + "-1"))
            self.root.display.text = text
        except timeout_decorator.timeout_decorator.TimeoutError:
            text = "タイムアウトです。"
            self.root.display.text = text
        except Exception:
            pass
            
    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False

        text = "{}{}".format(self.root.display.text, operator)
        self.root.display.text = text

    def clear_display(self):
        self.root.display.text = ""
        self.clear_bool = False

    def del_char(self):
        self.root.display.text = self.root.display.text[:-1]
        
    @timeout_decorator.timeout(3)
    def calculate(self):
        try:
            text = str(eval(self.root.display.text))
            self.root.display.text = text
            self.clear_bool = True
        except timeout_decorator.timeout_decorator.TimeoutError:
            text = "タイムアウトです。"
            self.root.display.text = text
            self.clear_bool = True
        except Exception:
            pass
    def exponential_notation(self):
        try:
            text = "{:e}".format(eval(self.root.display.text))
            self.root.display.text = text
            self.clear_bool = True
        except:
            pass
            
    def prime_judge(self):
        try:
            text = prime_count(eval(self.root.display.text))
            self.root.display.text = text
            self.clear_bool = True
        except timeout_decorator.timeout_decorator.TimeoutError:
            text = "タイムアウトです。"
            self.root.display.text = text
            self.clear_bool = True
        except Exception:
            pass

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Calkvlator().run()

