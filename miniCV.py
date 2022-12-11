from tkinter import *
import webbrowser as web

root = Tk()
root.title("Cyber Worm")
root.iconbitmap("logo.ico")
root.geometry("380x400")
root.configure(bg="#005b96")

def github():
    web.open("https://github.com/bellurm?tab=repositories")

def website():
    web.open("https://blog-cyberworm.com")

def linkedin():
    web.open("https://tr.linkedin.com/in/mehmetali-bellur-9b54461b8")

def instagram():
    web.open("https://www.instagram.com/_cyber.worm_/")

def hackerrank():
    web.open("https://www.hackerrank.com/mehmetalibellur")

def tryhackme():
    web.open("https://tryhackme.com/p/W0rm")

description = Label(root, text="About Cyber Worm", bg="#005b96", fg="#44bb66", padx=10, pady=10, font=("Arial", 16)).pack(side="top")

emailAddr = "kaliworm101@gmail.com"
email = Label(root, text=f"Special Contact: {emailAddr}", bg="#005b96", fg="#fefbf0", font=("Arial", 13)).pack(side="bottom")

# left side
frameGit = LabelFrame(root, text="Github", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.09, rely=0.13)
frameLinkedin = LabelFrame(root, text="LinkedIn", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.09, rely=0.4)
frameHackerrank = LabelFrame(root, text="HackerRank", width=140, height=75, bg="#005b96", fg="#fefbf0").place(relx=0.09, rely=0.67)
# right side
frameWebSite = LabelFrame(root, text="Website", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.56, rely=0.13)
frameInstagram = LabelFrame(root, text="Instagram", width=140, height=75, bg="#005b96", fg="#fefbf0").place(relx=0.56, rely=0.4)
frameTryHackMe = LabelFrame(root, text="TryHackMe", width=140, height=75, bg="#005b96", fg="#fefbf0").place(relx=0.56, rely=0.67)

# left side
buttonGit = Button(frameGit, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=github)
buttonGit.place(relx=0.14, rely=0.185)
buttonLinkedin = Button(frameLinkedin, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=linkedin)
buttonLinkedin.place(relx=0.14, rely=0.46)
buttonHackerrank = Button(frameHackerrank, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=hackerrank)
buttonHackerrank.place(relx=0.14, rely=0.73)
# right side
buttonWebSite = Button(frameWebSite, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=website)
buttonWebSite.place(relx=0.615, rely=0.185)
buttonInstagram = Button(frameInstagram, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=instagram)
buttonInstagram.place(relx=0.615, rely=0.46)
buttonTryHackMe = Button(frameTryHackMe, text="Click to visit.", width=13, height=2, bg="#00b0ff", fg="#282102", command=tryhackme)
buttonTryHackMe.place(relx=0.615, rely=0.73)

root.mainloop()