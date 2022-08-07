# ETL_tagaddod
###files:
- ETL.py : the main python script that makes the ETL pipeline and can be run using CLI
- 00- exploring the data.ipynb : just exploring the data and description
- 01- extraction of data.ipynb : to extract and transform the data
- 02- visualization.ipynb : to visualize the heat map using the final data


### description
a simple ETL task

in this repository I made an ETL pipeline to do the following:
1- extract the data from the json files (from collector nodes) 
2- transform the data as following :
  2.1- change the datetime to date time format
  2.2- fill the nulls in collector_id
  2.3- change the type of latitude , longitude and collector id to float type
3- load the data in a csv file that can be used by data analysts to visualize and get insights
4- performed simple visualization on the map using plotly 


### how to run ETL.py :
![image](https://user-images.githubusercontent.com/47314651/183311032-7ba8312f-22ae-4e11-9191-a7e4d91141c4.png)

arguments : 
1- in_path : the input path (relative or absolute) to the json file  (required)
2- out_path : the output path to output the csv file (optional) ( default : the same directory as the ETL.py)

output :
one csv file

input : 
one json file

### how ETL.py work:
1- reading the json file
2- converting the columns to the right format
3- process the rare case where the record contains a dictionary ('meta-data') containing the info
