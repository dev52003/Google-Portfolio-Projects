#IP address to be removed
remove_list = ['100.35.170.160' , '100.8.194.42' , '104.10.121.166' , '104.128.161.128']
# Open the file that contains the allow list
with open("allow_list.txt","r") as file:
    # Read the file contents
    ip_addresses = file.read()
    # Convert the string into a list
    ip_list = ip_addresses.split()
    # Iterate through the remove list
    for address in remove_list:
        # Remove IP addresses that are on the remove list
        if address in ip_list:
            ip_list.remove(address)
    # Update the file with the revised list of IP addresses
    ip_addresses = "\n".join(ip_list)
with open("allow_list.txt","w") as file:
    file.write(ip_addresses)