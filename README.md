# Opinion-Spam-Detection

The dataset was downloaded from: http://snap.stanford.edu/data/web-FineFoods.html

The dataset should be cleaned for special characters, formatted (timestamp to date) and properly delimited to fit our pig scripts (to extract the spam, ham data based on our heuristics) run in HDFS

The following are the cleaning python files and they should be executed on the actual dataset:

dateCleanUp.py
timeConversion.py

The outcome of this would be collected in foods.txt (the clean, formatted and delimited file) - of size around the actual dataset size with same number of records as in original dataset

The following pig scripts should be executed to extract the ham and spam review data based on heuristics (per product & per day average):

spamperday.pig
hamperday.pig
spamperproduct.pig
hamperproduct.pig

These four pig scripts would generate 

timesuspect.txt
timeham.txt
avgesupsect.txt
hamavgnew.txt

folders respectively

These HDFS Reducer output folders will have the files that are to be converted to .txt files to get the text versions of output

We saved these reducer output files as Spam_Time.txt, Ham_Time.txt, Spam_Average.txt, Ham_Average.txt respectively

These four .txt files are then combined into a single HamSpam.txt file using a simple java code (with two columns: firs column being ham/spam classification and second column as the corresponding review data)

reviewText.txt is the actual dataset with only the last column (review text column) that needs to be classified as ham or spam (based on the Naive Bayes Classification using the HamSpam.txt that has the extracted data based on heuristics)

The following .py file will execute (with HamSpam.txt and reviewText.txt in it's path) to produce the actual output:

ham_spam.py

tesPrediction.txt is the FINAL output file that would have classified the actual dataset (in this case reviewText.txt) as ham or spam reviews

Additionally, output.txt will display the accuracy of our Machine Learning Model
