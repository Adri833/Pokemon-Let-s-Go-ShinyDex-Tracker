import discord
import io
from discord.ext import commands
import json
import os
from PIL import Image, ImageDraw, ImageFont

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = "!"
TOTAL_SHINIES = 150  # excluyendo Mew, Meltan y Melmetal
POKEMON_KANTO = [
    {"id": 1, "name": "bulbasaur"},
    {"id": 2, "name": "ivysaur"},
    {"id": 3, "name": "venusaur"},
    {"id": 4, "name": "charmander"},
    {"id": 5, "name": "charmeleon"},
    {"id": 6, "name": "charizard"},
    {"id": 7, "name": "squirtle"},
    {"id": 8, "name": "wartortle"},
    {"id": 9, "name": "blastoise"},
    {"id": 10, "name": "caterpie"},
    {"id": 11, "name": "metapod"},
    {"id": 12, "name": "butterfree"},
    {"id": 13, "name": "weedle"},
    {"id": 14, "name": "kakuna"},
    {"id": 15, "name": "beedrill"},
    {"id": 16, "name": "pidgey"},
    {"id": 17, "name": "pidgeotto"},
    {"id": 18, "name": "pidgeot"},
    {"id": 19, "name": "rattata"},
    {"id": 20, "name": "raticate"},
    {"id": 21, "name": "spearow"},
    {"id": 22, "name": "fearow"},
    {"id": 23, "name": "ekans"},
    {"id": 24, "name": "arbok"},
    {"id": 25, "name": "pikachu"},
    {"id": 26, "name": "raichu"},
    {"id": 27, "name": "sandshrew"},
    {"id": 28, "name": "sandslash"},
    {"id": 29, "name": "nidoran-f"},
    {"id": 30, "name": "nidorina"},
    {"id": 31, "name": "nidoqueen"},
    {"id": 32, "name": "nidoran-m"},
    {"id": 33, "name": "nidorino"},
    {"id": 34, "name": "nidoking"},
    {"id": 35, "name": "clefairy"},
    {"id": 36, "name": "clefable"},
    {"id": 37, "name": "vulpix"},
    {"id": 38, "name": "ninetales"},
    {"id": 39, "name": "jigglypuff"},
    {"id": 40, "name": "wigglytuff"},
    {"id": 41, "name": "zubat"},
    {"id": 42, "name": "golbat"},
    {"id": 43, "name": "oddish"},
    {"id": 44, "name": "gloom"},
    {"id": 45, "name": "vileplume"},
    {"id": 46, "name": "paras"},
    {"id": 47, "name": "parasect"},
    {"id": 48, "name": "venonat"},
    {"id": 49, "name": "venomoth"},
    {"id": 50, "name": "diglett"},
    {"id": 51, "name": "dugtrio"},
    {"id": 52, "name": "meowth"},
    {"id": 53, "name": "persian"},
    {"id": 54, "name": "psyduck"},
    {"id": 55, "name": "golduck"},
    {"id": 56, "name": "mankey"},
    {"id": 57, "name": "primeape"},
    {"id": 58, "name": "growlithe"},
    {"id": 59, "name": "arcanine"},
    {"id": 60, "name": "poliwag"},
    {"id": 61, "name": "poliwhirl"},
    {"id": 62, "name": "poliwrath"},
    {"id": 63, "name": "abra"},
    {"id": 64, "name": "kadabra"},
    {"id": 65, "name": "alakazam"},
    {"id": 66, "name": "machop"},
    {"id": 67, "name": "machoke"},
    {"id": 68, "name": "machamp"},
    {"id": 69, "name": "bellsprout"},
    {"id": 70, "name": "weepinbell"},
    {"id": 71, "name": "victreebel"},
    {"id": 72, "name": "tentacool"},
    {"id": 73, "name": "tentacruel"},
    {"id": 74, "name": "geodude"},
    {"id": 75, "name": "graveler"},
    {"id": 76, "name": "golem"},
    {"id": 77, "name": "ponyta"},
    {"id": 78, "name": "rapidash"},
    {"id": 79, "name": "slowpoke"},
    {"id": 80, "name": "slowbro"},
    {"id": 81, "name": "magnemite"},
    {"id": 82, "name": "magneton"},
    {"id": 83, "name": "farfetchd"},
    {"id": 84, "name": "doduo"},
    {"id": 85, "name": "dodrio"},
    {"id": 86, "name": "seel"},
    {"id": 87, "name": "dewgong"},
    {"id": 88, "name": "grimer"},
    {"id": 89, "name": "muk"},
    {"id": 90, "name": "shellder"},
    {"id": 91, "name": "cloyster"},
    {"id": 92, "name": "gastly"},
    {"id": 93, "name": "haunter"},
    {"id": 94, "name": "gengar"},
    {"id": 95, "name": "onix"},
    {"id": 96, "name": "drowzee"},
    {"id": 97, "name": "hypno"},
    {"id": 98, "name": "krabby"},
    {"id": 99, "name": "kingler"},
    {"id": 100, "name": "voltorb"},
    {"id": 101, "name": "electrode"},
    {"id": 102, "name": "exeggcute"},
    {"id": 103, "name": "exeggutor"},
    {"id": 104, "name": "cubone"},
    {"id": 105, "name": "marowak"},
    {"id": 106, "name": "hitmonlee"},
    {"id": 107, "name": "hitmonchan"},
    {"id": 108, "name": "lickitung"},
    {"id": 109, "name": "koffing"},
    {"id": 110, "name": "weezing"},
    {"id": 111, "name": "rhyhorn"},
    {"id": 112, "name": "rhydon"},
    {"id": 113, "name": "chansey"},
    {"id": 114, "name": "tangela"},
    {"id": 115, "name": "kangaskhan"},
    {"id": 116, "name": "horsea"},
    {"id": 117, "name": "seadra"},
    {"id": 118, "name": "goldeen"},
    {"id": 119, "name": "seaking"},
    {"id": 120, "name": "staryu"},
    {"id": 121, "name": "starmie"},
    {"id": 122, "name": "mr-mime"},
    {"id": 123, "name": "scyther"},
    {"id": 124, "name": "jynx"},
    {"id": 125, "name": "electabuzz"},
    {"id": 126, "name": "magmar"},
    {"id": 127, "name": "pinsir"},
    {"id": 128, "name": "tauros"},
    {"id": 129, "name": "magikarp"},
    {"id": 130, "name": "gyarados"},
    {"id": 131, "name": "lapras"},
    {"id": 132, "name": "ditto"},
    {"id": 133, "name": "eevee"},
    {"id": 134, "name": "vaporeon"},
    {"id": 135, "name": "jolteon"},
    {"id": 136, "name": "flareon"},
    {"id": 137, "name": "porygon"},
    {"id": 138, "name": "omanyte"},
    {"id": 139, "name": "omastar"},
    {"id": 140, "name": "kabuto"},
    {"id": 141, "name": "kabutops"},
    {"id": 142, "name": "aerodactyl"},
    {"id": 143, "name": "snorlax"},
    {"id": 144, "name": "articuno"},
    {"id": 145, "name": "zapdos"},
    {"id": 146, "name": "moltres"},
    {"id": 147, "name": "dratini"},
    {"id": 148, "name": "dragonair"},
    {"id": 149, "name": "dragonite"},
    {"id": 150, "name": "mewtwo"}
]

