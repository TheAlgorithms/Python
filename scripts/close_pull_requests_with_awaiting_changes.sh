#!/bin/bash

# Açık pull request'leri listele
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Organiser: K. Umut Araz

# Her bir pull request üzerinde döngü
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_numara=$(echo "$pr" | jq -r '.number')
  pr_baslik=$(echo "$pr" | jq -r '.title')
  pr_etiketler=$(echo "$pr" | jq -r '.labels')

  # "awaiting changes" etiketinin mevcut olup olmadığını kontrol et
  awaiting_changes=$(echo "$pr_etiketler" | jq -r '.[] | select(.name == "awaiting changes")')
  echo "Kontrol ediliyor PR #$pr_numara $pr_baslik ($awaiting_changes) ($pr_etiketler)"

  # Eğer awaiting_changes varsa, pull request'i kapat
  if [[ -n "$awaiting_changes" ]]; then
    echo "Kapatılıyor PR #$pr_numara $pr_baslik 'awaiting changes' etiketi nedeniyle"
    gh pr close "$pr_numara" --comment "'awaiting changes' etiketine sahip PR'ler kapatılıyor, Hacktoberfest için hazırlanıyor"
    sleep 2
  fi
done
