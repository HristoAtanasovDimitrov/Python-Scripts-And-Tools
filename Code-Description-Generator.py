# --< Description >-- # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
#    The primary objective of this Python script is to format a given block of text into a visually centered    #
#    structure, bordered by a header and footer composed of hash (#) symbols. This block of text is             #
#    intended to serve as a description of the code and can be positioned at the beginning of the script.       #
#                                                                                                               #
#    MIT License                                                                                                #
#    Copyright (c) 2024 Hristo Dimitrov                                                                         #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Text to be formated
input_text = """
The primary objective of this Python script is to format a given block of text into a visually centered
structure, bordered by a header and footer composed of hash (#) symbols. This block of text is 
intended to serve as a description of the code and can be positioned at the beginning of the script.

MIT License
Copyright (c) 2024 Hristo Dimitrov
"""
# Function to format the text
def format_description(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    # Find the maximum line length
    max_length = max(len(line) for line in lines if line.strip())

    # Ensure max_length is even
    max_length = max_length + 1 if max_length % 2 != 0 else max_length

    # Create the description header and footer
    header = f"# --< Description >-- #{' #' * ((max_length // 2) - 7)}"
    footer = f"#{' #' * ((max_length // 2) + 4)}"

    # Print the formatted output
    print(header)

    for line in lines:
        if line.strip():
            # Calculate padding for each line
            padding = " " * ((int(len(footer) - len(line))) - 6)
            # Print the formatted line
            print(f"#    {line}{padding}#")
        else:
            # Print empty line with correct length
            print(f"{'#' + ' ' * (max_length + 7)}#")

    print(footer)

# Call the function with the text input
format_description(input_text)
