from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations


        '''self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F',
                                ]'''

        self.all_calc_list = []

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
                                       padx=10, pady=10, command=self.all_calc_list)
        self.export_button.grid(row=1)

    def export(self, all_calc_list):
        get_export = export(self)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
