#!/usr/bin/env python
__author__ = "Nelson Tam"
__copyright__ = "Copyright 2016"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nelson Tam"
__email__ = ""
__status__ = "Production"
import sys
def findlottopick(inputStr):
    # debugging flag (1 = turn on debugging output)
    debug = 1

    # lotto constants
    # represent physical constraints, 
    # including range of valid lotto numbers, 
    # length of expected string resulting in 1 or more successful pick combinations
    numInASet = 7
    minStrLen = numInASet * 1
    maxStrLen = numInASet * 2
    minLottoNum = 1
    maxLottoNum = 59

    # monitoring variables
    numOfSingleDigitFound = 0
    numOfDoubleDigitFound = 0
    found = 1

    inputLen = len(inputStr)

    # determine minimum number of require double digits in the pick
    minNumOfDoubleDigit = inputLen - minStrLen
    maxNumOfSingleDigitAllowed = numInASet - minNumOfDoubleDigit;

    # validate if string has required length to form possible pick
    if inputLen < minStrLen or inputLen > maxStrLen:
        return False, None

    l = map(int, inputStr)
    print(l)
    if debug == 1 : print (l)

    # special case if exactly 7 numbers than return list as is
    if inputLen == minStrLen:
        # check for 0 or duplicates
        if 0 not in l and len(l) == len(set(l)):
            return True, l
        else:
            return False, None

    # storage for lotto combination
    partial=[]
    # skip iteration before a digit is previously used as double digit number
    skip = 0

    for i in list(range(inputLen)):
        useDoubleDigit = 0     

        # skip digit first
        if skip == 1:
            skip = 0
            continue

        if debug == 1 : print ("i=%s" %(i))

        # if we reach the target then stop
        if len(partial) == numInASet and i == inputLen:
            break

        # illegal characters, cannot have zero
        if l[i] == 0:
            found = 0
            break

        # valid numbers from 1 to 59
        if l[i] >= 6:
            # first digit is 6 or greater, cannot be double digit
            if l[i] not in partial:
                partial.append(l[i])
                numOfSingleDigitFound += 1
            else:
                found = 0
                break
        elif i+1 < inputLen or l[i+1] == 0:
            # special case, if there is only 2 digits left
            # and list still needs 2 more number for a pick
            # then need to force to use 2 single digit number
            specialCaseUseSingleDigit = 0
            if i + 1 == inputLen - 1 and len(partial) == (numInASet - 2):
                specialCaseUseSingleDigit = 1

            # if very few quota of double digit left, and remaining numbers
            # have duplicate digits, and push back using double digit number later
            # special case - 12334567 where require pick needs to be 1, 23, 3, 4, 5, 6, 7
            # to avoid 2 single digit 3 from being picked.
            if minNumOfDoubleDigit <= 2:
                remain = l[i+2:]
                if numOfDoubleDigitFound < minNumOfDoubleDigit and len(remain) != len(set(remain)):
                    specialCaseUseSingleDigit = 1

            # calculate possible double digit
            n = l[i] * 10 + l[i+1]

            # scan remaining of list for possible identical "double digit number pattern"
            # to prevent situation where a double digit is chosen first, and then later another 
            # pattern is found, needed, but cannot be used (because it is used already)
            try:
                if i > 1 and i+2 < inputLen:
                    remainArr = l[i+2:]
                    remainStrAfterDoubleDigitUsed = "".join(str(x) for x in remainArr)
                    if remainStrAfterDoubleDigitUsed.find(str(n)) != -1:
                        specialCaseUseSingleDigit = 1
            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                print ("<p>Error: %s</p>" % e)

            # if double digit within valid range, and not under pressure to
            # use single digit
            if (n >= minLottoNum 
               and n <= maxLottoNum 
               and n not in partial
               and specialCaseUseSingleDigit == 0
               and numOfDoubleDigitFound < minNumOfDoubleDigit ):
                partial.append(n)
                numOfDoubleDigitFound += 1
                skip = 1
            else:
                if l[i] not in partial:
                    partial.append(l[i])
                    numOfSingleDigitFound += 1              
        else:
            # last element, must treat as single digit
            if l[i] not in partial:
                partial.append(l[i])
                numOfSingleDigitFound += 1        

    if found == 1 and len(partial) == numInASet:
        return True, partial
    else:
        return False, None

if __name__ == "__main__": 

    print ("Standard test case")
    sequence = [ "569815571556", "4938532894754", "1234567", "472844278465445" ]
    for inputStr in sequence:
        success, picks = findlottopick(inputStr)

        if success is True:
            print ("%s -> %s" % (inputStr, picks))

    print ("\nAdditional test cases, with 0")
    print ("the algorithm shall have a lotto pick for all of the following sequence: " )
    print ("101122241229"", ""1011222412209"", ""1011202241229"", ""1011222401229"" " )       
    sequence = [ "101122241229", "1011222412209", "1011202241229", "1011222401229" ]
    for inputStr in sequence:
        success, picks = findlottopick(inputStr)

        if success is True:
            print ("%s -> %s" % (inputStr, picks))

    print ("\nAdditional negative test cases, with 0")
    print ("the algorithm reject all of the following sequence, due to zero being in the pick: ")  
    print ("0101122241229"", ""10011222412209"", ""111222412290"", ""10012345"", ""12345607"" " )       
    sequence = [ "0101122241229", "10011222412209", "111222412290", "10012345", "12345607" ]
    for inputStr in sequence:
        success, picks = findlottopick(inputStr)

        if success is True:
            print ("%s -> %s" % (inputStr, picks) )

    print ("\nEdge cases")
    print ("the algorithm accept all of the following sequence: "  )
    print ("12334567"" "        )
    sequence = [ "12334567" ]
    for inputStr in sequence:
        success, picks = findlottopick(inputStr)

        if success is True:
            print ("%s -> %s" % (inputStr, picks) )  

    print ("\nAdditional test case as requested")
    sequence = [ "5698157156" ]
    for inputStr in sequence:
        success, picks = findlottopick(inputStr)

        if success is True:
            print ("%s -> %s" % (inputStr, picks)  )                    
