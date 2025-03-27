# 4_mountains_task_analysis
This is a set of tools created to help analyse data from the 4 mountains task. 
These tools were created independently of the orginal 4 mountains developer by me. I am not a professional software engineer, rather a hobbyist invovled in cognition research. Please use these files at your own risk and inspect the results critically for any unexpected output. Please let me know if there's a problem and I will attempt to resolve them - or contribute via GitHub

Please use config.txt to tell the program where the files are. This should be in the format: C:/Users/UserBob/Documents/python/four_mountains_score_files - or something. The config file must be in the same directory as the .py or .exe file

count_correct_4_mountains.py - to convert 4 mountains individual score files into a usable dataframe
The program looks in the directory - defined by config.txt
These files are structured such that they can be treated as .csv files
For each of the files, the program counts the values in the "response" column - possible values are 'TARGET', 'SPATIAL', 'CONFIGURAL', 'ELEMENT', 'NONE' and adds them to a dictionary
The responses are then arranged in a pandas dataframe with one row per participant, one column for each response type
The count in the TARGET column is the number of correct answers
Extra columns are added for the file name, and for the first three characters of the filename as this corresponds to participant number in my particular study
The dataframe is then saved in the same directory as the original files as response_frequencies_summary.csv
This file can be read and analysed by any standard stats software for further analysis
.exe file provided to assist users who are not confident running a .py script

count_correct_4_mountains_practice_check - to check general response trends by attempt number - to see if people are getting any worse or better as the test goes on
This does something similar to the above program, only it summarises results by attmept number rather than by participant
output in response_counts.csv in the same directory as the other files
