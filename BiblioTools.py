HELP_DOC = """
BIBLIO TOOLS
(version 1.0)
by Angelo Chan

A library of functions useful for performing bibliography-related actions, such
as taking a raw string of authors (directly copied and pasted) and formatting it
into a something suitable for a custom database.
"""



# Configurations ###############################################################



# Defaults #####################################################################

DEFAULT__separator_output = "; "
DEFAULT__separator_input = ","



# Strings ######################################################################

PROMPT__authors_1 = "\nPlease copy the list of authors and paste it here:\n>>> "
PROMPT__authors_2 = "Please specify the desired output separator. Enter "\
        "nothing to use the default.\n(DEFAULT = \"{S}\"\n>>> ".format(
        S = DEFAULT__separator_output)
PROMPT__authors_3 = "Please specify the desired input separator. Enter "\
        "nothing to use the default.\n(DEFAULT = \"{S}\"\n>>> ".format(
        S = DEFAULT__separator_input)



# Lists ########################################################################

LIST__quit = ["QUIT", "Quit", "quit", "Q", "q"]



# Functions ####################################################################

def Author_List(raw_str, separator_output=DEFAULT__separator_output,
            separator_input=DEFAULT__separator_input):
    """
    Return a string containing the authors of a paper in a format suitable for
    putting into a database. Extraneous characters like numbers, used to denote
    institutional affiliations, and which were copied over from the
    copy-and-paste, are removed.

    @raw_str
            (str)
            The raw copy-and-paste output obtained by copying the list of
            authors from a paper and pasting the result into a plaintext editor.
    
    @separator_output
            (str)
            The separator to be used in the output string-list.
    
    @separator_input
            (str)
            The separator be used in the original string-list.
    
    Author_List(str, str, str) -> str
    """
    raw_authors = raw_str.split(",")
    temp_authors = []
    for author in raw_authors:
        while author[0] in [" "] or author[0].isdigit(): # Remove leading
            author = author[1:]
        while author[-1] in [" "] or author[-1].isdigit(): # Remove trailing
            author = author[:-1]
        temp_authors.append(author)
    result = separator_output.join(temp_authors)
    return result

def Author_List_EXE():
    """
    COMMAND LINE INTERFACE
    
    Command line interface to make using the Author_List function more
    convenient.
    """
    input_1 = ""
    while input_1 not in LIST__quit:
        input_1 = raw_input(PROMPT__authors_1)
        if input_1 in LIST__quit: return
        input_2 = raw_input(PROMPT__authors_2)
        if input_2 in LIST__quit: return
        input_3 = raw_input(PROMPT__authors_3)
        if input_3 in LIST__quit: return
        #
        print("")
        if input_2:
            if input_3:
                print(Author_List(input_1, input_2, input_3))
            else:
                print(Author_List(input_1, input_2))
        else:
            print(Author_List(input_1))
    

