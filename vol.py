from pynput.keyboard import Key,Controller
import time
import pyautogui

# keyboard = Controller()
def soundChange(percentChange):
	if abs(percentChange)>0.2:
		print(abs(int(percentChange*10)))
		for _ in range(abs(int(percentChange*5))):
			if percentChange > 0 :
				print("Increasing vol.........")
				# keyboard.press(Key.media_volume_up)
				# keyboard.release(Key.media_volume_up)
				pyautogui.press('volumeup')
				time.sleep(0.01)
			else:
				print("Decreasing vol.........")
				# keyboard.press(Key.media_volume_down)
				# keyboard.release(Key.media_volume_down)
				pyautogui.press('volumedown')
				time.sleep(0.01)
	time.sleep(0.2) 

