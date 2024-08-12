import re

def parse_antivirus_log(log_string):
    # Split the string by '|' and ignore the initial part
    parts = log_string.split('|')
    
    # Find the index where key-value pairs start
    for index, part in enumerate(parts):
        if '=' in part and not part.endswith(r'\='):
            break
    
    # Join the remaining parts back into a string
    remaining_string = '|'.join(parts[index:])
    
    # Use regex to parse key-value pairs
    pattern = r'(\w+)=(.+?)(?=\s+\w+=|$)'
    matches = re.findall(pattern, remaining_string)

    log_dict = {}
    for key, value in matches:
        log_dict[key] = value
    
    return log_dict

lgotobeparsed = r"(actual_string_to_be_replcaed)"

parsed_log = parse_antivirus_log(lgotobeparsed)
print(parsed_log)