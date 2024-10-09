#!/bin/bash

# Organiser: K. Umut Araz

# Açık pull request'leri listele
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Her bir pull request üzerinde döngü
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_numara=$(echo "$pr" | jq -r '.number')
  pr_baslik=$(echo "$pr" | jq -r '.title')
  pr_etiketler=$(echo "$pr" | jq -r '.labels')

  # "tests are failing" etiketinin mevcut olup olmadığını kontrol et
  testler_basarisiz=$(echo "$pr_etiketler" | jq -r '.[] | select(.name == "tests are failing")')
  echo "Kontrol ediliyor PR #$pr_numara: $pr_baslik ($testler_basarisiz) ($pr_etiketler)"

  # Eğer testler başarısızsa, pull request'i kapat
  if [[ -n "$testler_basarisiz" ]]; then    
    echo "Kapatılıyor PR #$pr_numara: $pr_baslik 'tests are failing' etiketi nedeniyle"
    gh pr close "$pr_numara" --comment "'tests are failing' etiketi nedeniyle kapatılıyor"
    sleep 2
  fi
done
