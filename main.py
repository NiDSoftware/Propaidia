import tkinter as tk
import time as tm
from tkinter import messagebox
from tkinter import ttk

class appUi:
    def __init__(self, master,width,height):
        self.root = master
        self.width = width
        self.height = height
        pos_x = int((self.root.winfo_screenwidth()-self.width)/2)
        pos_y = int((self.root.winfo_screenheight()-self.height)/2)
        self.root.title("Προπαίδεια")
        self.root.geometry("{}x{}+{}+{}".format(self.width,self.height,pos_x,pos_y))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frm_statusBar()
        self.topmenu()
        self.frame_main()
    
    def frame_main(self):
        frm = tk.Frame(self.root)
        frm.grid(row=0, column=0, sticky= "wens")
        self.root.rowconfigure(0, weight=1)

        self.frm_top = tk.Frame(frm, bg="lightblue", bd=2, relief="raised")
        self.frm_left = tk.Frame(frm, bg="lightgreen" )
        sep = ttk.Separator(frm, orient="vertical")
        self.frm_right = tk.Frame(frm, bg="lightgreen")
        
        self.frm_top.grid(row=0, column=0, columnspan=3, sticky="we")
        self.frm_left.grid(row=1, column=0, sticky="wens")
        sep.grid(row=1, column=1, sticky="ns")
        self.frm_right.grid(row=1, column=2, sticky="wens")
        
        frm.grid_rowconfigure(1, weight=1)
        #frm.grid_columnconfigure(0, weight=1)
        frm.grid_columnconfigure(2, weight=2)

        lbl_title = tk.Label(self.frm_top, text="Μαθαίνω την Προπαίδεια", font=("verdana",22), bg="lightblue")
        lbl_title.grid(row=0, column=0, sticky="we")
        self.frm_top.grid_columnconfigure(0, weight=1)
        
        self.frame_left()

    def frame_left(self):
        lbl_name = tk.Label(self.frm_left, text= "Το όνομά σου είναι: ", font=("verdana",10))#, bg="lightgreen")
        lbl_getname = tk.Label(self.frm_left, textvariable = self.user, width=15, font=("verdana",10), anchor="w")#, bg="lightgreen")
        btn_name = tk.Button(self.frm_left, text="Όνομα", font=("verdana",10), command=self.win_username)

        lbl_propaidia = tk.Label(self.frm_left, text= "Θέλεις να μάθεις την προπαίδεια του:", font=("verdana",10))#, bg="lightgreen")
        self.spin_propaidia= ttk.Spinbox(self.frm_left, from_=1, to=10, width=5, font=("verdana",12))
        self.spin_propaidia.set(5)
        self.checkbox_var = tk.IntVar()
        #self.checkbox_var=1
        checkbox_random = tk.Checkbutton(self.frm_left, text="Τυχαία επιλογή", font=("verdana",10), variable = self.checkbox_var, command=self.checkbox_check)

        lbl_name.grid(row=0, column=0, sticky="w")
        lbl_getname.grid(row=0, column=1)
        btn_name.grid(row=0, column=2, pady=5, padx=5)

        lbl_propaidia.grid(row=1,column=0, columnspan=2, ipady=20, sticky="w")
        self.spin_propaidia.grid(row=1,column=2)
        checkbox_random.grid(row=2,column=2)
    
    def checkbox_check(self):
        if self.checkbox_var.get() ==1:
            self.menu_checkbtn_var.set(1)
            self.spin_propaidia["state"]="disable"
        else:
            self.menu_checkbtn_var.set(0)
            self.spin_propaidia["state"]="normal"

    def current_time(self):
        self.display_time.set(tm.strftime("%H:%M:%S    %A, %d %B %Y"))
        self.root.after(200,self.current_time)

    def topmenu(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.menu_checkbtn_var =tk.IntVar()

        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="Όνομα",command=self.win_username)
        self.filemenu.add_checkbutton(label="Τυχαία επιλογή", variable=self.menu_checkbtn_var, command=self.menu_checkbtn_check)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Έξοδος", command=self.root.destroy)
        self.menubar.add_cascade(label="Επιλογές", menu=self.filemenu)

        self.aboutmenu =tk.Menu(self.menubar, tearoff=False)
        self.aboutmenu.add_command(label="Οδηγίες")
        self.menubar.add_cascade(label="Περίληψη", menu=self.aboutmenu)
    
    def menu_checkbtn_check(self):
        if self.menu_checkbtn_var.get()==1:
            self.checkbox_var.set(1)
            self.spin_propaidia["state"]="disable"
        else:
            self.checkbox_var.set(0)
            self.spin_propaidia["state"]="normal"

    def frm_statusBar(self):
        self.frm_sbar= tk.Frame(self.root, bd=1, relief="sunken")
        self.display_time = tk.StringVar()
        self.user = tk.StringVar()
        self.user.set(" ")

        lbl_time = tk.Label(self.frm_sbar, textvariable=self.display_time, font=("Verdana", 8), bg="lightyellow", anchor= "w")
        lbl_username = tk.Label(self.frm_sbar, textvariable=self.user, font=("Verdana", 8), bg="lightyellow")
        lbl_author = tk.Label(self.frm_sbar, text="Created 2020 by Nikolaos Ntinopoulos", font=("Verdana", 8, "italic"), bg="lightyellow", anchor="e")
        sep1 = ttk.Separator(self.frm_sbar, orient="vertical")
        sep2 = ttk.Separator(self.frm_sbar, orient="vertical")
        self.current_time()


        self.frm_sbar.grid(row=1, column=0, sticky="we")
        lbl_time.grid(row=0, column=0, sticky="we")
        sep1.grid(row=0, column=1,sticky="ns")
        lbl_username.grid(row=0, column=2, sticky="we")
        sep2.grid(row=0, column=3,sticky="ns")
        lbl_author.grid(row=0, column=4, sticky="we")
        self.frm_sbar.grid_columnconfigure(2, weight=1)
        
    def win_username(self):
        self.window_username=tk.Toplevel(bg="lightgreen", bd=1, relief="sunken")
        self.window_username.title("Το όνομά σου")
        x=int((self.root.winfo_screenwidth()-400)/2)
        y=int((self.root.winfo_screenheight()-200)/2)
        self.window_username.geometry("400x200+{}+{}".format(x,y))
        self.window_username.attributes('-topmost', 'true')
        lbl_name = tk.Label(self.window_username, text="Γράψε το όνομά σου :", font=("Verdana",12), bg="lightgreen")
        self.name= tk.Entry(self.window_username, width=20, bd=2, font=("Verdana",12))
        self.name.focus()
        self.btnUsername =tk.Button(self.window_username, text="Εισαγωγή", font=("Verdana",12), command=self.getUsername)
        lbl_app = tk.Label(self.window_username, text="Μαθαίνω την Προπαίδεια", font=("Verdana", 8, "italic"), bg="lightgreen", bd=1, relief="sunken", anchor="e")
        
        lbl_name.grid(row=0,column=0, ipady=30)
        self.name.grid(row=0, column=1)
        self.btnUsername.grid(row=1,column=1, sticky="se", padx=10, pady=30)
        lbl_app.grid(row=2, column=0, columnspan=2, sticky="we")
        
        self.window_username.grid_rowconfigure(1, weight=1)
        self.window_username.grid_columnconfigure(1, weight=1)

    def getUsername(self):
        self.user.set(self.name.get().strip())
        self.window_username.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    appUi(root,800,600)
    root.mainloop()