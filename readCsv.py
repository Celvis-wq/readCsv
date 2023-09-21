# readCsv.py
# Celvis

# Function to read the CSV file and return the list of lines
def readCsv(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Function to parse the CSV data into two separate lists
def parseCsv(csvLines):
    countryNames = []
    countryCodes = []
    
    for line in csvLines:
        columns = line.strip().split(',')
        if len(columns) == 2:
            countryNames.append(columns[0])
            countryCodes.append(columns[1])
    
    return countryNames, countryCodes

# Function to output the data
def outputData(countryNames, countryCodes):
    print("Name\nCode\n")
    for name, code in zip(countryNames, countryCodes):
        print(name)
        print(code)
        print("- - - - -")

# check
if __name__ == "__main__":
    csvFilename = 'data.csv'
    
    # Read the CSV file
    csvLines = readCsv(csvFilename)
    
    if csvLines:
        # Parse the CSV data
        countryNames, countryCodes = parseCsv(csvLines)
        
        # Print the data
        outputData(countryNames, countryCodes)