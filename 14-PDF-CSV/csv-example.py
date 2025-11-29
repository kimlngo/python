import csv

#open file
data = open('example.csv', encoding='utf-8')

#csv.reader
csv_data = csv.reader(data)

#reformat it into a python object list of lists
data_lines = list(csv_data)
print(data_lines[0]) #['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']

print(len(data_lines)) #1001

# get all emails
all_emails = []

for line in data_lines[1:11]:
    all_emails.append(line[3])

print(all_emails)

# get all full names
all_full_names = []
for line in data_lines[1:11]:
    all_full_names.append(line[1] + ' ' + line[2])

print(all_full_names)

#write to a csv file
file_to_output = open('saved_file.csv', mode='w', newline='') #w means overwrite, use a for append, i.e., keep adding lines into
csv_writer = csv.writer(file_to_output, delimiter=',')

#write one row
csv_writer.writerow(['a', 'b', 'c'])

#write multiple rows
csv_writer.writerows([['1','2','3'], ['4','5','6']])
file_to_output.close()