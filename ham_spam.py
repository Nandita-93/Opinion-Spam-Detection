import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.evaluation import MulticlassMetrics, BinaryClassificationMetrics

# Build the Spark Context

conf = SparkConf().setAppName('Big Data Project').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

# Data set prep

inp = sc.textFile('F:/6350/Project/HamSpam.txt')
tes = sc.textFile('F:/6350/Project/reviewText.txt')

# Create a spam ham seperation for the inp dataset
spamTotal = inp.filter(lambda x: x.split('\t')[0]=='spam')
spam = spamTotal.map(lambda x: x.split('\t')[1])
hamTotal = inp.filter(lambda x: x.split('\t')[0]=='ham')
ham = hamTotal.map(lambda x: x.split('\t')[1])

# Build a Hashing TF for the words

htf = HashingTF(100000)
spamFeat =  spam.map(lambda x: htf.transform(x.split(" ")))
hamFeat =  ham.map(lambda x: htf.transform(x.split(" ")))
outFeat = tes.map(lambda x: (htf.transform(x.split(" ")),x)) 

# Label features - 0 SPAM, 1 HAM

hamPoints = hamFeat.map(lambda feat: LabeledPoint(1, feat))
spamPoints = spamFeat.map(lambda feat: LabeledPoint(0, feat))

# Labeled Point for the test. All the labels will be 0.

tesPoints = outFeat.map(lambda feat: (LabeledPoint(0, feat[0]),feat[1]))
# Join the data

data = hamPoints.union(spamPoints)
data.cache()
tesPoints.cache()

(train,test) = data.randomSplit([0.8,0.2])

model = NaiveBayes.train(train,1.0)

predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))
f = open('output.txt','w')
accuracy = 1.0 * predictionAndLabel.filter(lambda x: x[0] == x[1]).count() / test.count()
accurac = accuracy * 100.0
#print('model accuracy {}'.format(accuracy))
f.write('Model Accuracy Percentage '+ str(round(accurac,2))+ '%')
f.close()

#f1 = open('tesPrediction.txt','w')
predandfeats = tesPoints.map(lambda x: (model.predict(x[0].features),x[1]))
predandfeats.saveAsTextFile('tesPrediction')

