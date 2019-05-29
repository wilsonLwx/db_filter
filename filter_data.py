import csv


def filter_data(file_name):
    with open(file_name, 'r') as f:
        content = csv.DictReader(f, delimiter=',')
        temp = []
        for row in content:
            row = dict(row)
            row1 = row['']
            del row['']

            temp += ['{},{},{}'.format(row1, k, v) for k, v in row.items()]
        for i in temp:
            with open('new.csv', 'a+') as f:
                f.seek(0, 0)
                title = f.readline()
                title_str = 'gene_symbol,gene_id,exp\n'
                if title != title_str:
                    f.write(title_str)
                    f.write(i + '\n')
                else:
                    f.write(i + '\n')


if __name__ == '__main__':
    filter_data('config.csv')
