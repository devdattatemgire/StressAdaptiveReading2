import csv
from myapp.models import KnowledgeBase  # Replace 'myapp' with the name of your Django app

def import_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists in your CSV file

        for row in csv_reader:
            KnowledgeBase.objects.create(
                subject_id=row[0],
                subject_name=row[1],
                topic_name=row[2],
                text=row[3],
                level=row[4],
                q1=int(row[5]),
                q2=int(row[6]),
                q3=int(row[7]),
                q4=int(row[8]),
                q5=int(row[9]),
                a1=int(row[10]),
                a2=int(row[11]),
                a3=int(row[12]),
                a4=int(row[13]),
                a5=int(row[14])
            )

# Usage example
csv_file_path = 'path/to/your/csvfile.csv'
import_data_from_csv(csv_file_path)
