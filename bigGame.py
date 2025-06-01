"""
Maria Laura Gutierrez
06/01/25

Program Summary:
    This script is a Mad Libs program that takes nouns, verbs,adjectives,
    and other words from the user, and Uuses them to create a personalized story.

IPO Chart:
    Input: The user will input nouns, verbs, adjectives, and other word types.

    Process: The words will be inserted into a story template.

    Output: A personalized story will be displayed to the user.
"""

def main():
    # This is where I print the title and game instructions
    print("MadLib Game ...\n")
    print("Enter the following words:")

    # This is where I ask the user for different words to insert in the story
    # Each input is saved into a variable
    plural_noun_1 = input("Plural Noun: ")
    first_name = input("Person's First Name: ")
    noun_1 = input("Noun: ")
    last_name = input("Person's Last Name: ")
    plural_noun_2 = input("Plural Noun: ")
    place_1 = input("Place: ")
    plural_noun_3 = input("Plural Noun: ")
    place_2 = input("Place: ")
    plural_noun_4 = input("Plural Noun: ")
    noun_2 = input("Noun: ")
    adjective_1 = input("Adjective: ")
    adjective_2 = input("Adjective: ")
    verb = input("Verb: ")
    adjective_3 = input("Adjective: ")

    #This is where I put the variables into the story and print it out
    print("\nThe Big Game !!!\n")
    print(f"Hello there, sports {plural_noun_1}!\n"
          f"This is {first_name}, talking to you from the press {noun_1}\n"
          f"in {last_name} Stadium, where 57,000 cheering {plural_noun_2}\n"
          f"have gathered to watch (the) {place_1} {plural_noun_3}.\n"
          f"take on (the) {place_2} {plural_noun_4}.\n"
          f"Even though the {noun_2} is shining, it’s a/an {adjective_1}\n"
          f"cold day with the temperature in the {adjective_2} 20s.\n"
          f"We’ll be back for the opening {verb}-off after a few words\n"
          f"from our {adjective_3} sponsor.\n"
          )

if __name__ == "__main__":
    main()