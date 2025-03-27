import os
import pandas as pd

def count_targets_in_directory(directory_path):
    """
    Reads all .txt files in the specified directory and counts occurrences of "TARGET"
    in the 'response' column across all rows in each file.

    Parameters:
        directory_path (str): The path to the directory containing the .txt files.

    Returns:
        list of dict: A list of dictionaries with row number as keys and counts of 'TARGET'.
    """
    # Initialize a list to store counts of "TARGET" for each row
    target_counts = [{} for _ in range(15)]  # We know there are 15 rows to examine

    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):  # Only process .txt files
            file_path = os.path.join(directory_path, filename)

            # Read the file into a DataFrame
            try:
                df = pd.read_csv(file_path, sep='\t')  # Using tab as separator
                
                # Count 'TARGET' occurrences for each row in the response column
                for index in range(len(df)):
                    response_value = df.iloc[index]['response']
                    if 'TARGET' in response_value:
                        target_counts[index]['TARGET'] = target_counts[index].get('TARGET', 0) + 1
            
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return target_counts


def output_counts_to_csv(counts, output_file):
    """
    Outputs the counts of 'TARGET' to a CSV file.

    Parameters:
        counts (list of dict): The counts of 'TARGET' for each row.
        output_file (str): The path where the output CSV file will be saved.
    """
    # Convert the counts to a DataFrame
    counts_df = pd.DataFrame(counts)
    
    # Fill NaN values with 0 and export to CSV
    counts_df.fillna(0, inplace=True)
    counts_df.to_csv(output_file, index=False)
import os
import pandas as pd

def read_directory_from_config(config_file):
    """
    Reads the directory path from a configuration file.

    Parameters:
        config_file (str): The path to the configuration file.

    Returns:
        str: The directory path read from the config file.
    """
    try:
        with open(config_file, 'r') as f:
            directory_path = f.readline().strip()  # Read the first line and strip whitespace
            return directory_path
    except Exception as e:
        print(f"Error reading the config file {config_file}: {e}")
        return None

def count_responses_in_directory(directory_path):
    """
    Reads all .txt files in the specified directory and counts occurrences of specified responses
    in the 'response' column across all rows in each file.

    Parameters:
        directory_path (str): The path to the directory containing the .txt files.

    Returns:
        list of dict: A list of dictionaries with row number as keys and counts of each response.
    """
    # Initialize count dictionary for responses
    response_counts = [{} for _ in range(15)]  # We know there are 15 rows to examine
    possible_responses = ['TARGET', 'SPATIAL', 'CONFIGURAL', 'ELEMENT', 'NONE']

    # Initialize counts for each possible response
    for index in range(len(response_counts)):
        response_counts[index] = {response: 0 for response in possible_responses}

    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):  # Only process .txt files
            file_path = os.path.join(directory_path, filename)

            # Read the file into a DataFrame
            try:
                df = pd.read_csv(file_path, sep='\t')  # Using tab as separator
                
                # Count occurrences for each row in the response column
                for index in range(len(df)):
                    response_value = df.iloc[index]['response']
                    if response_value in possible_responses:
                        response_counts[index][response_value] += 1
            
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return response_counts

def output_counts_to_csv(counts, output_file):
    """
    Outputs the counts of responses to a CSV file.

    Parameters:
        counts (list of dict): The counts of responses for each row.
        output_file (str): The path where the output CSV file will be saved.
    """
    # Convert the counts to a DataFrame
    counts_df = pd.DataFrame(counts)
    
    # Fill NaN values with 0 and export to CSV
    counts_df.fillna(0, inplace=True)
    counts_df.to_csv(output_file, index=False)

def main():
    """
    Main function to run the script. Reads the directory path from a config file and processes the files.
    """
    # Actual config file path (the config file should be in the same directory as this script)
    config_file = os.path.join(os.path.dirname(__file__), 'config.txt')
    
    # Read the directory path from config
    directory_path = read_directory_from_config(config_file)
    
    if directory_path is not None:
        # Count the occurrences of each response
        counts = count_responses_in_directory(directory_path)

        # Output the counts to a CSV file
        output_file = os.path.join(directory_path, 'response_counts.csv')
        output_counts_to_csv(counts, output_file)
        
        print(f"Counts of responses have been output to {output_file}")

if __name__ == '__main__':
    main()