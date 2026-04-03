Pendências:
1. Parser — títulos com fallback

Seletor principal: h4.card-title a
Se não achar, usar fallback: h4.card-title span
Adicionar titulo_fallback no config.py

2. Parser — botões com if

Remover a lógica de link_list[0] e link_list[1]
Substituir pelo if "Ficha" in texto / elif "Integral" in texto
Garante que registros com apenas um botão não quebram

3. Commit do parser.py após as correções
4. Próximo passo após commit: __init__ do scraper.py
