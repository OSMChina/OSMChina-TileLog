from parser_apache import parser_apache
from parser_nginx import parser_nginx

def save_to_db()->None:
    pass

if __name__ == "__main__":
    source="apache"
    if source=="apache":
        logs=parser_apache()
    else:
        logs=[]
    save_to_db(logs)