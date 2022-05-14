clear
clear

# Nominal tests

echo "Nominal Test 0: Help menu"
python3 CalculatePalindromeLength.py -h
echo ""
echo ""

echo "Nominal Test 1: All english characters"
python3 CalculatePalindromeLength.py -tc 26
echo ""
echo ""

echo "Nominal Test 2: All english characters and show probabilities"
python3 CalculatePalindromeLength.py -tc 26 -s
echo ""
echo ""

echo "Nominal Test 3: Pool of 10 characters"
python3 CalculatePalindromeLength.py -tc 26
echo ""
echo ""

echo "Nominal Test 4: Pool of 2 characters"
python3 CalculatePalindromeLength.py -tc 2
echo ""
echo ""

echo "Nominal Test 5: Override threshold"
python3 CalculatePalindromeLength.py -tc 26 -th -1
echo ""
echo ""

echo "Nominal Test 6: Set maxRuns"
python3 CalculatePalindromeLength.py -tc 26 -mc 10
echo ""
echo ""

echo "Nominal Test 7: Override maxRuns"
python3 CalculatePalindromeLength.py -tc 26 -th -1
echo ""
echo ""





# Error tests

echo "===== TotalChars error tests ====="
echo ""

echo "Error Test: TotalChars zero"
python3 CalculatePalindromeLength.py -tc 0
echo ""
echo ""

echo "Error Test: TotalChars character"
python3 CalculatePalindromeLength.py -tc a
echo ""
echo ""

echo "Error Test: TotalChars string"
python3 CalculatePalindromeLength.py -tc foo
echo ""
echo ""

echo "Error Test: TotalChars blank"
python3 CalculatePalindromeLength.py -tc
echo ""
echo ""



echo "===== Threshold error tests ====="
echo ""

echo "Error Test: Threshold zero"
python3 CalculatePalindromeLength.py -tc 26 -th 0
echo ""
echo ""

echo "Error Test: Threshold -1"
python3 CalculatePalindromeLength.py -tc 26 -th -1
echo ""
echo ""

echo "Error Test: Threshold -5"
python3 CalculatePalindromeLength.py -tc 26 -th -5
echo ""
echo ""

echo "Error Test: Threshold character"
python3 CalculatePalindromeLength.py -tc 26 -th d
echo ""
echo ""

echo "Error Test: Threshold string"
python3 CalculatePalindromeLength.py -tc 26 -th foo
echo ""
echo ""

echo "Error Test: Threshold blank"
python3 CalculatePalindromeLength.py -tc 26 -th
echo ""
echo ""



echo "===== MaxRuns error tests ====="
echo ""

echo "Error Test: MaxRuns zero"
python3 CalculatePalindromeLength.py -tc 26 -mc 0
echo ""
echo ""

echo "Error Test: MaxRuns -1"
python3 CalculatePalindromeLength.py -tc 26 -mc -1
echo ""
echo ""

echo "Error Test: MaxRuns -5"
python3 CalculatePalindromeLength.py -tc 26 -mc -5
echo ""
echo ""

echo "Error Test: MaxRuns character"
python3 CalculatePalindromeLength.py -tc 26 -mc d
echo ""
echo ""

echo "Error Test: MaxRuns string"
python3 CalculatePalindromeLength.py -tc 26 -mc foo
echo ""
echo ""

echo "Error Test: MaxRuns blank"
python3 CalculatePalindromeLength.py -tc 26 -mc
echo ""
echo ""


