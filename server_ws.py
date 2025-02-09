import asyncio
import websockets
import serial

# Connexion série avec l'Arduino
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"📩 Commande reçue depuis Web : {message}")
        arduino.write((message + "\n").encode())  # Envoie à l'Arduino
        
        # Lire la réponse de l'Arduino et la renvoyer à la page web
        response = arduino.readline().decode().strip()
        await websocket.send(f"✅ Arduino: {response}")

# Lancer le serveur WebSockets sur le port 8765
start_server = websockets.serve(handle_client, "0.0.0.0", 8765)

print("🚀 Serveur WebSockets démarré sur ws://192.168.1.77:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
