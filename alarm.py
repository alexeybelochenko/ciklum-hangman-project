import datetime
import winsound
import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Budilnik')

def budilnik(date, hours, minutes):
    int(date)
    int(hours)
    int(minutes)
    now1=datetime.datetime.now()
    then=datetime.datetime(now1.year,now1.month,date,hours,minutes,00,000000)
    i=0
    while i < 1:
        now1 = datetime.datetime.now()
        now=datetime.datetime(now1.year,now1.month,now1.day,now1.hour,now1.minute,00,000000)
        
        if now == then:
            #winsound.PlaySound('good.wav',winsound.SND_FILENAME)
            i+=1
        else:
            continue

def  create():
     window1 = tk.Tk()
     f_top = tk.Frame(window1)
     f_bot= tk.Frame(window1)
     entry_date =tk.Entry(f_top , width = 25)
     entry_hours=tk.Entry(f_top, width = 25)
     entry_minutes=tk.Entry(f_top, width = 25)


     
     f_top.pack(side="top")
     f_bot.pack(side="bottom")
     entry_date.pack(side="left", padx = 10)
     entry_hours.pack(side="left", padx = 10)
     entry_minutes.pack(side="left", padx = 10) 
         

     
     
     ready =tk.Button(f_top, text = "Ready", command = budilnik(entry_date.get(), entry_hours.get(), entry_minutes.get()),  width = 5, height = 1)
     ready.pack(side="right")





new_bud= tk.Button(window, text = "New budilnik", command=create, width = 20, height = 2)
new_bud.pack() 




window.mainloop()