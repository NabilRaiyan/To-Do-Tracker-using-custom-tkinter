import customtkinter
import messagebox

row = 4
no = 1
l_row = 4


def add_label(data, col, row, padx, pady, font):
    label = customtkinter.CTkLabel(text=data, text_color="white", text_font=font)
    label.grid(column=col, row=row, padx=padx, pady=pady)


def add_to_do():
    global no, l_row
    to_do = to_do_entry.get()
    add_label(data=f"{no}: {to_do}", col=1, row=l_row, padx=5, pady=5, font=("Arial", 12, "bold"))
    no += 1
    l_row += 1


def add_todo():
    date = date_entry.get()
    global row
    if len(date) == 0 or len(to_do_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please enter all information")
    else:
        label = customtkinter.CTkLabel(text=f"Today's date: {date}", text_color="white",
                                       text_font=("Arial", 15, "bold"))
        label.grid(column=0, row=0, padx=5, pady=5)

        check_box = customtkinter.CTkCheckBox(width=15, height=15, border_width=2, border_color="white",
                                              checkmark_color="black")
        check_box.grid(column=0, row=row, padx=15, pady=15)
        add_to_do()
        row += 1

        to_do_entry.delete(0, customtkinter.END)


def reset_to_do():
    window.destroy()


window = customtkinter.CTk()
window.geometry("750x500")
window.title("TO-DO TRAKER")
window.configure(padx=50, pady=50, fg_color="#2C3639")

customtkinter.set_default_color_theme("green")

date_label = add_label(data="Enter Date: ", col=0, row=1, padx=0, pady=2, font=("Arial", 12, "bold"))
todo_label = add_label(data="Enter To-Do", col=0, row=2, padx=0, pady=2, font=("Arial", 12, "bold"))

date_entry = customtkinter.CTkEntry(width=180, height=30, border_width=1, corner_radius=8, fg_color="#2C3639",
                                    border_color="black",
                                    text_color="white")
date_entry.grid(column=1, row=1, padx=10, pady=15)

to_do_entry = customtkinter.CTkEntry(width=300, height=30, border_width=1, corner_radius=8, fg_color="#2C3639",
                                     border_color="black",
                                     text_color="white")
to_do_entry.grid(column=1, row=2, pady=15)

add_button = customtkinter.CTkButton(text="Add To-Do to the list", fg_color="white", border_width=1,
                                     border_color="black",
                                     text_color="black", hover_color="cyan", command=add_todo)
add_button.grid(row=1, column=2, padx=10, pady=15)

reset_button = customtkinter.CTkButton(text="Reset", fg_color="white", border_width=1, border_color="black",
                                       text_color="black", hover_color="cyan", command=reset_to_do)
reset_button.grid(row=2, column=2, padx=10, pady=15)

window.mainloop()
