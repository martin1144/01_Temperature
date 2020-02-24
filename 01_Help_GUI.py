from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
        def __init__(self):

            # Formatting variables..
            background_color = "light blue"

            # In actual program this is blank and is populated with user calculations
            self.all_calc_list = ['0 degrees C is 32.0 degrees F',
                                  '40 degrees C is 104.0 degrees F',
                                  '100 degrees C is 212.0 degrees F',
                                  '3 degrees C is 37.4 degrees F']

            # Converter Main Screen GUI...
            self.converter_frame = Frame(width=600, height=600, bg=background_color)
            self.converter_frame.grid()

            # Temperature Conversion Heading (row 0)
            self.temp_converter_label = Label (self.converter_frame, text="Temperature Converter",
                                               font=("Arial", "16", "bold"),
                                               bg=background_color,
                                               padx=10, pady=10)
            self.temp_converter_label.grid(row=0)

            # Help Button (row 1)
            self.help_button = Button (self.converter_frame, text="Help",
                                       font=("Arial", "14"),
                                       padx=10, pady=10, command=self.help)
            self.help_button.grid(row=1, pady=10)

        def help(self):
            print("You asked for help")
            get_help = help(self)
            get_help.help_text.configure(text="Help text goes here")


class History:
    def __init__(self, partner):

        background = "#a9ef99"      # Pale green

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up History heading (row 0)
        self.how_heading = Label(self.help_frame, text="help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # History text (label, row 1)
        self.help_text = Label(self.help_frame,
                                        text="Here are your most recent "
                                             "calculations. Please use the "
                                             "export button to create a text "
                                             "file of all your calculations for "
                                             "this session", wrap=250,
                                        font="arial 10 italic",
                                        justify=LEFT, bg=background, fg="maroon",
                                        padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                             command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
