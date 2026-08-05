# Full source parts

Pliki `app.part0`, `app.part1`, `app.part2` zawierają pełny kod aplikacji podzielony na 3 części (z powodu limitów API).

Aby złożyć pełny `app.py`:

```bash
bash assemble.sh
# lub
cat data/app.part0 data/app.part1 data/app.part2 > app.py
python app.py
```

Następnie aplikacja będzie działać z pełną funkcjonalnością (Scamalytics, 11 zakładek, enrichment itd.).
