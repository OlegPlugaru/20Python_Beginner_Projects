# have a python dictionary that has a key/value pair that represents a word and it's definition
# collect input from the user, input is a word
# check id the word is in the dictionary
# print the definition


def main():
    python_reserved_words = {
        "and": "A logical operator that returns True if both operands are True, and False otherwise.",
        "as": "Used to create an alias for a module or class.",
        "assert": "A debugging aid that tests a condition and triggers an error if the condition is not True.",
        "break": "Used to exit a loop prematurely.",
        "class": "Used to define a new class.",
        "continue": "Used to skip the current iteration of a loop and move to the next iteration.",
        "def": "Used to define a new function.",
        "del": "Used to delete a variable or attribute.",
        "elif": "A conditional statement that is used in conjunction with an if statement to test multiple conditions.",
        "else": "A conditional statement that is executed if none of the conditions in an if statement are True.",
        "except": "A block of code that is executed if an error occurs within a try block.",
        "False": "A boolean value that represents the logical value of False.",
        "finally": "A block of code that is always executed, regardless of whether an error occurs.",
        "for": "Used to iterate over a sequence of values.",
        "from": "Used to import a specific attribute or function from a module.",
        "global": "Used to indicate that a variable is a global variable.",
        "if": "A conditional statement that tests a condition and executes code if the condition is True.",
        "import": "Used to import a module.",
        "in": "A keyword used to test if a value is in a sequence.",
        "is": "A comparison operator that returns True if two objects are the same object.",
        "lambda": "Used to create anonymous functions.",
        "None": "A keyword that represents the absence of a value.",
        "nonlocal": "Used to indicate that a variable is a nonlocal variable.",
        "not": "A logical operator that returns True if the operand is False, and False otherwise.",
        "or": "A logical operator that returns True if either operand is True, and False otherwise.",
        "pass": "A null operation that does nothing.",
        "raise": "Used to raise an exception.",
        "return": "Used to return a value from a function.",
        "True": "A boolean value that represents the logical value of True.",
        "try": "A block of code that is used to test for errors.",
        "while": "Used to create a loop that continues while a condition is True.",
        "with": "Used to manage a context for a block of code.",
        "yield": "Used to return a value from a generator function."
    }
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in python_reserved_words:
            print(word, ":", python_reserved_words[word])\



main()
