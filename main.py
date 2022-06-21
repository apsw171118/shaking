def on_gesture_shake():
    global var_num
    var_num += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

var_num = 0

def on_forever():
    basic.show_number(var_num)
basic.forever(on_forever)

input.button_is_pressed(Button.A)
var_num = 0