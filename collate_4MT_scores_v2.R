# Data analysis for Akili Mali 2025
# © copyright of Lachlan Fotheringham

# Initialize workspace
rm(list = ls())
cat("\14")
setwd("/Users/lfoth/Documents/R/spatial navigation/4MT Results SS interim")

# Load necessary libraries
library(tidyverse)

# Custom function to count response scores from a file
count_scores <- function(file_name) {
  
  # Read in table and define response levels
  tmp <- read_delim(file_name, delim = "\t", show_col_types = FALSE) %>%
    mutate(response = factor(response, 
                             levels = c("TARGET", "CONFIGURAL", "ELEMENT", "SPATIAL", "NONE"))) %>%
    count(response, .drop = FALSE) %>% #don't lose factor levels even if they don't appear as a response
    pivot_wider(names_from = response, values_from = n)%>% # put the counts into the wide format
    mutate(ID = str_extract(file_name, "(?<=./)[A-Za-z]\\d+")) # applies a regex to extract the participant number from the filename and place it in a column called "ID"
}

# Get a list of .txt files in the directory
files <- list.files(pattern = "\\.txt$", full.names = TRUE)

# Count the scores for each of the files and combine them into one data frame
scores_for_all_df <- map_dfr(files, count_scores)

# Output data to CSV
write_csv(scores_for_all_df, '4MT_scores_all_participants_v2.csv')