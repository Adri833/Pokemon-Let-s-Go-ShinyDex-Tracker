import discord
import io
from discord.ext import commands
import json
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import aiohttp

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
    relleno = int((ancho - 4) * porcentaje)

    # Crear imagen transparente
    img = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Fondo gris con bordes redondeados
    draw.rounded_rectangle([0, 0, ancho, alto], radius=15, fill=(200, 200, 200), outline=(0, 0, 0), width=3)

    # Barra celeste rellena
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
    pokemon_obj = next((p for p in POKEMON_KANTO if p["name"] == pokemon_lower), None)

    if pokemon_obj is None:
        await ctx.send(f"❌ Pokémon '{pokemon}' no válido.")
        return

    if user_id not in shinydex_data:
        shinydex_data[user_id] = []

    if any(p["name"] == pokemon_lower for p in shinydex_data[user_id]):
        await ctx.send(f"⚠️ Ya tienes {pokemon_obj['name'].capitalize()} shiny.")
        return

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    shinydex_data[user_id].append({
        "id": pokemon_obj["id"],
        "name": pokemon_obj["name"],
        "date": fecha_actual
    })
    shinydex_data[user_id].sort(key=lambda x: x["id"])
    save_data()

    actual = len(shinydex_data[user_id])
    generar_barra_pokemon(actual, TOTAL_SHINIES, "barra.png")
    gif_url = f"https://play.pokemonshowdown.com/sprites/ani-shiny/{pokemon_lower}.gif"

    file = discord.File("barra.png", filename="barra.png")
    embed = discord.Embed(
        title=f"{pokemon_obj['name'].capitalize()} shiny añadido",
        description=f"¡Felicidades {ctx.author.mention}! 🌟",
        color=discord.Color.gold()
    )
    embed.set_image(url="attachment://barra.png")
    embed.set_thumbnail(url=gif_url)

    await ctx.send(file=file, embed=embed)

@bot.command()
async def soltar(ctx, *, pokemon: str):
    user_id = str(ctx.author.id)
    pokemon_lower = pokemon.lower()
    if user_id not in shinydex_data:
        await ctx.send("❌ No tienes Pokémon registrados.")
        return

    lista = shinydex_data[user_id]
    if not any(p["name"] == pokemon_lower for p in lista):
        await ctx.send(f"❌ No tienes {pokemon_lower} shiny registrado.")
        return

    shinydex_data[user_id] = [p for p in lista if p["name"] != pokemon_lower]
    save_data()
    await ctx.send(f"🗑️ {pokemon_lower.capitalize()} shiny eliminado de tu registro.")

@bot.command()
async def progreso(ctx):
    user_id = str(ctx.author.id)
    capturados = len(shinydex_data.get(user_id, []))
    generar_barra_pokemon(capturados, TOTAL_SHINIES, "barra.png")
    file = discord.File("barra.png", filename="barra.png")
    embed = discord.Embed(
        title=f"Progreso de {ctx.author.display_name}",
        description=f"Has capturado **{capturados}** de **{TOTAL_SHINIES}** shinies.",
        color=discord.Color.blue()
    )
    embed.set_image(url="attachment://barra.png")
    await ctx.send(file=file, embed=embed)

@bot.command()
async def lista(ctx, filtro: str = None):
    user_id = str(ctx.author.id)
    capturados = shinydex_data.get(user_id, [])
    if filtro == "faltan":
        faltan = [p["name"].capitalize() for p in POKEMON_KANTO if p["id"] not in [c["id"] for c in capturados]]
        await ctx.send(f"Pokémon que te faltan:\n" + ", ".join(faltan))
    else:
        tienes = [p["name"].capitalize() for p in capturados]
        await ctx.send(f"Pokémon capturados:\n" + ", ".join(tienes) if tienes else "No tienes shinies registrados.")

@bot.command()
async def random(ctx):
    user_id = str(ctx.author.id)
    capturados_ids = {p["id"] for p in shinydex_data.get(user_id, [])}
    pendientes = [p for p in POKEMON_KANTO if p["id"] not in capturados_ids]
    if not pendientes:
        await ctx.send("🎉 ¡Ya tienes todos los shinies!")
        return
    elegido = random.choice(pendientes)
    await ctx.send(f"🎯 Tu objetivo aleatorio: **{elegido['name'].capitalize()}**")

@bot.command()
async def stats(ctx):
    user_id = str(ctx.author.id)
    capturas = shinydex_data.get(user_id, [])

    if not capturas:
        await ctx.send("❌ No tienes shinies registrados.")
        return

    total_capturados = len(capturas)
    
    total_faltantes = TOTAL_SHINIES - total_capturados

    ultima = max(capturas, key=lambda x: datetime.strptime(x["date"], "%d/%m/%Y %H:%M"))
    fecha_ultima = datetime.strptime(ultima["date"], "%d/%m/%Y %H:%M")
    dias = (datetime.now() - fecha_ultima).days

    await ctx.send(
        f"📊 **Estadísticas de {ctx.author.display_name}**\n"
        f"⭐ **Progreso total:** {total_capturados}/{TOTAL_SHINIES} shinies capturados ({total_faltantes} restantes)\n"
        f"➡️ **Último shiny:** {ultima['name'].capitalize()} ({ultima['date']})\n"
        f"⏳ **Días desde la última captura:** {dias}"
    )

@bot.command()
async def historial(ctx):
    user_id = str(ctx.author.id)
    capturas = shinydex_data.get(user_id, [])
    if not capturas:
        await ctx.send("❌ No tienes shinies registrados.")
        return
    ultimos = sorted(capturas, key=lambda x: x["date"], reverse=True)[:10]
    mensaje = "\n".join([f"º🌟 {p['name'].capitalize()} — {p['date']}" for p in ultimos])
    await ctx.send(f"📝 Últimas capturas:\n{mensaje}")

@bot.command()
async def shinydex(ctx):
    user_id = str(ctx.author.id)
    capturados_ids = {p["id"] for p in shinydex_data.get(user_id, [])}

    cols = 15
    cell_size = 160
    icon_size = (130, 130)
    margen_x = (cell_size - icon_size[0]) // 2
    margen_y = (cell_size - icon_size[1]) // 2

    rows = (len(POKEMON_KANTO) + cols - 1) // cols
    img_width = cols * cell_size
    img_height = rows * cell_size

    img_base = Image.new("RGB", (img_width, img_height), color="white")
    draw = ImageDraw.Draw(img_base)
    
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    async with aiohttp.ClientSession() as session:
        for idx, pkm in enumerate(POKEMON_KANTO):
            x = (idx % cols) * cell_size
            y = (idx // cols) * cell_size
            
            # Descargar imagen del Pokémon
            if pkm["id"] in capturados_ids:
                # Si está capturado, usar la URL shiny
                url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/{pkm['id']}.png"
            else:
                # Si no está capturado, usar la URL normal
                url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pkm['id']}.png"

            async with session.get(url) as resp:
                if resp.status == 200:
                    datos = await resp.read()
                    img = Image.open(io.BytesIO(datos)).convert("RGBA")
                    img = img.resize(icon_size)

                    if pkm["id"] not in capturados_ids:
                        # Aplicar filtro de blanco y negro para los no capturados
                        img = img.convert("L").convert("RGBA")
                    
                    # Pegar la imagen en el lienzo
                    img_base.paste(img, (x + margen_x, y + margen_y), img)
                else:
                    print(f"No se pudo descargar la imagen de {pkm['name']}")

    with io.BytesIO() as image_binary:
        img_base.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="shiny_tabla.png"))

bot.run(TOKEN)