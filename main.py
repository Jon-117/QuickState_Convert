"""
This program continuously monitors your clipboard. Whenever it detects a change, it checks the new content for any full state names. If any are found, it replaces them with their corresponding abbreviations and updates the clipboard with the new string.
"""
import pyperclip
import re
import time
import os


# Set the CMD window title
os.system('title QuickState Convert')


state_abbreviations = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

instruction_message = """
Welcome to QuickState_Convert!

QuickState_Convert is designed to simplify your workflow by automatically converting US State names in your clipboard 
to their abbreviations. Here’s how to get started:

The program is running!

Copy Text: Whenever you copy text containing full US State names (e.g., "California", "Minnesota"), QuickState_Convert
will automatically detect and convert these names into their two-letter abbreviations (e.g., "CA", "MN").

Paste Anywhere: Now, when you paste your clipboard content, you'll notice that all State names have been abbreviated. 
It’s that simple!

Exiting: To stop the program, you can close this window or find its icon in the system tray and right-click the icon 
and select “Quit” or “Exit”.

Tips for Best Performance:

Ensure QuickState_Convert is running in the background for automatic conversion.
If you encounter any issues, restart the program or submit an issue on github!
Thank you for choosing QuickState_Convert. Enjoy streamlined state string conversions!
"""


def convert_state_to_abbreviation(text) -> str or None:
    """
    Regular expression pattern to match full state names
    :param text: String
    :return: If a state name is found in text, returns its abbreviation
    """
    pattern = r'\b(' + '|'.join(state_abbreviations.keys()) + r')\b'

    def abbreviate(match) -> str:
        """
        Function to replace full state names with abbreviations
        :param match:
        :return:
        """
        return state_abbreviations[match.group(0)]

    # Replace all occurrences of full state names with their abbreviations
    return re.sub(pattern, abbreviate, text, flags=re.IGNORECASE)


def monitor_and_abbreviate() -> None:
    """
    Monitor clipboard for changes and convert state names to abbreviations
    :return: None
    """
    previous_text = pyperclip.paste()  # Initially check the clipboard content
    while True:
        current_text = pyperclip.paste()
        if current_text != previous_text:
            # Text has changed, process it
            modified_text = convert_state_to_abbreviation(current_text)
            if modified_text != current_text:
                # Update the clipboard with the modified text
                pyperclip.copy(modified_text)
            previous_text = modified_text
        time.sleep(0.5)  # Check every half second


if __name__ == '__main__':
    print(instruction_message)
    monitor_and_abbreviate()
