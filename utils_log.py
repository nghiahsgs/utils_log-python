import logging

logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

def print_log(*para):
    para = ['%s'%e for e in para]
    content = ' '.join(para)
    print(content)
    logging.info(content)


# ham goc
print(1,2,'nghiahsgs')
# ham thay the
print_log(1,2,'nghiahsgs')
