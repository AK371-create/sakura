#!/usr/bin/env bash
TOKEN=$(awk -F'= ' '/^oauth_token/ {gsub(/"/, "", $2); print $2}' ~/.config/.wrangler/config/default.toml)
ZONE=684f37a5f76c562729eb566967222e18
ACCOUNT=c1e878bab2d8665a0ba32e7e2f54b225

echo "=== DNS records ==="
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE/dns_records" | python3 -m json.tool

echo ""
echo "=== Pages project domains ==="
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT/pages/projects/sakura/domains" | python3 -m json.tool
