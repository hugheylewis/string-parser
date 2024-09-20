import re

strings_file = input("Enter path to file: ")

def find_ip_addresses(text):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ip_pattern, text)
   
def find_win32_api_functions(text):
    function_pattern = r'\b(?:Create|Get|Set|Post|Send|Close|Delete|Open|Begin|End|Register|Unregister|Message|Update|Load|Free|Enable|Disable|Show|Hide|Query|Check|Write|Read|Print|Translate|Init|Exit)[A-Z][a-zA-Z0-9]*(?:A|W)?(?:Ex)?\b'
    return re.findall(function_pattern, text)

with open(strings_file, "r") as sf:
    file_as_string = ''.join(sf.readlines()).strip()
    
    ip_addresses = find_ip_addresses(file_as_string)
    ip_set = set(ip_addresses)
    unique_ip_list = (list(ip_set))
    
    api_functions = find_win32_api_functions(file_as_string)
    api_functions_filtered = list(filter(None, api_functions))
    function_set = set(api_functions_filtered)
    unique_function_list = (list(function_set))
    
    print("\n\n[+] Finding IPs...")
    if len(unique_ip_list) > 0:
        for i in unique_ip_list:
            print(f"\t- Potential IP: {i}")
    else:
        print("No hard-coded IPs found")
        
    print("\n\n[+] Finding Win32 API Function Calls...")
    if len(unique_function_list) > 0:
        for i in unique_function_list:
            print(f"\t- Potential Win32 API Function: {i}")
    else:
        print("\t[-] No API calls found")