from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):
        # Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations

        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F',
                                ]

        self.export = []

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font=("Arial" "19" "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # Export Button (row 1)
        self.export_button = Button(self.converter_frame, font=("Arial" "14" "bold"),
                                    text="Export", width=15,
                                    padx=10, pady=10,
                                    command=lambda: self.export(self.all_calc_list))
        self.export_button.grid(row=1)

    def export(self, partner, calc_history):
        print("you want to expoert")
        Export(self, calc_history)



class Export:
    def __init__(self, partner, export):

        print(export)

        background = "#a9ef99"     # Pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel ()

        # If users press cross at top, closes export and
        # 'releases' export button
        self.export_box.wm_protocol('WM_DELETE_WINDOW',
                                        partial(self.close_export, partner))


        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                     text="Export / Instructions",
                                     font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename"
                                                             "in the box below "
                                                             "and press the Save "
                                                             "button to save your "
                                                             "calculation history "
                                                             "to a text file.",
                                     justify=LEFT, widthe=40,
                                        bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                             "you enter below "
                                                             "already exists, "
                                                             "its contents will "
                                                             "be replaced with "
                                                             "your calculation "
                                                             "history",
                                     justify=LEFT, bg="#ffafaf", fg="maroon",
                                        font="Arial 10 italic", wrap=225, padx=10,
                                     pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                        font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                        command=partial(lambda: self.save_history, partner))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, export):
        # Put export button back to normal..
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format)
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add ,txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in export:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        print("you want to close")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
