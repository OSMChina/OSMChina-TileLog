import apache_log_parser
from pprint import pprint


def parser_apache()->list:

    apache_log_parser_line = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"")

    # data = open("access.log20211011", "r").readlines()
    data_file = open("access.log", "r").readlines()

    data_list=[]

    for i in range(len(data_file)):
        data_token = apache_log_parser_line(data_file[i])
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
        # pprint(data_dict)
        data_list.append(data_dict)

    pprint(data_list)

    # 接下来可以做的，对IP，UA进行统计，并且聚类，看看高频在哪里？
    # 同时可以分析一下谁下行流量最大，谁200率最低，进行地区优化

    # 此外，因为是OSM数据，所以如果是访问瓦片，可以把IP、UA、请求瓦片的三元组，打一个大大的三元组
    # 对他统计，看由IP+UA唯一标识的一个用户的访问轨迹，判断该用户的兴趣区域

    # 不准让欧盟人看见，否则GDPR警告。不过这些数据在国内是合法的
    
    return data_list