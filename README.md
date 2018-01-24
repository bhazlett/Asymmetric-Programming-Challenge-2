<h1>Asymmetric Programming Challenge: Mobile Device Keyboard</h1>

<h2>Overview:</h2>
My solution is implemented in Python 3 (specifically 3.3.2)

There are four files of code submitted:

<h3>AutocompleteProvider.py</h3>
Contains the implementation of the AutocompleteProvider class which has the following functions<br/>

quicksort()<br/>
train()<br/>
putInDict()<br/>
getWords()<br/>
dump()<br/>

<h3>Candidate.py</h3>
Contains the implementation of the Candidate class which has the following functions<br/>

getConfidence()<br/>
getWord()<br/>
increaseConfidenceByOne()<br/>
stringify()<br/>

<h3>testOne.py</h3>
File that tests the classes implemented in the other two files. Expects input from the user to get the file to input and the fragment to input.

<h3>testTwo.py</h3>
File that tests a user choice of inputs from the user then demonstrates the difference between in the suggested words.

There are two text input files submitted:
<h3>train.txt</h3>
This is the sentence the was provided.
<h3>train2.txt</h3>
This is a random sentence from the programming challenge page.

<h2>Running my Solution:</h3>
To run this all that is required is Python 3 (default). <br/>
To test one file this is expected output with what you type in <b>bold</b>: <br/>
<b>python testOne.py</b><br/>
Please enter the name of the file you want to use to train: <b>train.txt</b> <br/>
Please enter a word: <b>th</b> <br/>
Here are some suggestions <br/>
thing (2), that (2), think (1), third (1), this (1), thoroughly. (1), the (1) <br/><br/>

To test two files this is expected output with what you type in <b>bold</b>: <br/>
<b>python testTwo.py</b><br/>
How many files are being input: <b> 2 </b> <br/>
Please enter the name of the file you want to use to train: <b>train.txt</b> <br/>
Please enter a word: <b>th</b> <br/>
Here are some suggestions <br/>
thing (2), that (2), think (1), third (1), this (1), thoroughly. (1), the (1) <br/>
Please enter the name of the file you want to use to train: <b>train2.txt</b> <br/>
Please enter a word: <b>th</b> <br/>
Here are some suggestions <br/>
the (5), thing (2), that (2), this (1), think (1), thoroughly. (1), third (1), they (1)


