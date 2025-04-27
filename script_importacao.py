
import json
from bandas.models import Band, Album, Music  # Adjust 'curso' to your app name

def importar_dados(bandas_file, discos_file):
    # Load band data
    with open(bandas_file, 'r', encoding='utf-8') as f:
        bandas_json = json.load(f)
        for b in bandas_json:
            # Create band if it doesn't exist
            Band.objects.get_or_create(
                nome=b["nome"],
                defaults={
                    "nr_elementos": 4,  # default value
                    "ano_criacao": b["ano_criacao"]
                }
            )

    # Load album data
    with open(discos_file, 'r', encoding='utf-8') as f:
        discos_json = json.load(f)
        for disco in discos_json:
            # Get the band
            banda = Band.objects.get(nome=disco["banda"])

            # Create the album
            album = Album.objects.create(
                nome=disco["titulo"],
                nr_musicas=len(disco["musicas"]),
                band=banda,
                spotify_link="link"  # default value
            )

            # Create songs
            for m in disco["musicas"]:
                Music.objects.create(
                    nome=m["titulo"],
                    duration=m["duracao"],
                    album=album,
                    spotify_link="link",  # default value
                    lyrics="..."  # default value
                )
