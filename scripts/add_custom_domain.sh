#!/usr/bin/env bash
# Add sakuraballpark.com to Cloudflare Pages project "sakura" and create DNS record
set -e

TOKEN=$(awk -F'= ' '/^oauth_token/ {gsub(/"/, "", $2); print $2}' ~/.config/.wrangler/config/default.toml)
ACCOUNT=c1e878bab2d8665a0ba32e7e2f54b225
DOMAIN=sakuraballpark.com
PROJECT=sakura
TARGET=sakura-8hv.pages.dev

echo "=== 1. Find zone ID for $DOMAIN ==="
ZONE_RESP=$(curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/zones?name=$DOMAIN")
echo "$ZONE_RESP" | python3 -m json.tool | head -30
ZONE_ID=$(echo "$ZONE_RESP" | python3 -c "import sys,json; r=json.load(sys.stdin); print(r['result'][0]['id'] if r.get('result') else '')")
echo "ZONE_ID=$ZONE_ID"

if [ -z "$ZONE_ID" ]; then
  echo "ERROR: zone not found"
  exit 1
fi

echo ""
echo "=== 2. Add custom domain to Pages project ==="
curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT/pages/projects/$PROJECT/domains" \
  -d "{\"name\":\"$DOMAIN\"}" | python3 -m json.tool

echo ""
echo "=== 3. Add CNAME record (apex via CNAME flattening) ==="
curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
  -d "{\"type\":\"CNAME\",\"name\":\"@\",\"content\":\"$TARGET\",\"proxied\":true}" | python3 -m json.tool

echo ""
echo "=== 4. Add www CNAME ==="
curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
  -d "{\"type\":\"CNAME\",\"name\":\"www\",\"content\":\"$TARGET\",\"proxied\":true}" | python3 -m json.tool

echo ""
echo "=== Done ==="
