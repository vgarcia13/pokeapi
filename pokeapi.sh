#!/bin/sh

echo "PokeAPI Earth Pokemon extractor!"
echo "By: @vgarcia13"

# Check if cURL is available
type curl >/dev/null 2>&1 || { echo >&2 "cURL is not installed. Aborting..."; exit 1; }
echo

curl -s --request GET -H "Content-Type:application/json" https://pokeapi.co/api/v2/type/ground/ -o pokeGround.json

RESPONSE=`jq '.pokemon' pokeGround.json`

echo  "${RESPONSE}" | jq -r '.[]|select(.slot==2) | [.pokemon.name, .pokemon.url] | @csv' >> twoslotgroundpokemons.csv
sed -i twoslotgroundpokemons.csv -e '1i\"NAME","URL"'

echo "Done!"
