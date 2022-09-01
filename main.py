from pynput import mouse,keyboard
import threading
import time

counter = [0]

def on_click(x,y,button, pressed):
	if pressed:
		counter[0] += 1

def on_press(key):
	counter[0] += 1

listenerKey = keyboard.Listener(
    on_press=on_press)
listenerKey.start()

listenerMouse = mouse.Listener(
    on_click=on_click)
listenerMouse.start()

def findAPM(timeInterval, listpos):
	multiplier = 60/timeInterval

	while True:
		counterstart = counter[0]
		time.sleep(timeInterval)
		actions = counter[0] - counterstart
		APM = actions * multiplier
		APMs[listpos] = APM

threads = []
APMs = []
for i in range(0,60):
	threads.append(threading.Thread(target=findAPM, args= (i+1,i) ) )
	APMs.append(0)
	threads[i].start()

# sixtyAPM = threading.Thread(target=findAPM, args= (10,0))
# fiveAPM = threading.Thread(target=findAPM, args= (5,1))
# oneAPM = threading.Thread(target=findAPM, args= (1,2))

# sixtyAPM.start()
# fiveAPM.start()
# oneAPM.start()

while True:
	print(max(APMs))