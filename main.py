import apache_log_parser

line_parser = apache_log_parser.make_parser("%h - - %t \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\"")
# line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")

data='162.158.90.242 - - [01/Nov/2021:00:30:29 +0800] "GET / HTTP/1.1" 200 1325 "https://weeklyosm.eu/de/archives/14940" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"'
# data='127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -'

log_line_data = line_parser(data)
from pprint import pprint
pprint(log_line_data)