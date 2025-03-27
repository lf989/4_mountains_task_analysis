import os
import pandas as pd

def read_config(config_file_path):
    """
    Reads the directory path from a config file.
    
    Args:
        config_file_path (str): Path to the config file.
    
    Returns:
        str: The directory path read from the config file.
    """
    try:
        with open(config_file_path, 'r') as config_file:
            directory_path = config_file.readline().strip()  # Read the first line and remove any extra spaces/newlines
            return directory_path
    except Exception as e:
        print(f"Error reading config file {config_file_path}: {e}")
        return None

def get_response_frequencies(file_path):
    """
    Reads a CSV file and calculates the frequencies of each factor level in the 'response' column.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.Series: A Series containing the frequencies of each factor level in the 'response' column.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-delimited files
        
        # Calculate the frequencies of each factor level in the 'response' column
        response_frequencies = df['response'].value_counts()
        
        return response_frequencies
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def process_directory(directory_path):
    """
    Processes all text files in the specified directory and summarizes the frequencies of 'response' levels.
    
    Args:
        directory_path (str): Path to the directory containing the text files.
    
    Returns:
        pd.DataFrame: A DataFrame summarizing the frequencies of 'response' levels for each file.
    """
    # Initialize an empty list to store results
    results = []
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):  # Process only .txt files
            file_path = os.path.join(directory_path, filename)
            
            # Get the frequencies of 'response' levels for the current file
            frequencies = get_response_frequencies(file_path)
            
            if frequencies is not None:
                # Convert the Series to a dictionary and add the filename and first four characters
                result = frequencies.to_dict()
                result["filename"] = filename
                result["prefix"] = filename[:4]  # Add the first four characters of the filename
                results.append(result)
    
    # Convert the list of results to a DataFrame
    summary_df = pd.DataFrame(results).fillna(0)  # Replace NaN with 0 for missing levels
    
    # Reorder columns to have 'filename' and 'prefix' first
    columns = ["filename", "prefix"] + [col for col in summary_df.columns if col not in ("filename", "prefix")]
    summary_df = summary_df[columns]
    
    return summary_df

def main():
    """
    Main function to execute the program.
    """
    # Path to the config file
    config_file_path = "config.txt"  # Replace with the path to your config file if needed
    
    # Read the directory path from the config file
    directory_path = read_config(config_file_path)
    
    if directory_path is None:
        print("Error: Could not read directory path from config file.")
        return
    
    # Validate directory path
    if not os.path.isdir(directory_path):
        print(f"Error: The provided path '{directory_path}' is not a valid directory.")
        return
    
    # Process the directory and get the summary DataFrame
    summary_df = process_directory(directory_path)
    
    # Save the summary DataFrame as a CSV file in the same directory
    output_csv_path = os.path.join(directory_path, "response_frequencies_summary.csv")
    summary_df.to_csv(output_csv_path, index=False)
    
    print(f"Summary results saved to {output_csv_path}")

if __name__ == "__main__":
    main()
