#ivoxprojects
import customtkinter
from datetime import date

curr_date = date.today()
christmas_date = date(2022, 12, 25)
delta = curr_date - christmas_date
daysleft = -delta.days

root = customtkinter.CTk()
root.title("Days untill christmas!")
root.geometry("500x350")
root.resizable(False,False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=15, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text=f"{daysleft} days left untill christmas!", text_font=("", 20))
label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

root.mainloop()