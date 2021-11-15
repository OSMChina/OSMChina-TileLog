import apache_log_parser
from pprint import pprint

apache_log_parser_line = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"")

# data = open("access.log20211011", "r").readlines()
data = open("access.log", "r").readlines()

# for i in range(len(data)):
for i in range(4):
    data_token = apache_log_parser_line(data[i])
    # pprint(data_token)
    data_dict = {}
    data_dict["basic-ip"] = data_token["remote_host"]
    data_dict["basic-time"] = data_token["time_received_tz_datetimeobj"]
    data_dict["basic-url"] = data_token["request_url"]
    data_dict["basic-traffic"] = data_token["bytes_tx"]
    data_dict["http-ver"] = "HTTP" + data_token["request_http_ver"]
    data_dict["http-method"] = data_token["request_method"]
    data_dict["http-status"] = data_token["status"]
    data_dict["http-referer"] = data_token["request_header_referer"]
    data_dict["ua-full"] = data_token["request_header_user_agent"]
    data_dict["ua-mobile"] = data_token["request_header_user_agent__is_mobile"]
    data_dict["ua-browser"] = data_token["request_header_user_agent__browser__family"] + "/" + data_token[
        "request_header_user_agent__browser__version_string"]
    data_dict["ua-os"] = data_token["request_header_user_agent__os__family"] + "/" + data_token[
        "request_header_user_agent__os__version_string"]
    pprint(data_dict)
