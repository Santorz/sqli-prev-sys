#!/usr/bin/python3

import dangerous_queries
from colorama import init
init()
from colorama import Fore, Style
import json
import re

# Package to check for close matches
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from difflib import SequenceMatcher
from difflib import get_close_matches

reset_styles = Style.RESET_ALL
red_text = Fore.RED
green_text = Fore.GREEN
orange_text = Fore.MAGENTA
bright_text = Style.BRIGHT

obtained_dangerous_queries = []
close_match_ratio = None
highest_match = None
obtained_ratios = []


# Dictionaries Here...
input_options = {
    "1" : dangerous_queries.dangerous_postgresql_queries,
    "2" : dangerous_queries.dangerous_mysql_queries,
}

db_versions = {
    "1" : "PostgreSQL",
    "2" : "MySQL",
}

db_type_input = input(f"""\n   What Database does your Software Use ? \n
    Enter '1' for PostgreSQL
    Enter '2' for MySQL \n \n    Your Response =>  """)

print()

# Loop through and access their respective dictionaries

def main_control():
    
    for first_key, first_value in input_options.items():
            dangerous_queries_dict = first_value
        # Check if the input matches any key in the dictionaries and if true...
            if db_type_input == first_key:
                # Check if the 
                
                for db_version_key, db_version_value in db_versions.items():
                    
                    if db_type_input == db_version_key:
                        
                                                    
                        query_input = str(input(f"    Good! Now, type any {db_version_value} query you know \n\n    ==>  "))
                            
                        for second_key, second_value in dangerous_queries_dict.items():
                            obtained_dangerous_queries.append(second_value)
                            
                            for i in obtained_dangerous_queries:
                                all_queries_lower = i.lower()
                                query_input_lower = query_input.lower()
                                                                                        
                                seq_match = SequenceMatcher(a= all_queries_lower, b = str(query_input_lower) )
                                ratio = (seq_match.ratio())
                                highest_match = get_close_matches(query_input, obtained_dangerous_queries)

                                obtained_ratios.append(float(ratio))
                                
                            

                            if (query_input in obtained_dangerous_queries):
                                print(f""" \n   {red_text}{bright_text}   {query_input}   {reset_styles} is a DANGEROUS {db_version_value} query ! \n""")
                                exit(0)
                        
                            elif (query_input not in obtained_dangerous_queries and float(max(obtained_ratios)) > 0.65):
                               print(f""" \n   {orange_text}{bright_text}  {query_input}  {reset_styles} is potentially dangerous !""")
                               print(f"""      It's closest match is -->  {red_text}{bright_text} {next(iter(highest_match))} {reset_styles}""")
                               exit(0)
                                    
                                    
                        
                            elif (query_input not in obtained_dangerous_queries):
                                print(f""" \n   {green_text}{bright_text}  {query_input}  {reset_styles} is either a SAFE {db_version_value} query or isn't a {db_version_value} query at all... \n""")
                                exit(0)
                            
                            else:
                                print('Blah')
                         
            
    else:
        print('Unknown Database ! \n'.upper())
        
           
                        
                         
                                
                                
                            

main_control()


for key2, val2 in db_versions.items():
    filename = val2.lower()

    with open(filename+'.json', "w") as outjsonfile:
       
        json.dump([val3 for key3, val3 in input_options.items()], outjsonfile)
        
