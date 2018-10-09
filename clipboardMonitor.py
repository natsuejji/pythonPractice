# -*- coding: utf-8 -*-  
import win32clipboard
import win32api
import time

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def reset_clipboard():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText("")
    win32clipboard.CloseClipboard()
    time.sleep(0.1)

def main():
    s=[]
    while(1):
        if win32api.GetKeyState(81) == 1: 
            break
        else:
            content = get_clipboard() #取得剪貼簿
            if content not in s and content != "":
                s.append(content) 
                print(content)
            time.sleep(0.1)
    
    fn = input ('please enter your file name:')
    with open('clipFile/'+fn+'.txt', 'w',encoding='utf8') as f:
        for item in s:
            f.write("%s\n" % item)
        print('completed....')


if __name__ == '__main__':
    reset_clipboard()
    main()