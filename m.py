import tkinter as tk
import socket
import tkinter
import tkinter.messagebox
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd1 = "GET"
cmd2 = " "
cmd4 = " "
cmd5 = "HTTP/1.0\r\n\r\n"

list = {}

root = tk.Tk()
root.title("socket_GUI")
root.geometry("500x500")
e = tk.Entry(root)

e.pack()


def insert_point():
    cmd3 = str(e.get())
    cmd = cmd1 + cmd2 + cmd3 + cmd4 + cmd5
    cmd = cmd.encode()
    mysock.send(cmd)
    if len(cmd3)!=0:
     while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end='')
        t1.insert('insert', data)
    else :
        tkinter.messagebox.showerror('´íÎó', 'ÇëÊäÈëµØÖ·')
    mysock.close()




b1 = tk.Button(root, text=" ·ÃÎÊµØÖ·", width=15, height=2, command=insert_point)
b1.pack()

t1 = tk.Text(root)
t1.pack(fill="x")

root.mainloop()
