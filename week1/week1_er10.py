with open('poem.txt', 'r') as f:
    word_frequency = {}
    max = 0
    item = ''
    for line in f:
        for word in line.split():
            word = ''.join(e if e.isalnum() or e.isspace() else '' for e in word)
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
                if word_frequency[word] > max:
                    item = word
                    max = word_frequency[word]
    # print(item)
    # print(max)
    # print(word_frequency)

with open('stocks.csv', 'r') as f:
    company_info = ['Company Name,PE Ratio,PB Ratio\n']
    for line in f:
        if line.split(',')[0] == 'Company Name':
            continue
        company_list = line.split(',')
        company_name = company_list[0]
        pe = int(company_list[1])/int(company_list[2])
        pb = int(company_list[1])/int(company_list[-1])
        company_info.append(f'{company_name},{pe},{pb}\n')
    with open('Output.csv', 'w') as k:
        for i in company_info:
            k.write(i)

