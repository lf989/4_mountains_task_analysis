# 4_mountains_task_analysis
This is a set of tools created to help analyse data from the 4 mountains task. 
These tools were created independently of the orginal 4 mountains developer by me. I am not a professional software engineer, rather a hobbyist invovled in cognition research. Please use these files at your own risk and inspect the results critically for any unexpected output. Please let me know if there's a problem and I will attempt to resolve them - or contribute via GitHub

Please use config.txt to tell the program where the files are. This should be in the format: C:/Users/UserBob/Documents/python/four_mountains_score_files - or something

The program looks in the directory - defined by config.txt
These files are structured such that they can be treated as .csv files
For each of the files, the program counts the values in the "response" column - possible values are 'TARGET', 'SPATIAL', 'CONFIGURAL', 'ELEMENT', 'NONE' and adds them to a dictionary
The responses are then arranged in a pandas dataframe with one row per participant, one column for each response type
The count in the TARGET column is the number of correct answers
Extra columns are added for the file name, and for the first three characters of the filename as this corresponds to participant number in my particular study
The dataframe is then saved in the same directory as the original files as response_frequencies_summary.csv
This file can be read and analysed by any standard stats software for further analysis
