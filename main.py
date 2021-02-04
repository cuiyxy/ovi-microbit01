def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(0, 10))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.ROLLERSKATE)
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play_tone(988, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.show_leds("""
    . # . # .
    . . . # .
    . # . # .
    . . . . .
    . . . . .
    """)