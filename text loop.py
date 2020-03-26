with open('links.txt', 'r') as f: # Add the page links to links.txt in new lines
    link_list = [line.strip() for line in f]

number_of_idols = 0  # Change acordingly
number_of_pages = 0  # Number of pages you want to iterate


print(link_list)

for k in range(number_of_idols):
    idol_file = open(f'idol{k}.txt', 'w') # Output link set for each idol. Feed to JDownloader 2
    for j in range(number_of_pages):
        idol_file.write(f'{link_list[k]}?p={j + 1}\n') # Change the URL format acordingly

    idol_file.close
        
