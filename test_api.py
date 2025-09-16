import requests
import json

# URL de la API
url = "http://127.0.0.1:8000/api/usuarios/"

# Prueba 1: Buscar usuario existente
print("=== Prueba 1: Usuario existente ===")
data_existente = {
    "cedula": "1150334017"
}

response = requests.post(url, json=data_existente)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

print("\n" + "="*50 + "\n")

# Prueba 2: Buscar usuario inexistente
print("=== Prueba 2: Usuario inexistente ===")
data_inexistente = {
    "cedula": "9999999999"
}

response = requests.post(url, json=data_inexistente)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

print("\n" + "="*50 + "\n")

# Prueba 3: Sin cédula (error)
print("=== Prueba 3: Sin cédula ===")
data_sin_cedula = {}

response = requests.post(url, json=data_sin_cedula)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")