#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import tkinter.messagebox
import random

#設定初值
postion_A = 0
postion_B = 0
times = 0    
computer_numbers = []
answer = ''

def reset_all():
    global postion_A, postion_B, computer_numbers, times, answer
    postion_A = 0
    postion_B = 0
    times = 1    
    computer_numbers = answer_numbers()
    random.shuffle(computer_numbers)
    answer = f'我 第{times}次 猜你心中的數字是 {computer_numbers[0]}'
    
def main(var_A,var_B):            
    global postion_A, postion_B, computer_numbers, times, answer
    postion_A = int(var_A)
    postion_B = int(var_B)    
    
    if not postion_A == 4:
        times += 1        
        
        #取得下一次答案清單
        next_numbers (computer_numbers,postion_A,postion_B)                        
        
        #去掉這次的答案
        computer_numbers.pop(0)
        
        #如果答案清單沒有資料時
        if len(computer_numbers) == 0:
            tkinter.messagebox.showinfo(title = '錯誤訊息', message = '請檢查你的提示, 有問題喔!!!')
            game_button.configure(text = '再玩一次')
            prompt_A_entry.delete(0, 'end')
            prompt_B_entry.delete(0, 'end')
            answer_label.configure(text = '')
            reset_all()
        else:    
            #清除上一次的提示
            prompt_A_entry.delete(0, 'end')
            prompt_B_entry.delete(0, 'end')        
        
            #答案清單更新
            answer += f'\n我 第{times}次 猜你心中的數字是 {computer_numbers[0]}'
            answer_label.configure(text = answer)
    else:
        tkinter.messagebox.showinfo(title = '結束訊息', message = '哈哈....我答對了')
        game_button.configure(text = '再玩一次')
        prompt_A_entry.delete(0, 'end')
        prompt_B_entry.delete(0, 'end')
        answer_label.configure(text = '')
        reset_all()

#列出所有排列的副程式    
def answer_numbers():
    return_numbers = []
    n1s = [str(i) for i in range(0,10)]
    for n1 in n1s:
        n2s = n1s[:]
        n2s.remove(n1)
        for n2 in n2s:
            n3s = n2s[:]
            n3s.remove(n2)
            for n3 in n3s:
                n4s = n3s[:]
                n4s.remove(n3)
                for n4 in n4s:
                    return_numbers.append(n1+n2+n3+n4)
    return return_numbers

#核對數字及位置對不對的副程式
def get_postion (numbers_1,numbers_2):
    in_postion = 0
    not_in_postion = 0
    for number in numbers_1:
        if number in numbers_2:
            if numbers_1.index(number) == numbers_2.index(number):
                in_postion += 1
            else:
                not_in_postion += 1
                
    return in_postion,not_in_postion


#去掉不對答案的副程式
def next_numbers (return_list,answer_A,answer_B):
    flag_A = 0
    flag_B = 0    
    for number in return_list[1:]:
        flag_A, flag_B = get_postion (number,return_list[0])        
        if not (flag_A == answer_A and flag_B == answer_B):                
                return_list.remove(number)               
                
#檢查提示是否為數字格式及數字範圍
def check_number():
    var_A = prompt_A_entry.get()
    var_B = prompt_B_entry.get()
    flag = True
    
    if not var_A.isdigit():
        tkinter.messagebox.showinfo(title = '錯誤訊息', message = '提示A 輸入的不是數字')        
        flag = False
    else:
        if int(var_A) > 4:
            tkinter.messagebox.showinfo(title = '錯誤訊息', message = '提示A 數字不可大於4')            
            flag = False
            
    if not var_B.isdigit():
        tkinter.messagebox.showinfo(title = '錯誤訊息', message = '提示B 輸入的不是數字')        
        flag = False
    else:
        if int(var_B) > 4:
            tkinter.messagebox.showinfo(title = '錯誤訊息', message = '提示B 數字不可大於4')
            flag = False
            
    if flag:
        if int(var_A) + int(var_B) > 4:
            tkinter.messagebox.showinfo(title = '錯誤訊息', message = '提示A 與 提示B 合計不可大於4')
            flag = False
            
    if not flag:
        prompt_A_entry.delete(0, 'end')
        prompt_B_entry.delete(0, 'end')
    else:
        main(var_A,var_B)

def game_start():
    reset_all()
    answer_label.pack(side = tk.TOP)
    prompt_A_label.pack(side = tk.LEFT)
    prompt_A_entry.pack()
    prompt_B_label.pack(side = tk.LEFT)
    prompt_B_entry.pack()  
    button_prompt.pack(side = tk.BOTTOM)
    answer_label.configure(text = answer)


# In[4]:


window = tk.Tk()
window.title('猜數字')
window.geometry('800x600')
window.configure(background = 'white')

#規則說明框
rule_frame = tk.Frame(window)
rule_frame.pack(side = tk.TOP)
rule_show_frame = tk.Frame(rule_frame)
rule_show_frame.pack(side = tk.TOP)
rule_button_frame = tk.Frame(rule_frame)
rule_button_frame.pack(side = tk.BOTTOM)

rule_label = tk.Label(rule_show_frame, font = ('Arial' , 20), text='請 0 到 9 選4個數字,\n排列組合後做為你選的數字,\n數字 0 可以放在最前面,\n我會根據你的回答,\n猜出你的數字')
rule_label.pack(side = tk.TOP)

game_button = tk.Button(rule_button_frame, font = ('Arial' , 20), text = '開始遊戲', command = game_start)
game_button.pack(side = tk.LEFT)
close_button = tk.Button(rule_button_frame, font = ('Arial' , 20), text = '結束遊戲', command = window.destroy)
close_button.pack(side = tk.RIGHT)

#答案框
answer_frame = tk.Frame(window, bg = 'white')
answer_frame.pack(side = tk.TOP)
answer_label = tk.Label(answer_frame, font = ('Arial' , 12), bg = 'white', text = '')


#提示框
font_prompt = ('Arial', 12)
color_A = 'red'
color_B = 'blue'
prompt_frame = tk.Frame(window, bg = 'white')
prompt_frame.pack(side = tk.BOTTOM)

prompt_A_frame = tk.Frame(prompt_frame, bg = 'white')
prompt_A_frame.pack(side = tk.TOP)
prompt_B_frame = tk.Frame(prompt_frame, bg = 'white')
prompt_B_frame.pack(side = tk.TOP)

prompt_A_label = tk.Label(prompt_A_frame, font = font_prompt, fg = color_A, text='提示(A) 位置對, 數字也對的有:')
prompt_A_entry = tk.Entry(prompt_A_frame, font = font_prompt, fg = color_A)


prompt_B_label = tk.Label(prompt_B_frame, font = font_prompt, fg = color_B, text='提示(B) 數字對, 但位置不對的有:')
prompt_B_entry = tk.Entry(prompt_B_frame, font = font_prompt, fg = color_B)

button_prompt = tk.Button(prompt_frame, font = font_prompt, text = '送出提示', command = check_number)


window.mainloop()                


# In[ ]:





# In[ ]:




