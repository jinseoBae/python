import pandas as pd
#open file into csv
df = pd.read_csv('Final_Project.csv', encoding ='utf-8')
df1 = df.fillna(0) #fill all empty into zero 

#print out list of columns
print('Column Labels', df1.columns.values.tolist()) 
#print out number of rows and columns
print('Number of rows and columns', df1.shape) 

df1.dtypes #types of each columns

#print measure column summary including count, freq, top, and name
print("Measure: \n", (df1['Measure'].describe()))
#print year column summary including top, freq
print("\nYear: \n",(df1['Year'].describe()))
#print measure value summary including mean, std, min, and max
print("\nMeasure Value: \n", (df1['MeasureValue'].describe()))
#print Geo entity name summary including count,top,freq
print("\nGEO ENTITY NAME:")
print(df1['GeoEntityName'].describe(), '\n')

#set an alphabet specifically year between 2009 and 2011
x = df1[df1['Year']=="2009-2011"] 
#set an alphabet specifically 18 years and older
y = df1[df1['Measure'] == 'Rate- 18 Yrs and Older'] 
#set an alphabet specifically year between 2005 and 2007
o = df1[df1['Year']=='2005-2007']
#set an alphabet specifically year 2005
v = df1[df1['Year']=='2005']
#set an alphabet specifically year 2013
c = df1[df1['Year']=='2013']

#Find total number of participated people in each group in dataset by measure type
e = df1.Measure.value_counts()
print(e)

#Find average measure value of air quality in total of NYC
print ('Average Measure Value of air quality')
m = df1.MeasureValue.value_counts()
avg = m.mean()
print(round(avg,2)) #round it into 2 decimal place

bbb = v.groupby('Year')['Measure'].value_counts()
print(bbb, '\n') #get counts by measure type in 2005
vns = o.groupby('Year')['Measure'].value_counts()
print(vns, '\n') #get counts by measure type in 2005-2007
bnd = x.groupby('Year')['Measure'].value_counts()
print(bnd,'\n') #get counts by measure type in 2009-2011
ab = c.groupby('Year')['Measure'].value_counts()
print(ab, '\n') #get counts by measure type in 2013

#To find the averages of measure value by each Geo entity Name
df2 = df1.query('MeasureValue > 0').groupby(['GeoEntityName'], as_index = False)['MeasureValue'].mean()
print("Average of measure value by the areas \n")
print(round(df2,2))

#To find the averages of measure value by each Measure type
df3 = df1.query('MeasureValue > 0').groupby(['Measure'], as_index = False)['MeasureValue'].mean()
print("Average of measure value by measure type \n")
print(round(df3,2))


