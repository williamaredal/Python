import xml.etree.ElementTree as ET
import csv
import os
import re


filings_folder = 'C:\\Users\\willi\\Documents\\Company_filings\\BRK-A\\13F-HR\\sec_edgar_filings\\1067983\\13F-HR\\'
csv_folder = 'C:\\Users\\willi\\Documents\\Company_filings\\BRK-A\\13F-HR\\'

# NB todo:
# Rewrite script so that it operates more like the 'company_listed.py' script, searching for relevant 'start/stop' and extracting the relevant data (company_name and shares held + value of shares?), regardless of xml or txt format

def check_filing_type(check_file):
    for row in check_file:
        if "<TABLE>" in row:
            return True
            break

        elif "<XML>" in row:
            return False
            break
        else:
            continue



for filing_name in os.listdir(filings_folder):


    with open(filings_folder + filing_name, mode='r') as in_file:
        check_filing_type(in_file)
        start = False
        content = []

        if check_filing_type(in_file):
            print(filing_name, " is text")
            for line in in_file:
                print(re.sub(' +', ';', line))

            # filing is text-type
            # extract information from filing array, or write directly to new document

        else:
            print(filing_name, " is xml")
            # filing is xml-type
            # extract information from filing to array, or write directly to new document

        # open new write file
        # for loop writing from array, or just writing filtered information directly



################################################################################################

    with open(filings_folder + filing_name, mode='r') as in_file:
        start_txt = False
        start_xml = False
        end = ''
        for line in in_file:
            if "Column 1" in line:
                start_txt = True
                with open(csv_folder + '-' + filing_name.replace('txt', 'cvs'), mode='w') as out_file:
                    stripped = (line.strip() for line in in_file if start_txt)
                    lines = (line.split(',') for line in in_file if start_txt)

                    writer = csv.writer(out_file)
                    writer.writerows(lines)

                    print(in_file, lines, out_file)

            elif "<XML>" in line:
                start_xml = True
                break
            with open(csv_folder + '-' + filing_name.replace('txt', 'xml'), mode='w') as out_file:
                for copy_line in in_file:
                    out_file.write(copy_line)

                print(in_file, type(out_file))



print('Done') # Prints progress
