import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Fungsi web scraping
def get_data():
    url = 'https://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Ambil data dari halaman web
    data = soup.find('div', {'class': 'data'}).text
    return data

# Fungsi untuk menampilkan data di aplikasi desktop
def display_data():
    data = get_data()
    label.config(text=data)

# Aplikasi desktop
root = tk.Tk()
root.geometry('400x200')
root.title('Aplikasi Desktop')

# Tombol untuk menampilkan data
button = tk.Button(root, text='Tampilkan Data', command=display_data)
button.pack()

# Label untuk menampilkan data
label = tk.Label(root, text='')
label.pack()

root.mainloop()
