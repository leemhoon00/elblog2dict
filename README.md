# ELBLOG2DICT

## Description

This module converts Amazon ELB traffic logs into a python dictionary format.

## Installation

```bash
pip install elblog2dict
```

## Usage

```python
from elblog2dict import parser
import gzip

file_path = 'log1.log.gz'
with gzip.open(file_path, 'rb') as f:
    data = f.read()

extracted_data = parser.parse(data)

for data in extracted_data:
    print(data)

```

## Output

```json
{
  "type": "http",
  "timestamp": "2023-06-19T01:24:36.560391Z",
  "elb": "app/crawling-ALB/df7b42c830cab31c",
  "client_ip": "185.254.196.173",
  "clent_port": "55646",
  "target_ip": "172.31.1.83",
  "target_port": "80",
  "request_processing_time": "0.012",
  "target_processing_time": "0.001",
  "response_processing_time": "0.000",
  "elb_status_code": "404",
  "target_status_code": "404",
  "received_bytes": "231",
  "sent_bytes": "3828",
  "request_method": "GET",
  "url": "http://15.165.214.35:80/.env",
  "http_version": "HTTP/1.1",
  "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
  "ssl_cipher": "-",
  "ssl_protocol": "-",
  "target_group_arn": "arn:aws:elasticloadbalancing:ap-northeast-2:375350317796:targetgroup/crawling-TG/02bacd9ef5e3c0ab",
  "trace_id": "Root=1-648fae54-2521fdf43f8d31f87fc9061b",
  "domain_name": "-",
  "chosen_cert_arn": "-",
  "matched_rule_priority": "0",
  "request_creation_time": "2023-06-19T01:24:36.547000Z",
  "actions_executed": "waf,forward",
  "redirect_url": "-",
  "error_reason": "-",
  "target_port_list": "172.31.1.83:80",
  "target_status_code_list": "404",
  "classification": "-",
  "classification_reason": "-"
}

```

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

