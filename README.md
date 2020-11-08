This is a shooting simulator for Warhammer 40k. The purpose of it is to simulate a specific interaction of one unit shooting at another, and present a Return on Investment (ROI) for the points spent on the attacking unit. It will return as many ROIs as required by the Iterations input. These can be found in a text file labeled simResults.txt delimited by line breaks. I typically import this data into a spreadsheet and make a frequency distribution with it. It will also return the standard deviation for the data set. This was for debugging purposes but may serve useful in a later update.

Requires NumPy to run.

Syntax for all variable shots/damage with a constant modifier is the constant first followed by the amount of the type of dice being rolled (e.g. Melta Weapons in half range would do 2+d6 damage, 6 Fragstorm Grenade Launchers would fire 6d6 shots)

This simulator can be used for fighting too. Hopefully replacing BS with WS is self-explanatory. You may input up to ten weapon profiles for now. There shouldn't be a need for much more than that.

Unless specified parenthetically, each input must be an integer.


Thanks for being one of the folks attempting to break my numbskull script. The feedback is invaluable.
