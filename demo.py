from datetime import datetime
def difference_in_seconds(start_date, end_date):
    # Parse the start and end dates
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    # Calculate the difference in seconds
    difference = (end_datetime - start_datetime).total_seconds()

    return difference

# Example usage
start_date = '2022-04-01 12:00:00'
end_date = '2022-04-02 12:00:00'

difference = difference_in_seconds(start_date, end_date)
print("Difference in seconds:", difference)

import pandas as pd

# Create a sample dataframe
Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)

# Save the dataframe to a CSV file
df.to_csv('Biodata.csv', index=False)