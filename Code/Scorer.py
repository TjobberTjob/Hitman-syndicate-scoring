import tkinter as tk
from datetime import datetime
import pyautogui


map_scores = {'Miami': 0.8, 'Santa Fortuna': 1.2, 'Mumbai': 0.8, 'Whittleton': 0,
              'Sgail': 1.2, 'New York': 1, 'Haven': 0.6,  'Paris': 0.55, 'Sapienza': 0.3,
              'Marrakesh': 0.8, 'Bangkok': 1.25, 'Colorado': 0.75, 'Hokkaido': 1.5, 'Dubai': 0.5,
              'Dartmoor': 0.3, 'Berlin': 0.3, 'Chongqing': 0.6, 'Mendoza': 0.1, 'Ambrose': 0.8}

map_coords = {'Miami': (1208, 403), 'Santa Fortuna': (1217, 434), 'Mumbai': (1440, 415), 'Whittleton': (1227, 369),
              'Sgail': (1322, 338), 'New York': (1221, 376), 'Haven': (1437, 442),  'Paris': (1335, 362), 'Sapienza': (1346, 372),
              'Marrakesh': (1314, 397), 'Bangkok': (1480, 425), 'Colorado': (1165, 382), 'Hokkaido': (1542, 372), 'Dubai': (1412, 407),
              'Dartmoor': (1323, 357), 'Berlin': (1351, 356), 'Chongqing': (1490, 395), 'Mendoza': (1223, 500), 'Ambrose': (1468, 432)}


def screenshot_info():
    global last
    screencap = pyautogui.screenshot()
    coord_colors = [screencap.getpixel(map_coords[f]) for f in map_coords]
    score_sum = [[loc, map_scores[loc]] for f, loc in zip(coord_colors, map_coords) if f[0] > 200 and (f[1], f[2]) == (0, 0)]
    area_names = [f[0] for f in score_sum]
    text = sum([f[1] for f in score_sum])
    multiplier = 1.25 if all(f in ['Mendoza', 'Whittleton'] for f in area_names) else 1 if any(f in ['Mendoza', 'Whittleton'] for f in area_names) else 2
    text = round(text * multiplier, 1) if len(score_sum) >= 3 else ''
    last = last if len(score_sum) < 3 else datetime.now()
    return text 


def superimpose_text(text):
    color = "black" if isinstance(text, str) else 'green' if text < 2 else 'yellow' if text < 4 else 'red'
    # update the label
    label.config(text=text, fg=color)


def update_text():
    global last
    text = screenshot_info()
    superimpose_text(text)
    update_time = 50 if (datetime.now() - last).seconds < 2 else 500
    root.after(update_time, update_text)


last = datetime.now()
print('Running!')
first = datetime.now()
# instantiate Tk and set the window properties here
root = tk.Tk()
# root.iconbitmap(default='Code/icon.ico')
root.geometry("+1380+480")
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "white")
root.configure(background='white')
label = tk.Label(root, text='', font=('Times New Roman', '65'), fg='black', bg='white')
label.pack()
update_text()  # start the update loop
root.mainloop()
