#!/bin/bash

# Açık pull request'leri listele
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Organiser: K. Umut Araz

# Her bir pull request üzerinde döngü
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_numara=$(echo "$pr" | jq -r '.number')
  pr_baslik=$(echo "$pr" | jq -r '.title')
  pr_etiketler=$(echo "$pr" | jq -r '.labels')

  # "require type hints" etiketinin mevcut olup olmadığını kontrol et
  tip_ipucu_gerekiyor=$(echo "$pr_etiketler" | jq -r '.[] | select(.name == "require type hints")')
  echo "Kontrol ediliyor PR #$pr_numara: $pr_baslik ($tip_ipucu_gerekiyor) ($pr_etiketler)"

  # Eğer tip_ipucu_gerekiyor varsa, pull request'i kapat
  if [[ -n "$tip_ipucu_gerekiyor" ]]; then
    echo "Kapatılıyor PR #$pr_numara: $pr_baslik 'require type hints' etiketi nedeniyle"
    gh pr close "$pr_numara" --comment "'Require type hints' etiketine sahip PR'lar Hacktoberfest için kapatılıyor"
  fi
done
