# Pseudocode for Python Fortune Teller Program

BEGIN

    IMPORT random
    IMPORT sys
    IMPORT time

    // Load fortunes
    DECLARE fortunes AS LIST
    ADD "You are a winner!" TO fortunes
    ADD "A secret admirer will soon send you a sign of affection!" TO fortunes
    ADD "The one you love is much closer than you think!" TO fortunes
    ADD "Good things will happen to you by the end of the day today!" TO fortunes
    ADD "Fame and fortune will be yours if you take the time to learn Python!" TO fortunes
    ADD "I'm just a computer program, and have no magical powers!" TO fortunes

    DECLARE magic_colors AS LIST
    ADD "blue" TO magic_colors
    ADD "red" TO magic_colors
    ADD "green" TO magic_colors
    ADD "yellow" TO magic_colors

    // Get user name
    OUTPUT "Please enter your first name:"
    INPUT user_name

    // Welcome message
    OUTPUT "Welcome to my Python Fortune Teller program, " + user_name + "!"

    // Ask if user wants a fortune
    OUTPUT "Do you want me to tell you your fortune? [y/n]"
    INPUT question
    CONVERT question TO lower case
    WAIT 2 seconds

    IF question IS IN ["y", "yes"] THEN
        WAIT 1 second
        OUTPUT "Okay! To get your fortune, please input a magic color: [blue/red/green/yellow]"
        INPUT color
        CONVERT color TO lower case
        
        WAIT 1 second
        OUTPUT "Getting your fortune..."
        WAIT 2 seconds
        OUTPUT "Here is your fortune, " + user_name + ":"
        WAIT 1 second
        
        IF color IS IN magic_colors THEN
            DECLARE index AS RANDOM INTEGER BETWEEN 0 AND LENGTH OF fortunes - 1
            OUTPUT fortunes[index]
        ELSE
            OUTPUT "Please choose a magic color of either 'blue', 'red', 'green', or 'yellow'."
            WAIT 1 second
            OUTPUT "Once you have input a magic color, I will reveal your fortune!"
        END IF
    ELSE
        OUTPUT "Thank you for playing my Fortune Teller game today, " + user_name + "!"
        OUTPUT "Goodbye!"
        EXIT PROGRAM
    END IF

    OUTPUT "Thank you for playing my Fortune Teller game today, " + user_name + "!"
    OUTPUT "Goodbye!"

END

