from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "light blue"''

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                text="Temperature Converter",
                                font="Arial 19 bold",
                                bg=background_color,
                                padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instruction (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                     text="Type in the amount to be "
                                          "Converted and then push "
                                          "one of the buttons below...",
                                     font="Arial 10 italic", wrap=290,
                                     justify=LEFT, bg=background_color,
                                     padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), gold3
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="gold3", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))

        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                          text="To Fahrenheit", font="Arial 10 bold",
                          bg="Orchid1", padx=10, pady=10,
                          command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=6, pady=10)

        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                       command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=0, column=0,)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)
        error = "#ffafaf"   # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()
        self.to_convert_entry.configure(bg="white")

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to Fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                # Input os invalid (too cold)!!
                answer = "Too Cold!"
                has_errors = "yes"

            # Check amount is a valid number

            # Convert to F

            # Convert to C

            # Round!!

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg=error)
            # Add Answer to list for history
            if answer != "Too Cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)

            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def history(self, all_calc_list):
        print("You asked for history")
        History(self, all_calc_list)

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                             command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self,partner, calc_history):

        background = "#a9ef99"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="history / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use the "
                                                           "export button to create a text "
                                                           "file of all your calculations for "
                                                           "this session", wrap=250,
                                                      font="arial 10 italic",
                                                      justify=LEFT, bg=background, fg="maroon",
                                                      padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        # Dismiss and export button (row 3)

        self.history_export_frame = Frame(self.history_frame)
        self.history_export_frame.grid(row=3, pady=10)

        self.dismiss_btn = Button(self.history_export_frame, text="Dismiss",
                                  width=10, bg="orange", font="Arial 12 bold",
                             command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, pady=1)

        # Export Button
        self.export_button = Button (self.history_export_frame, text="Export",
                                     font="Arial 12 bold")
        self.export_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("History")
    something = Converter()
    root.mainloop()
