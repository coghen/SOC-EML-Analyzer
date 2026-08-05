# SOC – EML Analyzer

Zaawansowana, jednoplikowa aplikacja webowa (Flask) dla analityków **SOC** do automatycznej analizy wiadomości e-mail w formacie `.eml`.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Repozytorium:** https://github.com/coghen/SOC-EML-Analyzer

## Funkcje

| Obszar | Co robi |
|--------|--------|
| **Parsowanie .eml** | Nagłówki, załączniki (MD5/SHA256), IoC (IP, URL, domeny, e-mail, BTC) |
| **Mail Flow** | Chronologiczna oś czasu z nagłówków `Received` + relay IP |
| **DKIM / Auth** | Parsowanie DKIM (alignment), SPF/DKIM/DMARC z `Authentication-Results`, ARC, klucz publiczny z DNS |
| **Phishing score** | System 0–100 (NISKI / ŚREDNI / WYSOKI / KRYTYCZNY) z listą wskaźników |
| **Typosquatting / IDN** | Podobieństwo do marek i banków PL, homoglify, punycode |
| **Enrichment IP** | Shodan InternetDB, ip-api (proxy/VPN/geo), Tor Onionoo, DNSBL |
| **Scamalytics** | IP Fraud Risk API v3 (score, risk, VPN/Tor/datacenter, blacklisty) |
| **Hashe / URL** | MalwareBazaar, CIRCL Hashlookup, URLhaus, ThreatFox |
| **Domeny** | WHOIS, SPF/DMARC/MX, free hosting, podejrzane TLD |
| **UI** | Bootstrap 5.3, Dark Mode, 11 czytelnych zakładek, eksport HTML/PDF |

## Wymagania

- Python 3.10+
- (opcjonalnie) konto [Scamalytics](https://scamalytics.com/) – klucz API do zakładki Fraud Risk

## Instalacja (Linux / Ubuntu)

```bash
git clone https://github.com/coghen/SOC-EML-Analyzer.git
cd SOC-EML-Analyzer

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Konfiguracja Scamalytics (opcjonalna)
cp .env.example .env
# edytuj .env i wstaw SCAMALYTICS_USER oraz SCAMALYTICS_KEY

# Złóż pełny kod (jeśli używasz parts)
bash assemble.sh   # lub skopiuj pełny app.py z lokalnego środowiska development

python app.py
```

Aplikacja: **http://127.0.0.1:5000**

## Zmienne środowiskowe

| Zmienna | Opis |
|---------|------|
| `SCAMALYTICS_USER` | Username z panelu Scamalytics |
| `SCAMALYTICS_KEY` | Klucz API |
| `SCAMALYTICS_BASE` | Bazowy URL API (domyślnie węzeł EU: `https://api12.scamalytics.com/v3`) |

Bez tych zmiennych reszta analizatora działa normalnie; zakładka Scamalytics zgłosi brak konfiguracji.

## Zakładki UI

1. **Podsumowanie** – score phishingu, karty liczbowe, kluczowe nagłówki  
2. **Domeny** – werdykty, typosquatting  
3. **Adresy IP** – Shodan / ip-api / Tor / DNSBL  
4. **Ścieżka mailowa** – Mail Flow + relay IP  
5. **Załączniki** – hashe, podejrzane rozszerzenia  
6. **URL-e** – URLhaus / ThreatFox  
7. **Autentykacja i DKIM** – SPF/DKIM/DMARC + alignment + klucz DNS  
8. **Wskaźniki phishingu** – szczegółowa lista  
9. **Kryptowaluty** – adresy Bitcoin  
10. **Scamalytics** – IP Fraud Risk  
11. **IoC (SIEM)** – zbiorcza tabela + kopiuj  

## Źródła danych

| Źródło | Typ | Klucz API |
|--------|-----|----------|
| Shodan InternetDB | IP | nie |
| ip-api.com | geo / proxy | nie |
| Tor Onionoo | Tor | nie |
| DNSBL (Spamhaus, SpamCop, SORBS, Barracuda) | IP | nie |
| Abuse.ch (MalwareBazaar, URLhaus, ThreatFox) | hash / URL / IoC | nie |
| CIRCL Hashlookup | hash | nie |
| python-whois + dnspython | domeny / DNS | nie |
| **Scamalytics IP Fraud Risk API v3** | fraud score | **tak** |

## Bezpieczeństwo

- **Nie commituj** pliku `.env` ani prawdziwych kluczy API.
- Aplikacja służy do analizy **własnych** próbek SOC – nie uruchamiaj załączników z analizowanych maili.
- Domyślnie nasłuchuje tylko na `127.0.0.1`.

## Struktura

```
SOC-EML-Analyzer/
├── app.py              # loader lub pełna aplikacja (po assemble)
├── assemble.sh         # składa pełny kod z data/app.part*
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── data/
│   ├── app.part0       # część 0 pełnego kodu
│   ├── app.part1
│   ├── app.part2
│   └── README.md
└── README.md
```

> **Uwaga:** Z powodu limitów rozmiaru pojedynczego pliku w API GitHub, pełny kod (~63 kB) jest dostępny lokalnie w środowisku development (artifacts/app.py). Użyj `assemble.sh` lub skopiuj pełny plik.

## Licencja

MIT – użyj swobodnie w środowisku SOC / laboratoryjnym.
