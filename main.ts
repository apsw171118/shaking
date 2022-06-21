input.onButtonPressed(Button.A, function () {
    var_num = 0
})
input.onGesture(Gesture.Shake, function () {
    var_num += 1
})
let var_num = 0
var_num = 0
basic.forever(function () {
    basic.showNumber(var_num)
})
