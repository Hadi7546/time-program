





import easygui as gui


title    ='Time program'
buttons  =('Refresh','Exit')

while 5!=1:
    caption="chert"
    button=gui.buttonbox(caption, title, buttons)
    
    #خروج از مین لوپ
    if button=='Exit':
        break