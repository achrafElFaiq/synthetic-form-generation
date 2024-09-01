#!bash

if [ -z "$1" ]
 then
  python scrape.py free-for-commercial-use 50
else
  python scrape.py free-for-commercial-use $1
fi

ls ../data/fonts/ > ../data/fonts/fonts.list

python clean.py ../data/fonts

python find_good_fonts.py ../data/fonts
python cnvert_scored_fonts_to_csv.py ../data/fonts scored_fonts*.csv
