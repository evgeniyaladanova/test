from pyspark.sql import SparkSession
from pyspark import SQLContext

spark = SparkSession.builder.appName("EMR").getOrCreate()

sc = spark.sparkContext
sqlContext = SQLContext(sparkContext=sc)

aps_result = spark.sql("SELECT 1")

aps_result.write.mode('overwrite').parquet('s3://evgladtest/result2')

spark.stop()