import json
import csv
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Convert nuclei JSON output to CSV.')
parser.add_argument('--input', '-i', help='Input JSON file', required=True)
parser.add_argument('--output', '-o', help='Output CSV file', required=True)
args = parser.parse_args()

if not os.path.isfile(args.input):
    print(f'[-] File {args.input} does not exist')
    sys.exit(1)

if os.path.isfile(args.output):
    print(f'[-] File {args.output} already exists')
    sys.exit(1)

with open(args.input, 'r') as json_file:
    with open(args.output, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Template', 'Template URL', 'Template ID', 'Info Name', 'Info Author', 'Info Tags', 'Info Reference', 'Info Severity', 'Matcher Name', 'Type', 'Host', 'Matched At', 'IP', 'Timestamp', 'Curl Command', 'Matcher Status', 'Matched Line'])
        for line in json_file:
            try:
                line_json = json.loads(line)
            except json.decoder.JSONDecodeError:
                print(f'[-] JSON decoding error in line: {line}')
                continue
            template = line_json.get('template', '')
            template_url = line_json.get('template-url', '')
            template_id = line_json.get('template-id', '')
            info_name = line_json.get('info', {}).get('name', '')
            info_author = line_json.get('info', {}).get('author', '')
            info_tags = line_json.get('info', {}).get('tags', '')
            info_reference = line_json.get('info', {}).get('reference', '')
            info_severity = line_json.get('info', {}).get('severity', '')
            matcher_name = line_json.get('matcher-name', '')
            type_ = line_json.get('type', '')
            host = line_json.get('host', '')
            matched_at = line_json.get('matched-at', '')
            ip = line_json.get('ip', '')
            timestamp = line_json.get('timestamp', '')
            curl_command = line_json.get('curl-command', '')
            matcher_status = line_json.get('matcher-status', '')
            matched_line = line_json.get('matched-line', '')
            csv_writer.writerow([template, template_url, template_id, info_name, info_author, info_tags, info_reference, info_severity, matcher_name, type_, host, matched_at, ip, timestamp, curl_command, matcher_status, matched_line])

print(f'[+] Done. Output file: {args.output}')
