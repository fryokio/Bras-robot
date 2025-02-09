#!/bin/bash

echo "🔄 Mise à jour du dépôt GitHub..."
cd /home/pi/Bras-robot
git pull origin main

echo "✅ Dépôt mis à jour."

echo "🔄 Compilation du firmware Arduino..."
arduino-cli compile --fqbn arduino:mbed_nano:nano_rp2040_connect Arduino_Code/ArduinoR4_WiFi

echo "✅ Compilation terminée."

echo "🔄 Flash du firmware sur l'Arduino..."
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:mbed_nano:nano_rp2040_connect Arduino_Code/ArduinoR4_WiFi

echo "✅ Flash terminé ! 🚀"
