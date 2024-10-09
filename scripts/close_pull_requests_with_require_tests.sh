#!/bin/bash

# Organiser: K. Umut Araz

# Açık pull request'leri listele
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Her bir pull request üzerinde döngü
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_numara=$(echo "$pr" | jq -r '.number')
  pr_baslik=$(echo "$pr" | jq -r '.title')
  pr_etiketler=$(echo "$pr" | jq -r '.labels')

  # "require_tests" etiketinin mevcut olup olmadığını kontrol et
  require_tests=$(echo "$pr_etiketler" | jq -r '.[] | select(.name == "require tests")')
  echo "Kontrol ediliyor PR #$pr_numara $pr_baslik ($require_tests) ($pr_etiketler)"

  # Eğer require_tests varsa, pull request'i kapat
  if [[ -n "$require_tests" ]]; then
    echo "Kapatılıyor PR #$pr_numara $pr_baslik 'require_tests' etiketi nedeniyle"
    gh pr close "$pr_numara" --comment "'require_tests' etiketli PR'leri Hacktoberfest için kapatıyorum"
    # sleep 2
  fi
done
