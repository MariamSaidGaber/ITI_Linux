print("hello")

######### Importing Libraries	#######
import pyautogui		# This library to interact with gui
import webbrowser		# This library to open browser
import time				# This library is using to wait few seconds



webbrowser.register('chrom',
					None,
					webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'))


link = 'https://www.facebook.com/'			# Facebook profile link

webbrowser.get('chrom').open_new(link) 		# open the facebook link
time.sleep(7)								# will wait for 7 seconds until opening 

pyautogui.hotkey('ctrl','f')				# Will search in the browser 
pyautogui.typewrite("What's on your mind?")	# Search for this sentance "What's on your mind?"
pyautogui.press('enter')					# By keyboard press on enter
pyautogui.press('escape')					# By keyboard press on escape
pyautogui.press('enter')					# By keyboard press on enter

time.sleep(4)								# will wait for 4 seconds until opening 

pyautogui.typewrite("If you have the power to make someone happy, do it.")	# Write this sentance in a post 

pyautogui.click(650,585)					# To click on post we have to use mouse
