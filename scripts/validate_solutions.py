#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import pathlib
from types import ModuleType

import pytest
import requests

# Organiser: K. Umut Araz

PROJE_EULER_DIZIN_YOLU = pathlib.Path.cwd().joinpath("project_euler")
PROJE_EULER_CEVAPLARI_YOLU = pathlib.Path.cwd().joinpath(
    "scripts", "project_euler_answers.json"
)

with open(PROJE_EULER_CEVAPLARI_YOLU) as dosya:
    PROBLEM_CEVAPLARI: dict[str, str] = json.load(dosya)


def dosya_yolunu_module_cevir(dosya_yolu: pathlib.Path) -> ModuleType:
    """Bir dosya yolunu Python modülüne dönüştürür"""
    spec = importlib.util.spec_from_file_location(dosya_yolu.name, str(dosya_yolu))
    modül = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(modül)  # type: ignore[union-attr]
    return modül


def tum_cozum_dosya_yollari() -> list[pathlib.Path]:
    """Project Euler dizinindeki tüm çözüm dosya yollarını toplar"""
    cozum_dosya_yollari = []
    for problem_dizin_yolu in PROJE_EULER_DIZIN_YOLU.iterdir():
        if problem_dizin_yolu.is_file() or problem_dizin_yolu.name.startswith("_"):
            continue
        for dosya_yolu in problem_dizin_yolu.iterdir():
            if dosya_yolu.suffix != ".py" or dosya_yolu.name.startswith(("_", "test")):
                continue
            cozum_dosya_yollari.append(dosya_yolu)
    return cozum_dosya_yollari


def dosyalarin_urlsini_al() -> str:
    """Bu eylemi tetikleyen pull request numarasını döndürür."""
    with open(os.environ["GITHUB_EVENT_PATH"]) as dosya:
        olay = json.load(dosya)
    return olay["pull_request"]["url"] + "/files"


def eklenen_cozum_dosya_yolu() -> list[pathlib.Path]:
    """Sadece mevcut pull request'te eklenen çözüm dosya yollarını toplar.

    Bu, yalnızca script GitHub Actions'tan çalıştırıldığında tetiklenecektir.
    """
    cozum_dosya_yollari = []
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }
    dosyalar = requests.get(dosyalarin_url'sini_al(), headers=headers, timeout=10).json()
    for dosya in dosyalar:
        dosya_yolu = pathlib.Path.cwd().joinpath(dosya["filename"])
        if (
            dosya_yolu.suffix != ".py"
            or dosya_yolu.name.startswith(("_", "test"))
            or not dosya_yolu.name.startswith("sol")
        ):
            continue
        cozum_dosya_yollari.append(dosya_yolu)
    return cozum_dosya_yollari


def cozum_dosya_yollarini_topla() -> list[pathlib.Path]:
    # Sadece varsa döndür, aksi takdirde tüm çözümleri varsayılan olarak döndür
    if (
        os.environ.get("CI")
        and os.environ.get("GITHUB_EVENT_NAME") == "pull_request"
        and (dosya_yolları := eklenen_cozum_dosya_yolu())
    ):
        return dosya_yolları
    return tum_cozum_dosya_yollari()


@pytest.mark.parametrize(
    "cozum_yolu",
    cozum_dosya_yollarini_topla(),
    ids=lambda yol: f"{yol.parent.name}/{yol.name}",
)
def test_proje_euler(cozum_yolu: pathlib.Path) -> None:
    """Tüm Project Euler çözümlerini test etme"""
    # problem_[bu kısmı çıkar] ve 3 genişlik için sıfırlarla doldur
    problem_numarasi: str = cozum_yolu.parent.name[8:].zfill(3)
    beklenen: str = PROBLEM_CEVAPLARI[problem_numarasi]
    cozum_modülü = dosya_yolunu_module_cevir(cozum_yolu)
    cevap = str(cozum_modülü.solution())
    cevap = hashlib.sha256(cevap.encode()).hexdigest()
    assert (
        cevap == beklenen
    ), f"{problem_numarasi} için beklenen çözümün hash'inin {beklenen} olması gerekiyordu, ama {cevap} alındı"
