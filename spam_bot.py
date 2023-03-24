import pyautogui as pg,webbrowser as web, time as tm
web.open('https://web.whatsapp.com/send?phone=NumberPhone')
tm.sleep(10)
for i in range(100):
    pg.write('*Message')
    pg.press('enter')
    print('Mesagge: '+str(i+1))
    pass