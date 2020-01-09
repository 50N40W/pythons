import os
import board
from digitalio import DigitalInOut, Direction
import time
import touchio

# Set this to True to turn the touchpads into a keyboard
ENABLE_KEYBOARD = False

# Used if we do HID output, see below
if ENABLE_KEYBOARD:
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keycode import Keycode
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    kbd = Keyboard()
    layout = KeyboardLayoutUS(kbd)

#print(dir(board), os.uname()) # Print a little about ourselves

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

touches = [DigitalInOut(board.CAP0)]
for p in (board.CAP1, board.CAP2, board.CAP3):
    touches.append(touchio.TouchIn(p))

leds = []
for p in (board.LED4, board.LED5, board.LED6, board.LED7):
    led = DigitalInOut(p)
    led.direction = Direction.OUTPUT
    led.value = True
    time.sleep(0.25)
    leds.append(led)
for led in leds:
    led.value = False

cap_touches = [False, False, False, False]

active_led = 0x00
INIT = 4
RESTART = 3
GREEN = 2
YELLOW = 1
RED = 0
EXPIRED = -1

duration = 50
state = EXPIRED

def read_caps():
    t0_count = 0
    t0 = touches[0]
    t0.direction = Direction.OUTPUT
    t0.value = True
    t0.direction = Direction.INPUT
    # funky idea but we can 'diy' the one non-hardware captouch device by hand
    # by reading the drooping voltage on a tri-state pin.
    t0_count = t0.value + t0.value + t0.value + t0.value + t0.value + \
               t0.value + t0.value + t0.value + t0.value + t0.value + \
               t0.value + t0.value + t0.value + t0.value + t0.value
    cap_touches[0] = t0_count > 2
    cap_touches[1] = touches[1].raw_value > 3000
    cap_touches[2] = touches[2].raw_value > 3000
    cap_touches[3] = touches[3].raw_value > 3000
    return cap_touches

def type_alt_code(code):
    kbd.press(Keycode.ALT)
    for c in str(code):
        if c == '0':
            keycode = Keycode.KEYPAD_ZERO
        elif '1' <= c <= '9':
            keycode = Keycode.KEYPAD_ONE + ord(c) - ord('1')
        else:
            raise RuntimeError("Only number codes permitted!")
        kbd.press(keycode)
        kbd.release(keycode)
    kbd.release_all()

tcounter = 610
while True:
#    time_in_state = time.monotonic() - start_time
#    time_in_state += 0.1
#    if time_in_state > 300.0:
#        time_in_state = 0.0
    caps = read_caps()
    print(caps)
    if caps[0]:
        active_led = 0x01 
        state = RESTART
        # five seconds in restart, so count = 50
        duration = 50
        tcounter = 0
        if ENABLE_KEYBOARD:
            type_alt_code(234)
    if caps[1]:
        state = RESTART
        #expires after green and yellow, so 1 min in each.  
        # that's a count of 600 for each state
        duration = 600
        active_led = 0x02
        if ENABLE_KEYBOARD:
            type_alt_code(230)
    if caps[2]:
        state = RESTART
        # we want 5 minutes or 300 seconds or a count of 3000
        # for the gr + yellow.  That means duration should be
        # half that or 1500 for each.
        duration = 1500
        active_led = 0x04
        if ENABLE_KEYBOARD:
            type_alt_code(227)
    if caps[3]:
        duration = 3000
        active_led = 0x03
        active_led = 0x08
        if ENABLE_KEYBOARD:
            layout.write('https://www.digikey.com/python\n')

    if tcounter > 0:
        tcounter = tcounter - 1
    if tcounter < (duration >> 1) - (duration >> 2):
        active_led = active_led | 0x08
    if tcounter == 0:
        tcounter = duration
        prev_active_led = active_led
        if state == RESTART:
            tcounter = 50
            active_led = 0xff
            state = GREEN
        elif state == GREEN:
            active_led = 0x04
            state = YELLOW
        elif state == YELLOW:
            state = RED
            duration = 50
            active_led = 0x02
        elif state == RED:
            state = EXPIRED
            duration = 20
            active_led = 0x01
        elif state == EXPIRED:
            duration = 10
            active_led = 0x01

    leds[0].value = active_led & 0x01
    leds[1].value = active_led & 0x02
    leds[2].value = active_led & 0x04
    leds[3].value = active_led & 0x08
    time.sleep(0.1)
