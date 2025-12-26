import pprint

import arcade
from arcade import Rect, XYWH

SCREEN_TITLE = "Название игры"
HEIGHT = 50
WIDTH = 50
ROW = 12
COL = 16
SCREEN_WIDTH = COL * WIDTH
SCREEN_HEIGHT = ROW * HEIGHT


class Red(arcade.Sprite):
    def __init__(self):
        super().__init__("Red.png", scale=0.02)
        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2

    def moving_right(self):
        for row in range(len(window.field)):
            if 5 in window.field[row]:
                c = window.field[row].index(5)
                if c != len(window.field[row]) - 1:
                    window.field[row][c + 1] = 5
                    window.field[row][c] = 0
                    break


class Blue(arcade.Sprite):
    def __init__(self):
        super().__init__("Blue.jpg", scale=0.1)
        self.center_x = 50
        self.center_y = 500


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Инициализация переменных игры
        self.blue_sprite = Blue()
        self.red_sprite = Red()
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def setup(self):
        """Инициализация/перезапуск игры"""
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.blue_sprite)
        arcade.draw_sprite(self.red_sprite)
        for y in range(ROW):
            for x in range(COL):
                arcade.draw_rect_outline(
                    rect=XYWH(
                        x=x * WIDTH + WIDTH / 2,
                        y=y * HEIGHT + HEIGHT / 2,
                        width=WIDTH,
                        height=HEIGHT
                    ),
                    color=arcade.color.YELLOW
                )

    def on_update(self, delta_time):
        """Логика игры (вызывается ~60 раз в секунду)"""
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.red_sprite.moving_right()
            pprint.pprint(self.field)

    def on_key_release(self, key, modifiers):
        """Отпускание клавиши"""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """Клик мышью"""
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """Движение мыши"""
        pass


window = MyGame()
window.setup()
arcade.run()


"""
В этом проекте сделать так, чтобы при нажатии на кнопку Д - объект также в игре двигался вправо
Когда движение вправо будет готово - сделать и в левую сторону, а также обучить нашего врага двигаться вниз

Отдельно попробовать разобраться с шириной квадратика (чтобы он ровно занимал всё пространство)
Просто спросить у дипсика, думаю, что поможет ;)

Если до этого все задания успешно выполнены, то добавить в игру таймер (вспомнить, как в пайтоне это создаётся)
ПО таймеру просто вызывать каждые 3 секунды функцию (мувинг_райт), чтобы он сам двигался в правую сторону

"""