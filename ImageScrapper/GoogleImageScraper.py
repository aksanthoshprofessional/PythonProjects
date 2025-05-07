import tkinter as tk
from tkinter import filedialog,messagebox,ttk
import os
import requests 
from bs4 import BeautifulSoup

SAVE_FOLDER='images'

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def select_directory():
    global SAVE_FOLDER
    SAVE_FOLDER = filedialog.askdirectory()
    check()

def check():
    global SAVE_FOLDER
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()

def download_images():
    global window
    global entry1
    global entry2
    
    data=entry1.get()
    n_images=int(entry2.get())

    os.chdir(SAVE_FOLDER)
    

    searchurl=GOOGLE_IMAGE + 'q=' +data
    print(searchurl)

    response = requests.get(searchurl,headers=usr_agent)
    html=response.text

    soup=BeautifulSoup(html,'html.parser')
    i=0
    jpg_images = soup.find_all('img',src=lambda src: src and 'http' in src.lower() or 'https' in src.lower(),limit=n_images)
    window.update_idletasks()
    x_center = window.winfo_x()//2 + (window.winfo_width() // 2)
    y_center = window.winfo_y()//2 + (window.winfo_height() // 2)
    root = tk.Toplevel(window)
    root.geometry("+{}+{}".format(x_center, y_center))
    root.grab_set()
    root.title('Progress')
    root.geometry("+{}+{}".format(x_center, y_center))
    
    a=tk.Label(root,text="Downloading...",justify='center')
    a.pack()
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack()
    progress['maximum']=n_images
    for item in jpg_images: 
        i+=1
        url=item['src']
        response=requests.get(url)
        save_as='{}{}.jpg'.format(data,i)
        with open(save_as,'wb') as file:
            file.write(response.content)
        progress['value'] = i + 1
        progress.update()
    root.destroy()
    messagebox.showinfo("Complete","The images are saved into /{}".format(SAVE_FOLDER))


def main():
    global entry1
    global entry2
    global window
    window=tk.Tk()
    window.geometry('600x250')
    window.title('Google Image Scrapper')
    label1 =tk.Label(window,text="Google Image Scrapper", width=20,font=("bold",20))
    label1.pack()
    label2=tk.Label(window,text="Made by Santhosh.A",width=20,font=("arial",9))
    label2.pack()
    label_1 =tk.Label(window,text="What do you want to download?", width=26,font=("bold",12))
    label_1.place(x=40,y=88)
    entry1=tk.Entry(window,font=("bold",12),justify='center')
    entry1.place(x=280,y=92,width=220,height=20)

    label_1 =tk.Label(window,text="Number of Images :", width=26,font=("bold",12))
    label_1.place(x=76,y=120)
    entry2=tk.Entry(window,font=("bold",12),justify='center')
    entry2.place(x=280,y=122,width=220,height=20)

    b=tk.Button(window, text='Submit' , width=20,bg='white',fg='black',command=lambda: select_directory())

    b.place(x=230,y=200)



    window.mainloop()


if __name__ == '__main__':
    main()
