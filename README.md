# Geonames-Gazetteer-Extraction
The script is a tool to extrac gazetteer for target language from the database released by [Geonames](https://www.geonames.org/).
Th script is written in Pythton 3.6+
# Usage
[Downlad](https://www.dropbox.com/s/oweqmcdwesa701j/alternateNames.txt?dl=0) alternateNames.txt file

[Downlad](https://www.dropbox.com/s/jik9lvx13wp8zhd/allCountries.txt?dl=0) allCountries.txt

```
python gaz_extraction.py  --target_language LAN_CODE --output_directory output_directory OUTPUT_DIR --path_allCountries FILE_PATH_1 --path_alternateNames FILE_PATH_2
```
LAN_CODE is ISO 639-1 language code

output format (separted by tab)
```
圣胡利娅-德洛里亚       Sant Julià de Lòria
圣胡利娅－德洛里亚      Sant Julià de Lòria
奥尔迪诺        Ordino
萊塞斯卡爾德－恩戈爾達  les Escaldes
恩坎普  Encamp
卡尼略  Canillo
卡尼略  Canillo
````