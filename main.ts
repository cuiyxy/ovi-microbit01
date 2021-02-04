input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(input.temperature())
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(randint(0, 10))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Rollerskate)
})
music.playTone(988, music.beat(BeatFraction.Half))
music.playTone(262, music.beat(BeatFraction.Whole))
basic.showLeds(`
    . # . # .
    . . . # .
    . # . # .
    . . . . .
    . . . . .
    `)
