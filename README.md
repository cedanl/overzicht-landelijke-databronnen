# Landelijke data bronnen
"Goh, ik wist helemaal niet dat dit bestand beschikbaar was!" of "Hebben we ook zoiets voor het MBO?" horen we regelmatig bij CEDA workshops. Er is veel data beschikbaar voor onderwijstellingen, maar soms ontbreekt het overzicht. 

Daarom nu een overzicht van beschikbare data uit landelijke (en dus uniforme) bronnen voor onderwijsinstellingen. Deze bronnen bieden de mogelijkheid tot benchmarking (soms wordt dit ook expliciet aangeboden). Daarnaast zijn er vaak instellingsbestanden beschikbaar die per instelling er dus hetzelfde uitzien. Dat biedt mogelijkheden voor het gebruik van deze code en logic om deze te bewerken naar informatieproducten zoals voorspelmodellen, statistische diagnoses en dashboards.

Dit is een eerste versie, vul vooral aan! Dit kan door middel van een issue of een email naar corneel.denhartogh@surf.nl.


## Inhoudsopgave
- [Studentgegevens & Onderwijs](#studentgegevens--onderwijs)
  - [Instroom](#instroom)
  - [Inschrijvingen en Studievoortgang](#inschrijvingen-en-studievoortgang)
  - [Studententevredenheid](#studententevredenheid)
  - [Alumni en arbeidsmarkt](#alumni-en-arbeidsmarkt)
- [Institutionele Data](#institutionele-data)
  - [Financiële gegevens](#financiële-gegevens)
  - [Personeelsgegevens](#personeelsgegevens)
  - [Instellingsregistraties](#instellingsregistraties)
  - [Adresgegevens](#adresgegevens)


# Studentgegevens & Onderwijs

## Instroom

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Studielink | Studielink Telbestand | HBO, WO | Voorlopige aanmeldingen | [Toelichting telbestand](https://www.tignl.eu/downloads/studielink/pvl%20telbestand%20studielink.pdf) | [CEDA instroomprognose](https://github.com/cedanl/studentprognose) | Wekelijks | [UNL - WO bachelor](https://www.universiteitenvannederland.nl/aanmeldingen-bacheloropleidingen)|
| MBO Voorzieningen | CAMBO | MBO | Voorlopige aanmeldingen | [Voorziening Centraal aanmelden](https://mbovoorzieningen.nl/voorzieningen/voorziening-centraal-aanmelden/) | | Wekelijks | |

## Inschrijvingen en Studievoortgang

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | ROD 1CijferHO | HBO, WO | Instroom, inschrijvingen en diploma's | [DUO - ROD Controle studentgegevens](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/bron-controleren/bekostigingsstatus-studenten.jsp)| [CEDA Pythong Package](https://github.com/cedanl/eencijfer), [CEDA Power BI dashboard](https://github.com/ed2c/1cho_ins_visualisation_powerbi), [CEDA R Preparatie](https://github.com/cedanl/1cho_ins_preparation_r)| Jaarlijks begin februari | [DUO - Geaggregeerde data en voorspellingen](https://www.duo.nl/open_onderwijsdata/hoger-onderwijs/aantal-studenten/), [VH - HBO Inschrijvingen](https://www.vereniginghogescholen.nl/kennisbank/feiten-en-cijfers/artikelen/dashboard-instroom-inschrijvingen-en-diploma-s), [VH - HBO Studiesucces](https://www.vereniginghogescholen.nl/kennisbank/feiten-en-cijfers/artikelen/dashboard-instroom-inschrijvingen-en-diploma-s), [UNL WO downloads](https://www.universiteitenvannederland.nl/downloadbare-gegevens-studenten) |
| DUO | ROD Bekostiging | HBO, WO | Bekostigingsstatus van studenten | [DUO - ROD Bekostigingsstatus](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/bron-controleren/bekostigingsstatus-studenten.jsp) | [CEDA Wisselstroom](https://github.com/cedanl/wisselstroom), [CEDA Wisselstroom demo](https://github.com/cedanl/wisselstroom_demo) | Jaarlijks | |
| DUO | Bekostiging MBO | MBO | Bekostigingsstatus van studenten | [DUO - MBO Bekostigingsstatus](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/bekostiging-mbo.jsp) | | Jaarlijks | |


## Studententevredenheid

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Landelijk Centrum Studiekeuze | NSE | HBO, WO | Tevredenheidsonderzoek studenten | [NSE - Informatie](https://lcsk.nl/nse/resultaten/) | | Jaarlijks | [NSE - Landelijk dashboards](https://lcsk.nl/nse/resultaten/dashboard/) |
| JBO MBO | JOB monitor | MBO | Tevredenheidsonderzoek studenten | [JOB - Rapport](https://www.jobmbo.nl/monitor/) | | Jaarlijks | [JOB - Resultaten](https://www.jobmonitorresultaten.nl/) |

## Alumni en arbeidsmarkt

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Centerdata/IVA | NAE | WO | Alumni enquete | [NAE - Informatie](https://www.nationale-alumni-enquete.nl/algemene-informatie/) | | Om het jaar | [UNL - WO NAE](https://www.universiteitenvannederland.nl/onderwerpen/onderwijs/nationale-alumni-enquete)|
| ROA | HBO-monitor | HBO | Alumni enquete | [HBO monitor - Informatie](https://www.hbomonitor.nl/nl/hogescholen/algemene-informatie) | | Jaarlijks half april | [HBO monitor rapportage](https://www.hbomonitor.nl/nl/resultaten/kansen-op-de-arbeidsmarkt) |
| CINOP | G4-Schoolverlatersonderzoek | MBO | Arbeidsmarkt obv CBS |  | | Jaarlijks |  |

# Institutionele Data

## Financiële gegevens

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | XBRL | HBO | Financiën hogescholen | | | Jaarlijks half oktober | |

## Personeelsgegevens

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | RAHO | HBO | Personeel hogescholen | | | Jaarlijks voorjaar | [VH - HBO Personeel](https://www.vereniginghogescholen.nl/kennisbank/feiten-en-cijfers/artikelen/dashboard-personeel) |
| UNL | WOPI | WO | Geaggregeerde personeelsgegevens | https://www.universiteitenvannederland.nl/downloadbare-gegevens-personeel | | Jaarlijks | [UNL - WO Aantallen](https://www.universiteitenvannederland.nl/onderwerpen/personeel/personeel-in-dienst-van-universiteiten), [UNL - WO Verhouding vast en tijdelijk](https://www.universiteitenvannederland.nl/onderwerpen/personeel/verhouding-vast-en-tijdelijk-personeel), [UNL - WO Herkomst personeel](https://www.universiteitenvannederland.nl/onderwerpen/personeel/herkomst-personeel) |

## Instellingsregistraties

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | RIO | MBO, HBO, WO | Gegevens geaccrediteerde opleidingen | https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/opleidingsgegevens-in-croho/raadplegen-en-downloaden.jsp | | Jaarlijks half oktober | |
| Onderwijsinspectie | Sectorindeling HO | HBO, WO | Sectoren van opleidingen | https://www.onderwijsinspectie.nl/documenten/publicaties/2023/02/14/overzicht-sectorindeling-ho | | Onbekend | |

## Adresgegevens

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | Adressen instellingen | HBO, WO | Adressen | https://www.duo.nl/open_onderwijsdata/hoger-onderwijs/adressen/ | | Jaarlijks | |


