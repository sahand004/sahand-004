
from tkinter import *
from tkinter import messagebox
from turtle import window_height

from setuptools import Command


# creat Specialized variables
def specialized_variables():
    global bmi,abf_female,abf_male,lbm_male,lbm_female,ibw_male,ibw_female,bmr_female,bmr_male,weight_float
    weight_float = float(entry_weigth.get())
    height_float = float(entry_height.get())
    height_float = height_float *0.01
    age_float = float(entry_age.get())
    purpose_fat_float = float(entry_purpose_fat.get())*0.01
    
    bmi = weight_float/(height_float*height_float)

    abf_male = (1.2*bmi)+(0.23*age_float)-(10.0)-(5.4)
    abf_female = ((1.2*weight_float)/(height_float**2))+(0.23*age_float)-(5.4)

    lbm_male = (abf_male - weight_float)
    lbm_female = (abf_female - weight_float)

    ibw_male = (lbm_male/(1-purpose_fat_float))
    ibw_female = (lbm_female/(1-purpose_fat_float))

    bmr_male = (6.8*age_float)-(height_float*5)+(weight_float*13.7)+66
    bmr_female = (4.7*age_float)-(height_float*1.8)+(weight_float*9.6)+655
 

    
# creat config label
def run_prog():
    specialized_variables()

    if radio_btn.get() == "مرد":
        label_0.config(text=f':آقای {entry_name.get()} تحلیل بدنی شما بشرح زیر می باشد')
        label_1.config(text=f'توده خالص بدنی: {round(lbm_male,3)}')
        label_2.config(text=f'وزن ایده آل: {round(ibw_male,3)}')
        label_3.config(text=f'متابولیسم پایه: {round(bmr_male,3)}')
        label_4.config(text=f'درصد چربی فعلی: {round(abf_male,3)}')
        label_5.config(text=f'{round(bmi,3)} :BMI')

    elif radio_btn.get() == "زن":
        label_0.config(text=f':خانم {entry_name.get()} تحلیل بدنی شما بشرح زیر می باشد')
        label_1.config(text=f'توده خالص بدنی: {round(lbm_female,3)}')
        label_2.config(text=f'وزن ایده آل: {round(ibw_female,3)}')
        label_3.config(text=f'متابولیسم پایه: {round(bmr_female,3)}')
        label_4.config(text=f'درصد چربی فعلی: {round(abf_female,3)}')
        label_5.config(text=f'{round(bmi,3)} :BMI')




win = Tk()

win.title('Sports Calculator')
win.geometry('590x300')
win.resizable(width=False, height=False)
win.iconphoto(False, PhotoImage(file='D:\\Devs\\TK\\Sport Project\\icons8-gym-60.png'))


filename = PhotoImage(file = 'D:\\Devs\\TK\\Sport Project\\sports-png-30297.png')
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# creat labels input  and  entry
Label(win,text='اسم').grid(column="0",row="0")
entry_name = Entry(win)
entry_name.grid(column="1",row="0")

Label(win,text='فامیلی').grid(column="2",row="0")
entry_fname = Entry(win)
entry_fname.grid(column="3",row="0")

Label(win,text='سن').grid(column="0",row="1")
entry_age = Entry(win)
entry_age.grid(column="1",row="1")

Label(win,text='درصد چربی هدف').grid(column="2",row="1")
entry_purpose_fat=Entry(win)
entry_purpose_fat.grid(column="3",row="1")

Label(win,text='(cm)قد').grid(column="0",row="2")
entry_height=Entry(win)
entry_height.grid(column="1",row="2")

Label(win,text='(kg)وزن').grid(column="2",row="2")
entry_weigth=Entry(win)
entry_weigth.grid(column="3",row="2")


# creat radibutton  for male and female
radio_btn = StringVar()
radio_btn.set('مرد')

Radiobutton(win,text='مرد',variable=radio_btn,value='مرد',command = run_prog).grid(column="0",row="3")
Radiobutton(win,text='زن',variable=radio_btn,value='زن').grid(column="1",row="3")

#creat button for rub
button_rub = Button(win,text='     اجرا     ',command=run_prog).grid(column="3",row="3")

# creaat lables output
Label(win,text='').grid(column="0",row="4")

label_0 = Label(win,text='')
label_0.grid(column="0",row="5")

label_1 = Label(win,text='توده خالص بدنی:')
label_1.grid(column="0",row="6")

label_2 = Label(win,text='وزن ایده آل:')
label_2.grid(column="0",row="7")

label_3 = Label(win,text='متابولیسم پایه:')
label_3.grid(column="0",row="8")

label_4 = Label(win,text='درصد چربی فعلی:')
label_4.grid(column="0",row="9")

label_5 = Label(win,text='BMI:')
label_5.grid(column="0",row="10")



win.mainloop()