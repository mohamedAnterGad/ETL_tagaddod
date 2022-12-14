# ETL_tagaddod
### files:
- automate.py : the main scrip that we can schedule to run every day (for example) to extract all the json files from the directory and output the csv files into outputs directory
- ETL.py : the python script that makes the ETL pipeline and can be run using CLI
- 00- exploring the data.ipynb : just exploring the data and description
- 01- extraction of data.ipynb : to extract and transform the data
- 02- visualization.ipynb : to visualize the heat map using the final data
- 03- automation.ipynb : just trying the functions and testing them


### description
a simple ETL task

in this repository I made an ETL pipeline to do the following: </br>
1- extract the data from the json files (from collector nodes) </br>
2- transform the data as following :</br>
  2.1- change the datetime to date time format </br>
  2.2- fill the nulls in collector_id </br>
  2.3- change the type of latitude , longitude and collector id to float type </br>
3- load the data in a csv file that can be used by data analysts to visualize and get insights </br>
4- performed simple visualization on the map using plotly 


### how to run automate.py :
put the automate.py file in the same source directory and run
![image](https://user-images.githubusercontent.com/47314651/183449068-f1fd4e87-1f04-4f88-bb59-376e6dfddcda.png)
outputs :
- ouput directory : contains all the csv files
- processed directory : contains all the processed json files

if you prefer to run manually you can run ETL.py and put the arguments </br>
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


### enhancements:
- added automate.py script to automate the pipe line and move the processed (json) files into a new directory (processed)
- output the csv files to a new directory (outputs)

### future work and enhancement:
- we can use spark if the volumn of the data increased and we wanted to use distributed file system
