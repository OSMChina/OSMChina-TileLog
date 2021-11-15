import apache_log_parser

apache_log_line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"")

# data = open("access.log20211011", "r").readlines()
data = open("access.log", "r").readlines()
# data='162.158.90.242 - - [01/Nov/2021:00:30:29 +0800] "GET / HTTP/1.1" 200 1325 "https://weeklyosm.eu/de/archives/14940" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"'

log_line_data = apache_log_line_parser(data[70])

from pprint import pprint
pprint(log_line_data)

# print(log_line_data)