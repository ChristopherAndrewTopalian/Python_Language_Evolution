"""
example_001.py - The Late Binding "Gotcha" in Python Loop Closures
"""

def main():
    print("--- 1. The Intuitive Approach (Fails) ---")
    buttons_intuitive = []
    
    for person in ["Alice", "Bob", "Charlie"]:
        # A beginner naturally expects this to bind to the current 'person'
        buttons_intuitive.append(lambda: print(f"Clicked {person}"))

    # Simulating the user clicking the buttons later
    for i, btn in enumerate(buttons_intuitive):
        print(f"Button {i+1}: ", end="")
        btn()  # Prints "Charlie" every time

    print("\n--- 2. The Standard Workaround (Un-Pythonic) ---")
    buttons_workaround = []
    
    for person in ["Alice", "Bob", "Charlie"]:
        # We must pollute the lambda signature with a dummy default argument
        buttons_workaround.append(lambda p=person: print(f"Clicked {p}"))

    for i, btn in enumerate(buttons_workaround):
        print(f"Button {i+1}: ", end="")
        btn()  # Correctly prints Alice, Bob, Charlie

if __name__ == "__main__":
    main()

####

# Dedicated to God the Father
# (c) Copyright 2026 Christopher Andrew Topalian
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# College of Scripting Music & Science
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
# Google Sites: https://sites.google.com/view/CollegeOfScripting

