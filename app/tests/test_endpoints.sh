#!/bin/bash

BASE_URL="http://localhost:8000"

echo "🧪 Testing RideTracker API..."
echo ""

# Test 1: Health Check
echo "1️⃣ Health Check:"
curl -s "$BASE_URL/health" | jq
echo ""

# Test 2: Root
echo "2️⃣ Root Info:"
curl -s "$BASE_URL/" | jq
echo ""

# Test 3: Stats (vacío al inicio)
echo "3️⃣ Stats iniciales:"
curl -s "$BASE_URL/stats" | jq
echo ""

# Test 4: Crear clase
echo "4️⃣ Crear clase:"
RESPONSE=$(curl -s -X POST "$BASE_URL/clases" \
  -H "Content-Type: application/json" \
  -d '{
    "duracion": 60,
    "maniobras": ["paralelo", "rotonda", "incorporacion"],
    "notas": "Primera clase de prueba"
  }')
echo $RESPONSE | jq
CLASE_ID=$(echo $RESPONSE | jq -r '.id')
echo "ID creado: $CLASE_ID"
echo ""

# Test 5: Obtener todas
echo "5️⃣ Obtener todas las clases:"
curl -s "$BASE_URL/clases" | jq
echo ""

# Test 6: Obtener una por ID
echo "6️⃣ Obtener clase por ID:"
curl -s "$BASE_URL/clases/$CLASE_ID" | jq
echo ""

# Test 7: Actualizar
echo "7️⃣ Actualizar clase:"
curl -s -X PUT "$BASE_URL/clases/$CLASE_ID" \
  -H "Content-Type: application/json" \
  -d '{
    "duracion": 90,
    "maniobras": ["paralelo", "rotonda", "cambio de sentido"],
    "notas": "Clase actualizada - mejoré mucho"
  }' | jq
echo ""

# Test 8: Stats con datos
echo "8️⃣ Stats después de crear:"
curl -s "$BASE_URL/stats" | jq
echo ""

# Test 9: Errores - ID inválido
echo "9️⃣ Test error - ID inválido:"
curl -s "$BASE_URL/clases/invalid_id" | jq
echo ""

# Test 10: Errores - ID no existe
echo "🔟 Test error - ID no existe:"
curl -s "$BASE_URL/clases/507f1f77bcf86cd799439011" | jq
echo ""

# Test 11: Borrar
echo "1️⃣1️⃣ Borrar clase:"
curl -s -X DELETE "$BASE_URL/clases/$CLASE_ID"
echo "Clase borrada"
echo ""

# Test 12: Verificar que se borró
echo "1️⃣2️⃣ Verificar borrado:"
curl -s "$BASE_URL/clases" | jq
echo ""

echo "✅ Tests completados!"
