#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import Library
from pyspark.sql import SparkSession
import pyspark
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# create  SparkSession object from within pyspark, make SparkSession.builder
# The spark.mongodb.input.uri specifies the MongoDB server address (127.0.0.1),
# the database to connect (train), and the collection (DF) from which 
# to read data, and the read preference.
# The spark.mongodb.output.uri specifies the MongoDB server address (127.0.0.1),
# the database to connect (train), and the collection (DF) to which to write data.
# Connects to port 27017 by default.
def spark_SparkSession():
    spark = SparkSession     .builder     .master("local")     .appName("myApp")     .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/train.DF")     .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/train.DF")     .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.12:3.0.0')    .getOrCreate()
    return spark

# read Data from  csv
def Read_CSV(spark):
    df = spark.read.option("header",True).option("inferSchema",True).format("csv").load(r'C:\\Users\\King\\Desktop\\project_\\train.csv')
    data=SaveAndLoad__MongoDB(df,spark)
    return data

# Write the df DataFrame to the MongoDB database and collection specified in the spark.mongodb.output.uri option by using the write method
#To read from a collection called contacts in a database called train, specify train.DF in the input URI option.
def SaveAndLoad__MongoDB(df,spark):
#     df.write.format("mongo").mode("append").save()
    data = spark.read.format('com.mongodb.spark.sql.DefaultSource').load()
    return data

def UpDate_DataFrame(data):
    # sort dataframe through columns
    sort=[]
    for i in range(0,66):sort.append(str(i))
    data = data.select(sort)
    #select rank from data
    # add new columns the name is label ,and the label is rank
    label=data.select(data[0])
    data=data.withColumn("label", label[0])
    #selsect all columns without first two
    data=data.select(data.columns[2:])    
    return data

def Build_Model(data):
    #take each iteam in the col-row have feature then add it to the new col the name is features
    assembler = VectorAssembler(inputCols=data.columns,outputCol="features")
    data_Withfeatures=assembler.transform(data)
    #to test the the model ,We divide the data to train and test
    train_split, test_split = data_Withfeatures.randomSplit(weights = [0.7, 0.3], seed = 12345)
    #create LogisticRegression model
    lr = LogisticRegression(maxIter=5, regParam=0.01, labelCol="label")
    #fit train_split
    lr_model = lr.fit(train_split)
    #make the test
    lr_result = lr_model.transform(test_split)
    #take columns after 64 columns
    features=lr_result.select(lr_result.columns[64:])
    #print 
    features.show(100)
    return lr_result,features


def main():
    spark=spark_SparkSession()
    data=Read_CSV(spark)
    data=UpDate_DataFrame(data)
    lr_result,features=Build_Model(data)
    print(features)
if __name__ == "__main__":
    main()


# In[ ]:




