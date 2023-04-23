import random


# Create the madlib template that will be processed later
madlibs = [
    # adverb, color, animal, verb, adjective, noun
    "The {0} {1} {2} {3} over the {4} {5}.",
    # adjective, noun, verb, adjective
    "{0} {1} {2} many very {3} jewels."
]

# Prompts must match the expected inputs from madlibs
prompts = [
    ["Adverb", "Color", "Animal", "Verb", "Adjective", "Noun"],
    ["Adjective", "Noun", "Verb", "Adjective"]
]

# Blank list to hold the users input
# that will build the madlib in output_madlib()
inputs = []

def get_madlib():
    """Pick a random madlib template from the madlibs list"""
    # Number of madlibs that can be chosen
    madlib_count = len(madlibs)
    # Pick a random madlib from the list of templates
    madlib = random.randrange(madlib_count)
    # Begin gathering user inputs by displaying prompts
    display_prompts(madlib)

def display_prompts(madlib):
    """Display users the prompts needed to get all
        the information required for the madlib template.

    Args:
        madlib (int): index of the madlib template
            and prompt that should be used
    """
    print("\tCreating your story!")
    # Loop through prompts and display them to user
    # append users input into the inputs variable for
    # processing later
    for prompt in prompts[madlib]:
        inputs.append(input(f"{prompt}: "))
    output_madlib(madlib)

def output_madlib(madlib):
    """Output the finished madlib to the user.

    Args:
        madlib (int): index of the madlib template
            and prompt that should be used
    """
    # Get the madlib template we need to work with
    madlib = madlibs[madlib]
    # Format the template using *inputs to unpack
    # the list and satisfy the templates arguments
    formatted_madlib = madlib.format(*inputs)
    print(formatted_madlib)