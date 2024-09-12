#!/bin/bash

INPUT_FILE="access.log"

OUTPUT_FILE="report.txt"

# Total number of requests
lines=$(grep -c '.' "$INPUT_FILE")

# Number of unique IP adresses
count=$(awk '{ips[$1]++} END {print length(ips)}' "$INPUT_FILE")

# Number of requests by methods
methods=$(awk '{match($0, /"[A-Z]+/); print substr($0, RSTART+1, RLENGTH)}' "$INPUT_FILE" | sort | uniq -c)

#  Most popular url
purl=$(awk '{urls[$7]++} END {max_count = 0; max_url = ""; for (url in urls) {if (urls[url] > max_count) {max_count = urls[url]; max_url = url}} print max_count " " max_url}' "$INPUT_FILE")

# Create the report
echo "Отчет о логе веб-сервера" > "$OUTPUT_FILE"
echo "========================" >> "$OUTPUT_FILE"
echo -e "Общее количество запросов:\t$lines" >> "$OUTPUT_FILE"
echo -e "Количество уникальных IP-адресов:\t$count" >> "$OUTPUT_FILE"
echo -e "\nКоличество запросов по методам:" >> "$OUTPUT_FILE"
echo "$methods" >> "$OUTPUT_FILE"
echo -e "\nСамый популярный URL:\t$purl" >> "$OUTPUT_FILE"

echo "Отчет сохранен в файл $OUTPUT_FILE"
