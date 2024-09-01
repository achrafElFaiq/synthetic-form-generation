#!bash

if [ -z "$1" ]
 then
  python scrape.py free-for-commercial-use 50
else
  python scrape.py free-for-commercial-use $1
fi

echo Veuillez supprimer les éventuelles polices qui vous semblent illisibles dans le dossier data/fonts et appuyez sur entrée.
read varname

ls ../data/fonts/ > ../data/fonts/fonts.list

python clean.py ../data/fonts
