import csv
import pandas as pandas


def main():
	df_r=pandas.read_csv("relationship.csv")
	df_in=pandas.read_csv("information.csv")
	df_r=df_r.dropna(axis=1,how='all')
	df_in=df_in.dropna(axis=1,how='all')
	length_r=len(df_r.index)
	length_in=len(df_in.index)

	i=0 ## row number in relationship file
	for row in range (i,length_r):

		## "from"
		from1=df_r.iloc[i,0]
		k=0 ##row number in information file
		for info in range(0, length_in):
			current=df_in.iloc[k,0]
			if current==from1:
				description=df_in.iloc[k,1]
				df_r["From"].replace(from1,description,inplace=True)
				break
			else:
				k=k+1

		## "to"
		to=df_r.iloc[i,1]
		j=0
		for info in range(0, length_in):
		 	current=df_in.iloc[j,0]
		 	if current==to:
		 		description=df_in.iloc[j,1]
		 		df_r["To"].replace(to,description,inplace=True)
		 		break
		 	else:
		 		j=j+1
		i=i+1
	print(df_r)	
main()

