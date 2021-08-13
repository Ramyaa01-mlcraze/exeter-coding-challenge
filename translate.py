import re #regex for matching the patterns
import os
import platform #to determine the platform 
import csv
import psutil #to measure the memory usage of the python script (install psutil package)
from datetime import datetime  #to measure the time taken to complete the process

start_time = datetime.now() 

words = {}
counter = []

#Read the french_dictionary.csv
with open('french_dictionary.csv','r') as file_csv:
    read_csv = csv.reader(file_csv)
    d1 = dict(read_csv)
    d2 = dict(d1.items())

#Read the find_words.txt
with open('find_words.txt','r') as t:
    tc = t.read()
    for a in tc.split():
        words[a] = d2[a]
        continue

#Read the t8.shakespeare.txt file
with open('t8.shakespeare.txt','r') as s:
    s_c=s.read()
    for a,b in words.items():
        s_c=s_c.replace(a,words[a])
       
       #replacing all the capitalized words
        if a.capitalize() in s_c:
            s_c=s_c.replace(a.capitalize(),words[a].capitalize())
print("t8.shakespeare.txt has been read successfully")

#Write the translated data into the t8.shakespeare.txt file
with open('t8.shakespeare.translated.txt','w') as s_w:
    s_w.write(s_c)
print("Translation Completed")

print("Frequency calculation started succesfully")

#Regex module is used to find whether all the words translated are present in the french_disctionary.csv file
for i in list(words.values()): 
        word1 = re.findall('\\b'+i+'|'+i+'s \\b', s_c.lower()) 
        counter.append(len(word1))
#print(counter)

print("Frequency calculation completed")

#Open the frequency.csv file in write mode
with open('frequency.csv','w') as csvf:
    writer=csv.writer(csvf)
    headers=['English Word','French Word','Frequency']
    writer.writerow(headers)

    #Iterating through the for loop to add the frequency of the words which was translated
    count=0
    for a,b in words.items():
        writer.writerow([a,b,counter[count]])
        count+=1

print("Frequency has been written Successfully")

#process time 
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

#platform which is used to run the python script
print(platform.system())

#memory usage of the python script to be executed
process = psutil.Process(os.getpid())
m_process = process.memory_info().rss #memory is given in bytes
m_p = m_process/1048576 #memory in bytes is converted to MB (1 MB = 1048576 bytes)
print("The memory usage is:",m_p,"in MB")