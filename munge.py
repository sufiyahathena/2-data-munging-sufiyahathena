# Place code below to do the munging part of this assignment.

def process_numbers(numbers):
    processed_numbers = []
    for num in numbers:
        try:
            processed_num = int(num)  # Attempt to turn the input into an integer
            if processed_num < 1879:
                result = (processed_num / 100) * 1.8
                formatted_result = "{:.1f}".format(result)  # Format the number into a string with one decimal place
                processed_numbers.append(formatted_result)
            else:
                processed_numbers.append(num)  # Keep the original number if it's not processed
        except ValueError:
            processed_numbers.append(num)  # Keep the original string if it can't be turned into an integer
    return processed_numbers


# open file
f = open("data/GLB.Ts+dSST.txt", 'r')
   
# create new file which will be our csv
f_new = open("data/clean_data.csv", 'w')


# skipping first seven lines
for i in range(7):
    f.readline().strip()   

# HEADER LINE
header = f.readline().strip()
# split to get rid of spaces between names of columns + replace with commas
column_names = header.split()
column_names_str = ','.join(column_names)
f_new.write(column_names_str +"\n")

# get rid of bottom seven lines of descriptors
all_lines = f.readlines()
for i in range(7):
    all_lines.pop()

# filter to turn into csv
for i in range(len(all_lines)):
    l_list = all_lines[i].split()
    l_str = ','.join(process_numbers(l_list))
    l_str = ','.join(l_list)
    if l_list:
        # Handle missing data by replacing '***' with 'NA'
        l_list = ['NA' if item == '***' or item == '****' else item for item in l_list]
        l_str = ','.join(l_list)

    if l_str == column_names_str: # if repeated header
        continue
    elif l_list == []: # if line break
        continue
    elif i == len(all_lines):
        f_new.write(l_str) # to not add line break on last line
    else:
        for j in range(len(l_list)):
            if j == 0: # year
                f_new.write(l_list[j] + ",")
            elif j == (len(l_list)-1): # year
                f_new.write(l_list[j])
        #for j in l_list:
            elif "*" in l_list[j]: # treat missing values
                l_list[j] = "NaN"
                f_new.write(l_list[j] + ",")
            else:
                convert = int(l_list[j]) / 100 * 1.8 # convert values
                l_list[j] = str(format(convert, ".1f")) # turn into string and format
                f_new.write(l_list[j] + ",")
        if i != len(all_lines):
            f_new.write("\n") # to not add line break on last line   
        
# close both files
f_new.close()
f.close() 
