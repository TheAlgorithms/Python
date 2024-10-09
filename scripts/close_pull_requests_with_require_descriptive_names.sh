#!/bin/bash

# Organiser: K. Umut Araz

# Açık pull request'leri listele
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Her bir pull request üzerinde döngü
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_numara=$(echo "$pr" | jq -r '.number')
  pr_baslik=$(echo "$pr" | jq -r '.title')
  pr_etiketler=$(echo "$pr" | jq -r '.labels')

  # "require descriptive names" etiketinin mevcut olup olmadığını kontrol et
  tanimlayici_etiketler=$(echo "$pr_etiketler" | jq -r '.[] | select(.name == "require descriptive names")')
  echo "Kontrol ediliyor PR #$pr_numara $pr_baslik ($tanimlayici_etiketler) ($pr_etiketler)"

  # Eğer tanimlayici_etiketler varsa, pull request'i kapat
  if [[ -n "$tanimlayici_etiketler" ]]; then
    echo "Kapatılıyor PR #$pr_numara $pr_baslik 'require descriptive names' etiketi nedeniyle"
    gh pr close "$pr_numara" --comment "'Require descriptive names' etiketine sahip PR'lar Hacktoberfest için kapatılıyor"
  fi
done
