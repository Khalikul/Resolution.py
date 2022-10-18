import win32api
import win32con
import pywintypes
width=int(input('Enter the Width: '))
height=int(input('Enter the Height: '))

devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = width
devmode.PelsHeight = height

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)
