from telebot import types


class Markup:
    def __init__(self, buttons):
        self.buttons = buttons

    @property
    def markup(self):
        mrup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = self.buttons.copy()
        button_am = len(buttons)
        last_button = None
        if button_am % 2 == 1:
            last_button = buttons.pop()
        for i in range(button_am // 2):
            mrup.add(buttons[i*2], buttons[i*2 + 1])
        if last_button:
            mrup.add(last_button)
        return mrup