if os.path.exists("shinydex.json"):
    with open("shinydex.json", "r") as f:
        shinydex_data = json.load(f)
else:
    shinydex_data = {}

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

def save_data():
    with open("shinydex.json", "w") as f:
        json.dump(shinydex_data, f, indent=4)

def generar_barra_pokemon(actual, total, archivo="barra.png"):
    ancho, alto = 500, 50
    porcentaje = actual / total
    relleno = int((ancho - 4) * porcentaje)  # margen para el borde

    # Crear imagen transparente
    img = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Fondo gris con bordes redondeados
    draw.rounded_rectangle([0, 0, ancho, alto], radius=15, fill=(200, 200, 200), outline=(0, 0, 0), width=3)

    # Barra amarilla rellena
    draw.rounded_rectangle([2, 2, relleno, alto - 2], radius=13, fill=(151, 240, 240))

    # Texto encima
    texto = f"{actual}/{total} ({porcentaje*100:.1f}%)"
    try:
        fuente = ImageFont.truetype("arial.ttf", 22)
    except:
        fuente = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), texto, font=fuente)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    draw.text(((ancho - text_w) / 2, (alto - text_h) / 2), texto, fill=(0, 0, 0), font=fuente)

    img.save(archivo)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def capturar(ctx, *, pokemon: str):
    user_id = str(ctx.author.id)
    pokemon_lower = pokemon.lower()

    # Buscar el pokemon en la lista para validar y obtener el id
    pokemon_obj = next((p for p in POKEMON_KANTO if p["name"] == pokemon_lower), None)

    if pokemon_obj is None:
        await ctx.send(f"❌ Pokémon '{pokemon}' no válido. Asegúrate de escribir el nombre correctamente.")
        return

    if user_id not in shinydex_data:
        shinydex_data[user_id] = []

    # Comprobar si ya tiene el pokemon capturado, buscando por nombre
    if any(p["name"] == pokemon_lower for p in shinydex_data[user_id]):
        await ctx.send(f"⚠️ Ya tienes {pokemon_obj['name'].capitalize()} shiny registrado.")
        return

    # Guardar el pokemon con id y nombre
    shinydex_data[user_id].append({"id": pokemon_obj["id"], "name": pokemon_obj["name"]})

    # Ordenar la lista del usuario por id
    shinydex_data[user_id].sort(key=lambda x: x["id"])

    save_data()

    actual = len(shinydex_data[user_id])
    generar_barra_pokemon(actual, TOTAL_SHINIES, "barra.png")

    gif_url = f"https://play.pokemonshowdown.com/sprites/ani-shiny/{pokemon_lower}.gif"

    file = discord.File("barra.png", filename="barra.png")
    embed = discord.Embed(
        title=f"{pokemon_obj['name'].capitalize()} shiny añadido",
        description=f"¡Felicidades {ctx.author.mention}! ⭐",
        color=discord.Color.gold()
    )
    embed.set_image(url="attachment://barra.png")
    embed.set_thumbnail(url=gif_url)

    await ctx.send(file=file, embed=embed)

