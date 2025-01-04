import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, ttk, Toplevel, Label, Button, Entry, StringVar
import threading
import subprocess

def browse_excel():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("Excel files", "*.xlsx *.xls"), ("all files", "*.*")))
    excel_path.set(filename)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    destination_path.set(folder_selected)

def copy_folders_robocopy(excel_path, destination_root, column_folder_name, column_path, progress_bar):
    df = pd.read_excel(excel_path)
    total = len(df)
    if not os.path.exists(destination_root):
        os.makedirs(destination_root)

    for index, row in df.iterrows():
        new_folder_name = str(row[column_folder_name.get()])
        source_folder_path = str(row[column_path.get()])
        full_destination_path = os.path.join(destination_root, new_folder_name)

        if os.path.exists(source_folder_path):
            try:
                # Thực thi lệnh robocopy với các tham số sửa đổi
                subprocess.run(
                    ["robocopy", source_folder_path, full_destination_path, "/E", "/X", "/PURGE",
                     "/COPY:DAT", "/TEE", "/MT:32"],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error during copying {source_folder_path}: {e}")
        else:
            print(f"Error: The source folder {source_folder_path} does not exist.")
        
        # Cập nhật tiến trình
        progress_bar['value'] = (index + 1) / total * 100
        root.update_idletasks()

    progress_bar['value'] = 0  # Reset progress bar after completion
    show_completion_message()

def show_completion_message():
    popup = Toplevel()
    popup.title("Copy Complete")
    popup.geometry("400x200")
    message = "Chúc mừng bạn đã copy thành công các profile GPM,\nchúc anh em kiếm thật nhiều tiền\n"
    Label(popup, text=message, font=("Helvetica", 12), fg="black").pack(pady=(20, 0))
    special_message = "Tool by @dangiaosu"
    Label(popup, text=special_message, font=("Helvetica", 12, "bold"), fg="red").pack()
    Button(popup, text="OK", command=popup.destroy).pack(pady=20)

def start_copy_thread():
    threading.Thread(target=start_copy).start()

def start_copy():
    copy_folders_robocopy(excel_path.get(), destination_path.get(), new_folder_column, path_column, progress)

# Giao diện chính
root = tk.Tk()
root.title("Copy thư mục profiles GPM - Tool by @Dangiaosu")

excel_path = StringVar()
destination_path = StringVar()
new_folder_column = StringVar()
path_column = StringVar()

Label(root, text="Chọn File Excel:").grid(row=0, column=0)
Entry(root, textvariable=excel_path, width=50).grid(row=0, column=1)
Button(root, text="Browse", command=browse_excel).grid(row=0, column=2)

Label(root, text="Chọn thư mục cần copy tới:").grid(row=1, column=0)
Entry(root, textvariable=destination_path, width=50).grid(row=1, column=1)
Button(root, text="Browse", command=browse_folder).grid(row=1, column=2)

Label(root, text="Tên cột thư mục mới:").grid(row=2, column=0)
Entry(root, textvariable=new_folder_column, width=20).grid(row=2, column=1)

Label(root, text="Tên cột chứa đường dẫn thư mục cũ:").grid(row=3, column=0)
Entry(root, textvariable=path_column, width=20).grid(row=3, column=1)

progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.grid(row=4, columnspan=3)

Button(root, text="Bắt đầu Copy", command=start_copy_thread).grid(row=5, column=1)

root.mainloop()
