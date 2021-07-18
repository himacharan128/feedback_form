from tkinter import *
import os
window = Tk()
window.title("SUGGESTIONS BOX")
window.geometry('1100x150')
window.configure(background = "light blue")
def take_text():
    global a1,b1,c1,d1
    suggestion1 = a1.get()
    suggestion2 = b1.get()
    suggestion3 = c1.get()
    suggestion4 = d1.get()
    filename='feedback_file'
    for i in range(2):
    	if os.path.isfile("./"+filename):
    		f=open(filename,'a')
    		data='person-1--->'+suggestion1+'\nperson-2--->'+suggestion2+'\nperson-3--->'+suggestion3+'\nperson-4--->'+suggestion4+'\n'+'*'*80+'\n'
    		f.write(data)
    		break
    	else:
    		data='*'*80+'\n'+' '*37+'SUGGESTIONS\n'+'*'*80
    		f=open(filename,"w")
    		f.write(data + "\n")
    		f.close()
    		continue
    window.destroy()
a = Label(window ,text = "person-1",bg='pink')
a.grid(row = 0,column = 0)
b = Label(window ,text = "person-2",bg='pink')
b.grid(row = 1,column = 0)
c = Label(window ,text = "person-3",bg='pink')
c.grid(row = 2,column = 0)
d = Label(window ,text = "person-4",bg='pink')
d.grid(row = 3,column = 0)
a1 = Entry(window,width=100)
a1.grid(row = 0,column = 1)
b1 = Entry(window,width=100)
b1.grid(row = 1,column = 1)
c1 = Entry(window,width=100)
c1.grid(row = 2,column = 1)
d1 = Entry(window,width=100)
d1.grid(row = 3,column = 1)
btn =Button(window ,text="Submit",command=take_text)
btn.grid(row=4,column=1)
window.mainloop()