# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ad9a3f2c-25db-4f4a-b956-d8a354a856c4",
# META       "default_lakehouse_name": "SalesLH",
# META       "default_lakehouse_workspace_id": "a894cc19-45d2-420b-884d-4dc7fc44fb12",
# META       "known_lakehouses": [
# META         {
# META           "id": "ad9a3f2c-25db-4f4a-b956-d8a354a856c4"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
