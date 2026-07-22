import pyautogui as enzo
import time

enzo.hotkey('win','r')
enzo.write('mspaint', interval=0.2)
enzo.press('enter')
time.sleep(2)
enzo.hotkey('win','up')
enzo.moveTo(400, 400)
enzo.dragTo(480, 400)
enzo.dragTo(480, 480)
enzo.dragTo(400, 480)
enzo.dragTo(400, 400)

# enzo.write("Garchomp", interval=0.1)
# enzo.FAILSAFE=False
# enzo.moveTo(1919, 0, 2 )
# enzo.click()
