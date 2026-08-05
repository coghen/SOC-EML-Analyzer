# Pełny kod źródłowy (podzielony)

Pliki `app.part0`, `app.part1`, `app.part2` zawierają **pełny** kod aplikacji SOC EML Analyzer (~63 kB).

## Złożenie aplikacji

Z katalogu głównego repozytorium:

```bash
bash assemble.sh
# lub ręcznie:
cat data/app.part0 data/app.part1 data/app.part2 > app.py
python app.py
```

Po złożeniu uruchom:

```bash
pip install -r requirements.txt
cp .env.example .env   # opcjonalnie Scamalytics
python app.py
```

Aplikacja: http://127.0.0.1:5000