def generar_tabla_imagen(pokemons, capturados_ids):
    # Configuraciones
    cols = 6  # columnas
    rows = (len(pokemons) + cols - 1) // cols
    cell_size = 120
    width = cols * cell_size
    height = rows * cell_size

    # Crear imagen en blanco
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Fuente para texto (puedes cambiar por path a una ttf si quieres)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    estrella = "🌟"

    for i, p in enumerate(pokemons):
        x = (i % cols) * cell_size
        y = (i // cols) * cell_size

        # Si capturado: fondo azul
        if p["id"] in capturados_ids:
            draw.rectangle([x, y, x+cell_size, y+cell_size], fill=(100, 149, 237))  # cornflowerblue

            # Estrella en esquina superior derecha
            draw.text((x + cell_size - 25, y + 5), estrella, font=font, fill="yellow")
        else:
            # Fondo blanco
            draw.rectangle([x, y, x+cell_size, y+cell_size], fill="white")

        # Escribir el nombre centrado
        nombre = p["name"].capitalize()
        bbox = draw.textbbox((0, 0), nombre, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        text_x = x + (cell_size - w) // 2
        text_y = y + (cell_size - h) // 2
        text_color = "white" if p["id"] in capturados_ids else "black"
        draw.text((text_x, text_y), nombre, font=font, fill=text_color)

    return img

@bot.command()
async def shinydex(ctx):
    user_id = str(ctx.author.id)
    capturados = shinydex_data.get(user_id, [])
    capturados_ids = {p["id"] for p in capturados}

    img = generar_tabla_imagen(POKEMON_KANTO, capturados_ids)

    with io.BytesIO() as image_binary:
        img.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="shiny_tabla.png"))

bot.run(TOKEN)
