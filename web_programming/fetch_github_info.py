#!/usr/bin/env python3
"""
sarathkaul tarafından 14/11/19 tarihinde oluşturuldu
lawric1 tarafından 24/11/20 tarihinde güncellendi

Kimlik doğrulama erişim belirteci ile yapılacaktır.
Kişisel erişim belirtecinizi oluşturmak için https://github.com/settings/tokens adresini ziyaret edin.

NOT:
Kodda asla herhangi bir kimlik bilgisi sabit kodlanmamalıdır. Özel bilgileri saklamak için her zaman bir ortam
dosyası kullanın ve çalışma zamanında bilgileri almak için `os` modülünü kullanın.

Kök dizinde bir ".env" dosyası oluşturun ve belirtecinizle birlikte bu iki satırı o dosyaya yazın::

#!/usr/bin/env bash
export USER_TOKEN=""
"""

from __future__ import annotations

import os
from typing import Any

import requests

BASE_URL = "https://api.github.com"

# https://docs.github.com/en/free-pro-team@latest/rest/reference/users#get-the-authenticated-user
AUTHENTICATED_USER_ENDPOINT = BASE_URL + "/user"

# https://github.com/settings/tokens
USER_TOKEN = os.environ.get("USER_TOKEN", "")


def fetch_github_info(auth_token: str) -> dict[Any, Any]:
    """
    requests modülünü kullanarak bir kullanıcının GitHub bilgilerini getirir
    """
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    return requests.get(AUTHENTICATED_USER_ENDPOINT, headers=headers, timeout=10).json()


if __name__ == "__main__":  # pragma: no cover
    if USER_TOKEN:
        for key, value in fetch_github_info(USER_TOKEN).items():
            print(f"{key}: {value}")
    else:
        raise ValueError("'USER_TOKEN' alanı boş olamaz.")
