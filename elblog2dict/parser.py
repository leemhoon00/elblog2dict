import re

fields = ['type', 'timestamp', 'elb', 'client_ip', 'clent_port', 'target_ip', 'target_port', 'request_processing_time', 'target_processing_time',
          'response_processing_time', 'elb_status_code', 'target_status_code', 'received_bytes', 'sent_bytes',
          'request_method', 'url', 'http_version', 'user_agent', 'ssl_cipher', 'ssl_protocol', 'target_group_arn', 'trace_id', 'domain_name', 
          'chosen_cert_arn', 'matched_rule_priority', 'request_creation_time', 'actions_executed', 'redirect_url', 'error_reason', 
          'target_port_list', 'target_status_code_list', 'classification', 'classification_reason']

def parse(datas):
    result = []
    if type(datas) == bytes:
        datas = datas.decode('utf-8')

    datas = datas.splitlines()

    for line in datas:

        temp = 1
        extracted_data={}

        for field in fields:
            regex = re.compile(r'([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*):([0-9]*) ([^ ]*)[:-]([0-9]*) ([-.0-9]*) ([-.0-9]*) ([-.0-9]*) (|[-0-9]*) (-|[-0-9]*) ([-0-9]*) ([-0-9]*) \"([^ ]*) (.*) (- |[^ ]*)\" \"([^\"]*)\" ([A-Z0-9-_]+) ([A-Za-z0-9.-]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" ([-.0-9]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^ ]*)\" \"([^\s]+?)\" \"([^\s]+)\" \"([^ ]*)\" \"([^ ]*)\"')
            match = regex.search(line)

            if match:
                extracted_data[field] = match.group(temp)
                temp += 1

        result.append(extracted_data)

    return result