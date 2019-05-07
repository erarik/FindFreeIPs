from tkinter import *
from tkinter.ttk import *
import ipaddress
import socket
from subprocess import call
import os


def check_ping(hostname):
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = True #"Network Active"
    else:
        pingstatus = False #"Network Error"

    return pingstatus

    
def get_free_ip(subnet, nb):
    free=[]

    print("searching subnet: {}".format(str(subnet)))
    for addr in ipaddress.ip_network(subnet).hosts():
       if(len(free) >= nb):
          return free
       try:
          print(socket.gethostbyaddr(str(addr)))
       except:
          if(check_ping(str(addr))==False):
              print("FREE: {}".format(str(addr)))
              free.append(str(addr))
          pass
    return free



class FreeIp:

    def __init__(self, window):
        self.window = window
        window.title("Search free ip within the subnet")

        self.label = Label(window, text="Subnet")
        self.label.grid(column=0, row=0)

        self.entry = Entry(window)
        self.entry.insert(0,"10.20.132.0/24")
        self.entry.grid(column=1, row=0)

        self.label = Label(window, text="Number of free ips to find")
        self.label.grid(column=2, row=0)

        var =IntVar()
        var.set(5)
        self.nb = Spinbox(window, from_=0, to=10, width=5, textvariable=var)
        self.nb.grid(column=3,row=0)

        self.rearch_button = Button(window, text="Search", command=lambda: self.search())
        self.rearch_button.grid(column=4, row=0)

        self.text = Text(window)
        self.text.grid(column=0, row=1, columnspan=5)


    def search(self):
        subnet = self.entry.get()
        free_subnets_p1 = get_free_ip(subnet, int(self.nb.get()))

        #self.ips.insert(0,' - '.join(free_subnets_p1))
        self.text.insert(INSERT, "Free IPs - {}\r\n".format(subnet))
        for ip in free_subnets_p1:
              self.text.insert(INSERT, "{}\r\n".format(ip))
        self.text.insert(INSERT, "Search ended\r\n")

if __name__=='__main__':
    window = Tk()
    FreeIp(window)
    window.mainloop()
    


