from tkinter.ttk import *
from tkinter import *




class PhoneBook():

    
    def __init__(self, root):
########################################### Contacts details ############################################################
        self.data={  
   		"1": ["Oleta Level","+442032960159","10 London Wall, London EC2M 6SA, UK"],
   		"2": ["Maida Harju","+442032960899","Woodside House, 94 Tockholes Rd, Darwen BB3 1LL, UK"],
                "3": ["Lia Pigford","+442032960182","23 Westmorland Cl, Darwen BB3 2TQ, UK"],
                "4": ["Ghislaine Darden","+442032960427","20-24 Knowlesly Rd, Darwen BB3 2NE, UK"],
                "5": ["Jana Spitler","+442032960370","4 St Lucia Cl, Darwen BB3 0SJ, UK"],
                "6": ["Dolly Detweiler","+442032960977","18 Johnson Rd, Darwen BB3, UK"],
                "7": ["Stanley Vanderhoof","+442032960000","17 Anchor Ave, Darwen BB3 0AZ, UK"],
                "8": ["Adan Milian","+442032960011","20 Ellerbeck Rd, Darwen BB3 3EX, UK"],
                "9": ["Marivel Molina","+442032960013","Tockholes Rd, Darwen BB3, UK"],
                "10": ["Kris Everett","+442032960012","Pinewood, Tockholes Rd, Darwen BB3 1JY, UK"]
           }
        self.root = root
        self.top_frame()
        self.root.title("Magic PhoneBook")
        self.Table()
        self.LoadTable()
        #self.grid(sticky = (N,S,W,E))
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)

################################# Frame, Entry and Button definitions, declarations and functions bindings####################
    def top_frame(self):
        topfrm = Frame(self.root)
        topfrm.grid(row=1, sticky='w')
    
        self.btnConnect = ttk.Button(self.root, text = "Search", command=self.Search).grid(row=1, column=2, sticky=W)
        self.enteredlocation = StringVar()
    
        self.e2=Entry(topfrm)
        self.e2.grid(row=1,column=2, sticky='w')
 
####################################### Table for Contacts information
    def Table(self):
        tv = Treeview(self.root)
        tv['columns'] = ('ph_number', 'address',)
        tv.heading("#0", text='Name', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('ph_number', text='Phone Number')
        tv.column('ph_number', anchor='center', width=100)
        tv.heading('address', text='Address')
        tv.column('address', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
      for k,v in self.data.items():
          self.treeview.insert('', 'end', text=v[0], values=(v[1],v[2]))
      
    def Search(self):
        
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for k,v in self.data.items():
            if self.e2.get() in v[0]:
                self.treeview.insert('', 'end', text=v[0], values=(v[1],v[2]))
                
            if self.e2.get() in v[1]:
                self.treeview.insert('', 'end', text=v[0], values=(v[1],v[2]))

            if self.e2.get() in v[2]:
                self.treeview.insert('', 'end', text=v[0], values=(v[1],v[2]))
                
        print(self.e2.get().find(v[0]))
        print(self.e2.get())
    #  reg = re.compile(r'[a-zA-Z]')
     # re.findall(self)


def main():
    root=Tk()
    PhoneBook(root)
    root.mainloop()
if __name__ == '__main__':
    main()
