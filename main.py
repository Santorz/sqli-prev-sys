#!/usr/bin/python3

import dangerous_queries
from colorama import init
init()
from colorama import Fore, Style

reset_styles = Style.RESET_ALL
red_text = Fore.RED
green_text = Fore.GREEN
bright_text = Style.BRIGHT

final_result = None


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
                            if query_input in second_value:
                                print(f""" \n   {red_text}{bright_text} |  {query_input}  | {reset_styles} is a very dangerous {db_version_value} query ! \n""")
                                
                            

main_control()

