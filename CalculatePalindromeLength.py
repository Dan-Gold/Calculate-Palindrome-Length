"""
Python 3.10.4


OVERVIEW:

    This program was developed to calculate the maximum palindrome length given the total
    number of characters in the pool to create the palindrome, and given a threshold
    probability, and the maximum number of allowable runs.



Technical:





OUTPUT:




USAGE:
    usage: CalculatePalindromeLength.py [-h] -tc TOTALCHARS [-th THRESHOLD] [-mc MAXRUNS] [-s]

    Used to calculate the maximum word length of a palindrome given the total number of characters in
    the pool with a probability threshold and/or maximum number of calculation runs.

    options:
      -h, --help      show this help message and exit
      -th THRESHOLD   Probability decimal. When the probability is less than or equal to this number
                      stop calculating. Set to -1 to ignore this stop condition. (Default is 0.000001)
      -mc MAXRUNS     The maximum number of times calculate is allowed to run. (Default is 400)
      -s              Shows the processing of the probabilities by printing to the terminal. (Default
                      is False)

    required arguments:
      -tc TOTALCHARS  Total number of characters in the character set that will be used to make
                      palindromes.




RESOURCES USED:

    https://math.stackexchange.com/questions/2129120/probability-of-being-a-palindrome

    https://www.wolframalpha.com/widgets/view.jsp?id=464e41dfc7c0cc7a140939f10c754b

    Might want to implement this so that there is only one equation and not one for even or odd
    https://math.stackexchange.com/questions/1076007/best-function-getting-0-for-odd-parameter-1-for-even



EXAMPLE:

    python CalculateProbabilityOfPalindrome.py -h




Revision Log:

Name                |  Revision  |  Date      |  Note
--------------------------------------------------------------------------------
Dan_Gold            |  1.1       | 04/28/2022 |  Initial release.
--------------------------------------------------------------------------------


"""

import argparse
import errno

def argParse():
    """ This is the argparse for calling this program as main """

    parser = argparse.ArgumentParser(description = "Used to calculate the maximum word length of a palindrome given the total number of characters in the pool with a probability threshold and/or maximum number of calculation runs. ")

    # Required Arguments
    required = parser.add_argument_group("required arguments")
    required.add_argument('-tc', dest="totalChars", help = "Total number of characters in the character set that will be used to make palindromes. ", required=True)

    # Optional Arguments
    parser.add_argument('-th', dest="threshold", default=0.000001, help = "Probability decimal. When the probability is less than or equal to this number stop calculating. Set to -1 to ignore this stop condition. (Default is 0.000001)")
    parser.add_argument('-mr', dest="maxRuns", default=400, help = "The maximum number of times calculate is allowed to run. (Default is 400)")
    parser.add_argument('-s', dest="show", action='store_true', help = "Shows the processing of the probabilities by printing to the terminal. (Default is False)")

    args = parser.parse_args()

    return(args)


class calcProbPal():
    """ Calculates the probability of a palindrome appearing given the number of characters being used. """

    def __init__(self, threshold = 0.000001, maxCalcRuns = 400, show=False):
        """ threshold   = When the probability is less than or equal to this number stop calculating. Must be a decimal less than 1. Set to -1 to ignore this stop condition. Default is 0.000001.
            maxCalcRuns = The maximum number of times calculate is allowed to run to avoid the possibility that this program runs forever. Set to -1 to ignore this stop condition. Default is 400 runs.
            show        = Set to True to print the processing of the probabilities. Default is False.
        """

        try:
            threshold = float(threshold)
        except:
            pass

        try:
            maxCalcRuns = int(maxCalcRuns)
        except:
            pass
            # TODO: make these except statement better

        # Threshold must be less than one and greater than zero, or equal to -1
        if(not ((threshold < 1 and threshold > 0) or threshold == -1)):
            print("Entered threshold was not a value exclusively between 0-1 or equal to -1, setting to default: 0.000001")
            threshold = 0.000001

        self.threshold = threshold
        self.maxCalcRuns = maxCalcRuns
        self.show = show
        self.floatPrec = 20

    def runCalculations(self, totalChars):
        """ Runs the calculation until probability threshold is met or the maximum number of runs is met unless these variables are overridden. Returns the resulting word length that meets the desired input targets. """

        # TODO: Check inputs to make sure they are all within valid ranges

        curProb = 99
        wordLength = 0

        while((wordLength < self.maxCalcRuns or self.maxCalcRuns == -1) and (curProb > self.threshold or self.threshold == -1)):
            curProb = self.calculate(totalChars, wordLength)

            if(self.show):
                print("Word Length: {0}   Probability: {1:.{prec}f}".format(wordLength, curProb, prec=self.floatPrec))

            wordLength += 1

        # Check to see that the last wordLength += 1 probability is equal to the previous
        # probability. Theoretically they should always be the same and to be more efficient
        # we only need to loop through even numbers then add one to the wordLength when the
        # threshold is reached. Which would reduce the number of times calculate is called by half.
        # TODO: make runQuickCalculations() method with this efficiency
        nextProb = self.calculate(totalChars, wordLength)

        if(self.show):
            print("Word Length: {0}   Probability: {1:.{prec}f}".format(wordLength, curProb, prec=self.floatPrec))

        if((not nextProb == curProb) and wordLength > 0):
            # This code should theoretically never be reached
            wordLength -= 1

        return(wordLength, curProb)

    def calculate(self, totalChars, wordLength):
        """ Calculates the probability that the given wordLength and the total number of characters
        in the character set could be a palindrome. Returns the probability as a float. """

        probability = 0

        if(wordLength % 2 == 0):
            # Even
            probability = self.calcPalEven(totalChars, wordLength)

        else:
            # Odd
            probability = self.calcPalOdd(totalChars, wordLength)

        return(probability)

    def calcPalEven(self, totalChars, wordLength):
        """ Calculates the probability that the current EVEN wordLength is a palindrome. Returns the probability as a float. """

        result = 0

        try:
            result = 1/(totalChars**(wordLength/2))
        except ZeroDivisionError as e:
            print("Error: {0} setting result to zero".format(e))
            

        return(result)

    def calcPalOdd(self, totalChars, wordLength):
        """ Calculates the probability that the current ODD wordLength is a palindrome. Returns the probability as a float. """

        result = 0

        try:
            result = 1/(totalChars**((wordLength-1)/2))
        except ZeroDivisionError as e:
            print("Error: {0} setting result to zero".format(e))

        return(result)

    def calcPalAll(self, totalChars, wordLength):
        """ Calculates the probability that the current wordLength is a palindrome. Returns the probability as a float.

        Warning this has floating point error where 9 is at the end. Might need to round up to nearest three consecutive zeros.
        0.010000000000000009
        0.10000000000000009

        Decided not to use this method for the calculations, the other way is more accurate.

        Floating Point Arithmetic: Issues and Limitations
        https://docs.python.org/3/tutorial/floatingpoint.html
        """

        result = ((1/(totalChars**(wordLength/2)))**((1+(-1)**(wordLength))/2)) + ((1/(totalChars**((wordLength-1)/2)))**((1+(-1)**(wordLength+1))/2)) - 1

        return(result)

if __name__ == "__main__":
    # This is main

    options = argParse()

    app = calcProbPal(options.threshold, options.maxRuns, options.show)

    wordLen, prob = app.runCalculations(int(options.totalChars))

    print("Word Length: {0} With final probability of {1} to meet threshold of {2}".format(wordLen, prob, options.threshold))
    print("Program complete")
