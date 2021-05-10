#! /usr/bin/bash
echo "getting 3ed data"
# if condition to check for final
mkdir ./final_data/
curl -o 3ed_data.zip https://www.lock5stat.com/datasets3e/Lock5Data3eCSV.zip
unzip 3ed_data.zip -d ./final_data/
rm -f 3ed_data.zip
echo "3ed data retrieved"
