import csv

def text_to_csv(input_file, output_file):
    # Open the input text file for reading
    with open(input_file, 'r') as f:
        # Read the lines from the text file
        lines = f.readlines()

    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(['Time_step', 'Transaction_Id', 'Sender_Id', 'Sender_Account', 'Sender_Country',
                             'Sender_Sector', 'Sender_lob', 'Bene_Id', 'Bene_Account', 'Bene_Country',
                             'USD_amount', 'Label', 'Transaction_Type'])

        # Iterate over each line in the text file
        for i, line in enumerate(lines):
            # Skip the header row
            if i == 0:
                continue
            
            # Split the line into columns based on the comma separator
            columns = line.strip().split(',')
            
            # Write the columns to the CSV file
            csv_writer.writerow(columns)

# Example usage
input_file = 'fraud_payment_data.txt'
output_file = 'fraud_payment_data.csv'
text_to_csv(input_file, output_file)
