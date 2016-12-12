# This is a sample function to test the framework
# Downloading the data, filtering and applying a model


# Import sample market data
import quandl

#spread front-month
dataSpread = quandl.get("CHRIS/CME_RK1")
#price front-month: CHRIS/CME_SG1
#dataPrice = quandl.get("CHRIS/CME_SG1")
#print(dataSpread)

# Send data to dataframe and clean up data
# this works in Jupyter with a conda notebook, not command line...
import pandas as pd
df = pd.DataFrame(dataSpread)#, columns=['isSpreadPositive'])
df.head(5)


#mydata = mydata
#remove outliers
# merge two series on dates.
# add binary variable to data (create label)

# write a function to import ticker as a parameter
# write toolbox to clean up data
