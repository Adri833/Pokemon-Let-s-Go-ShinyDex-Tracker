Instrucciones rápidas para levantar el bot en Raspberry Pi:

1. Instalar Docker y Docker Compose:
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y docker.io docker-compose-plugin
   sudo usermod -aG docker $USER
   (cerrar sesión y volver a entrar)

2. Copiar estos archivos junto con bot.py, requirements.txt y shinydex.json
   en una carpeta de la Raspberry.

3. Renombrar .env.example a .env y poner tu token de Discord.

4. Levantar el contenedor:
   docker compose up -d --build

5. Ver logs:
   docker logs -f shinydex-bot

El archivo shinydex.json quedará persistente fuera del contenedor.
