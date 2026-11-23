# The World in One Day — Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/syuaibcvk/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/syuaibcvk/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One picture of one day: a newspaper front page for Sunday 22 November
2026. The lead story is the collapse of COP31 in Antalya — after more
than two weeks of talks, the longest UN climate summit ever, the EU and
around 130 parties refused to endorse the "Antalya Pact" because its
final draft never named coal, oil or gas, and UN chief António Guterres
answered: "There is no ambiguity in the science." Around it: a Russian
drone flattens part of an apartment block in Dymer, near Kyiv (four
killed there, three in Vyshneve, 14 missing); suspected Ukrainian sea
drones sink the Russian corvette Merkury at its berth in Benghazi;
Iran strikes a civilian industrial site in Bahrain on Saturday, two
hurt, as Gulf states condemn; Chuck Hubbard's recount win gives the
Democrats at least 258 House seats, their largest majority since 1992;
Reuters reports the SEC is examining Nvidia's accounting as the AI
sell-off deepens; Trump dares Iran to test the US blockade as 14
tankers mass at Kharg Island; settlers torch cars and homes near
Ramallah; the Houthis claim a strike on the Rabigh refinery; drones hit
homes and a UN building in Khartoum; special forces capture "El Chapo
Isidro" in Sinaloa; South Korea's education minister resigns over the
AI exam-cheating chaos; and fire sweeps a candy factory in Cikande,
Banten. In brief: a boat capsizes in Bayelsa, Paolo Bulgari dies aged
89, and the EU and Indonesia sign a deal scrapping tariffs on 98.5% of
EU goods.

Every headline and figure was cross-checked on 22–23 November 2026
against reporting from Reuters, BBC, CNN, AP, France 24, The Guardian,
Al Jazeera, Le Monde, The Hindu, Yonhap, Euronews, Middle East Eye and
the Straits Times. Saturday events are dated in the text; the market
figures in the masthead are Friday 20 November closes, labelled as
such. Two stories from the brief were deliberately left out after
checking: BepiColombo entered Mercury orbit on 21 November, not the
22nd, and the Sinaloa death toll is 11 (seven gunmen, four soldiers)
per the AP and Mexico's Defense Ministry, not 20.

## How it was made

`entry.png` was drawn by `render_frontpage.py` — a from-scratch Pillow
program (fixed text, fixed DejaVu fonts, fixed geometry, no network,
no clock) that lives in the workspace next to this repository. Running
it twice writes byte-identical PNGs. `main.py` (Python 3.13, standard
library only) simply delivers that picture: it verifies the PNG
signature, the 1 MiB size cap and the pinned SHA-256 of the bundled
`entry.png`, copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`), then verifies the copy is byte-identical.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

make.fun referral code: `m4wxdrjn`

## License

MIT — see [LICENSE](LICENSE).
