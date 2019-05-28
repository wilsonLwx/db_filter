# __author__ = 'wilsonLwx'
# __date__ = '2019/5/28'
import yaml
import os


class DBFilter:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            db_config = yaml.load(f)
            ex_db_config = db_config.get('ex_db_config')
            im_db_config = db_config.get('im_db_config')

            ex_host = ex_db_config.get('host')
            ex_port = ex_db_config.get('port', 3306)
            ex_user = ex_db_config.get('user')
            ex_pwd = ex_db_config.get('pwd')
            ex_db = ex_db_config.get('db')
            ex_table = ex_db_config.get('table')
            ex_save_path = ex_db_config.get('save_path', './')

            im_host = im_db_config.get('host')
            im_port = im_db_config.get('port', 3306)
            im_user = im_db_config.get('user')
            im_pwd = im_db_config.get('pwd')
            im_db = im_db_config.get('db')
            file_name = im_db_config.get('file_name')

        self.ex_str = 'mysqldump -h{host} -P{port} -u{user} -p{pwd} {db} {table} > {save_path}{table}.sql'.format(
            host=ex_host, port=ex_port,
            user=ex_user, pwd=ex_pwd, db=ex_db,
            table=ex_table, save_path=ex_save_path)

        self.im_str = 'mysql -h{host} -P{port} -u{user} -p{pwd} {db} < {file_name}'.format(
            host=im_host,
            port=im_port,
            user=im_user,
            pwd=im_pwd,
            db=im_db,
            file_name=file_name
        )

    def export_data(self):
        print(self.ex_str)
        os.system(self.ex_str)

    def import_data(self):
        print(self.im_str)
        os.system(self.im_str)


if __name__ == '__main__':
    db_filter = DBFilter('config.yml')
    db_filter.import_data()
