# Landelijke data bronnen
"Interessant, waar komt de onderliggende data vandaan?" of "Hebben we ook zoiets voor het MBO?" horen we regelmatig bij CEDA workshops. Er is veel data beschikbaar voor onderwijstellingen, maar soms ontbreekt het overzicht. 

Daarom nu een overzicht van beschikbare data uit landelijke (en dus uniforme) bronnen voor onderwijsinstellingen. Deze bronnen bieden de mogelijkheid tot benchmarking (soms wordt dit ook expliciet aangeboden). Daarnaast zijn er vaak instellingsbestanden beschikbaar die per instelling er dus hetzelfde uitzien. Dat biedt mogelijkheden voor het gebruik van deze code en logic om deze te bewerken naar informatieproducten zoals voorspelmodellen, statistische diagnoses en dashboards.

Dit is een eerste versie, vul vooral aan! Dit kan door middel van een issue of een email naar corneel.denhartogh@surf.nl.


## Inhoudsopgave
- [Algemene Data Overzichten](#algemene-data-overzichten)
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


# Algemene data overzichten

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Overheid | Meerdere | Allen | Overzicht alle publieke datasets | [Alle Datasets](https://data.overheid.nl/zoek) |  | | |



# Studentgegevens & Onderwijs

## Instroom

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Studielink | Studielink Telbestand | HBO, WO | Voorlopige aanmeldingen | [Toelichting telbestand](https://www.tignl.eu/downloads/studielink/pvl%20telbestand%20studielink.pdf) | [CEDA instroomprognose](https://github.com/cedanl/studentprognose) | Wekelijks | [UNL - WO bachelor](https://www.universiteitenvannederland.nl/aanmeldingen-bacheloropleidingen)|
| MBO Voorzieningen | CAMBO | MBO | Voorlopige aanmeldingen | [Voorziening Centraal aanmelden](https://mbovoorzieningen.nl/voorzieningen/voorziening-centraal-aanmelden/) | | Wekelijks | |

## Inschrijvingen en Studievoortgang

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | ROD 1CijferHO | HBO, WO | Instroom, inschrijvingen en diploma's | [DUO - ROD Controle studentgegevens](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp)| [CEDA 1cijferho](https://github.com/cedanl/1cijferho), [CEDA Python Package](https://github.com/cedanl/eencijfer), [CEDA Power BI dashboard](https://github.com/cedanl/1cho_ins_visualisation_powerbi), [CEDA Tableau dashboard](https://github.com/cedanl/1cho_ins_visualisation_tableau), [CEDA R Preparatie](https://github.com/cedanl/1cho_ins_preparation_r)| Jaarlijks begin februari | [DUO - Geaggregeerde data en voorspellingen](https://www.duo.nl/open_onderwijsdata/hoger-onderwijs/aantal-studenten/), [VH - HBO Inschrijvingen](https://www.vereniginghogescholen.nl/kennisbank/feiten-en-cijfers/artikelen/dashboard-instroom-inschrijvingen-en-diploma-s), [VH - HBO Studiesucces](https://www.vereniginghogescholen.nl/kennisbank/feiten-en-cijfers/artikelen/dashboard-instroom-inschrijvingen-en-diploma-s), [UNL WO downloads](https://www.universiteitenvannederland.nl/downloadbare-gegevens-studenten) |
| DUO | ROD Bekostiging | HBO, WO | Bekostigingsstatus van studenten | [DUO - ROD Bekostigingsstatus](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/bron-controleren/bekostigingsstatus-studenten.jsp) | [CEDA Wisselstroom](https://github.com/cedanl/wisselstroom), [CEDA Wisselstroom demo](https://github.com/cedanl/wisselstroom_demo) | Jaarlijks | |
| DUO | Bekostiging MBO | MBO | Bekostigingsstatus van studenten | [DUO - MBO Bekostigingsstatus](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/bekostiging-mbo.jsp) | | Jaarlijks | |
| DUO | Referentieraming OCW | MBO, HBO, WO | Prognoses verwachte aantal studenten per onderwijsinstelling | [Instellingsprognoses mbo en ho](https://duo.nl/open_onderwijsdata/nieuws/instellingsprognoses-po-vo-mbo-en-ho-beschikbaar.jsp) | | Jaarlijks | [Dashboard MBO prognose](https://informatieproducten.duo.rijkscloud.nl/public/instellingsprognosesmbo/) |
| DUO | DUO Open onderwijsdata | MBO | Dashboards voortijdig schoolverlaten en jongeren in een kwetsbare positie | [Dashboards vsv en jikp](https://informatieproducten.duo.rijkscloud.nl/public/dashboardvsvopen/) | | 2x per jaar | [Dashboards vsv en jikp](https://informatieproducten.duo.rijkscloud.nl/public/dashboardvsvopen/) |
| DUO | SBB/RIO | MBO | Erkende opleidingscodes | [Erkende opleidingscodes - Middelbaar beroepsonderwijs](https://www.duo.nl/open_onderwijsdata/middelbaar-beroepsonderwijs/erkende-opleidingen/erkende-opleidingscode-en-beroep.jsp) | | Jaarlijks | |
| DUO | DUO | MBO | Databestanden macro-doelmatigheid, instroom en switch | [Mijn DUO](https://zakelijk.duo.nl/zakelijk/portaal/dashboard) | | Jaarlijks | |
| MBO Raad | | MBO | Financieel en medewerkers, en studiesucces | [MBObenchmark](https://mbobenchmark.nl/Mosaic/login.aspx?returnUrl=%2Fmosaic%2Fdashboard) | | Jaarlijks | [Benchmark mbo \| MBO Raad](https://www.mboraad.nl/publicaties/benchmark-mbo) |
| CBS | Mbo; studenten, niveau, leerweg, studierichting, regiokenmerken | MBO | Aantal MBO-studenten uitgesplitst naar niveau (1-4), leerweg (BOL/BBL), studierichting en regio. Het meest complete MBO-inschrijvingsoverzicht voor regionale en sectorale analyses. | [CBS Open Data 85353NED](https://opendata.cbs.nl/ODataApi/OData/85353NED) | | Jaarlijks | |
| CBS | Mbo; studenten naar niveau, leerweg, herkomst | MBO | MBO-studenten uitgesplitst naar niveau, leerweg en herkomstland. Biedt lange tijdreeks voor diversiteitsanalyses en beleid rond gelijke kansen in het MBO. | [CBS Open Data 85354NED](https://opendata.cbs.nl/ODataApi/OData/85354NED) | | Jaarlijks | |
| CBS | Mbo; studenten naar niveau, leerweg, studierichting, herkomst | MBO | MBO-studenten gecombineerd naar niveau, leerweg, studierichting én herkomst. Meest gedetailleerde MBO-dataset voor intersectionele analyses van diversiteit en studiekeuze. | [CBS Open Data 85352NED](https://opendata.cbs.nl/ODataApi/OData/85352NED) | | Jaarlijks | |
| CBS | Instromers mbo; bedrijfstakken 1 jaar eerder | MBO | Toont uit welke bedrijfstakken nieuwe MBO-instromers afkomstig zijn. Relevant voor instellingen die willen begrijpen wie zich aanmeldt vanuit de arbeidsmarkt (met name BBL). | [CBS Open Data 85574NED](https://opendata.cbs.nl/ODataApi/OData/85574NED) | | Jaarlijks | |
| CBS | Instromers mbo; maatschappelijke positie 1 jaar eerder, persoonskenmerken | MBO | Maatschappelijke positie van MBO-instromers één jaar voor aanmelding (bijv. werkend, werkzoekend, uit onderwijs). Inzicht in wie de MBO instroomt en vanwaar. | [CBS Open Data 85569NED](https://opendata.cbs.nl/ODataApi/OData/85569NED) | | Jaarlijks | |
| CBS | Mbo door- en uitstroom, achtergrondkenmerken | MBO | Doorstroom en uitstroom van MBO-studenten van het ene naar het volgende studiejaar, uitgesplitst naar herkomst en geslacht. Inzicht in voortijdig schoolverlaten en overstap. | [CBS Open Data 85519NED](https://opendata.cbs.nl/ODataApi/OData/85519NED) | | Jaarlijks | |
| CBS | Gepromoveerden; ervaringen en duur promotietraject | HBO, WO | Ervaringen van gepromoveerden met hun promotietraject, inclusief werkdruk, ongewenst gedrag en tevredenheid. Relevant voor HR-beleid en integriteitsbeleid binnen onderzoeksinstellingen. | [CBS Open Data 86238NED](https://opendata.cbs.nl/ODataApi/OData/86238NED) | | Onregelmatig | |
| CBS | Werkzame gepromoveerden; arbeidskenmerken | HBO, WO | Arbeidsmarktpositie van gepromoveerden: contractvorm, voltijdwerk en loondienst. Inzicht in de arbeidsmarktwaarde van een promotie. | [CBS Open Data 86240NED](https://opendata.cbs.nl/ODataApi/OData/86240NED) | | Onregelmatig | |
| CBS | Studeren in het buitenland; studiepuntmobiliteit hbo en wo | HBO, WO | Aandeel HBO- en WO-studenten dat studiepunten in het buitenland haalt. Relevant voor internationaliseringsbeleid en het monitoren van mobiliteitsambities. | [CBS Open Data 85907NED](https://opendata.cbs.nl/ODataApi/OData/85907NED) | | Jaarlijks | |
| CBS | Wetenschappelijk onderwijs; promoties, studierichting | WO | Aantal promoties per studierichting en geslacht in het wetenschappelijk onderwijs. Inzicht in onderzoeksoutput en diversiteit in de academische pipeline. | [CBS Open Data 83966NED](https://opendata.cbs.nl/ODataApi/OData/83966NED) | | Jaarlijks | |
| CBS | Hoger onderwijs; eerste- en ouderejaarsstudenten, studierichting, herkomst | HBO, WO | Ingeschrevenen in het HO uitgesplitst naar eerstejaars/ouderejaars, studierichting en herkomst. Geschikt voor instroomanalyses en diversiteitsmonitoring per richting. | [CBS Open Data 85421NED](https://opendata.cbs.nl/ODataApi/OData/85421NED) | | Jaarlijks | |
| CBS | Hoger onderwijs; ingeschrevenen, onderwijssoort, opleidingsfase en -vorm | HBO, WO | Totaal ingeschrevenen in HBO en WO per onderwijssoort, opleidingsfase (bachelor/master) en opleidingsvorm (voltijd/deeltijd/duaal). Standaard benchmarkset voor HO-instellingen. | [CBS Open Data 85423NED](https://opendata.cbs.nl/ODataApi/OData/85423NED) | | Jaarlijks | |
| CBS | Hoger onderwijs; eerstejaarsstudenten, vooropleiding en opleidingsfase | HBO, WO | Eerstejaars in het HO uitgesplitst naar vooropleiding (MBO, HAVO, VWO) en opleidingsfase. Inzicht in doorstroom vanuit het voorgaande onderwijs naar HO. | [CBS Open Data 85422NED](https://opendata.cbs.nl/ODataApi/OData/85422NED) | | Jaarlijks | |
| CBS | Hoger onderwijs; internationale studenten, nationaliteit | HBO, WO | Aantal internationale studenten in het HO uitgesplitst naar nationaliteit en geslacht. Lange tijdreeks voor internationaliseringsbeleid en monitoring van herkomstlanden. | [CBS Open Data 85124NED](https://opendata.cbs.nl/ODataApi/OData/85124NED) | | Jaarlijks | |
| CBS | Hoger onderwijs; internationale studenten, onderwijskenmerken | HBO, WO | Internationale studenten in HO uitgesplitst naar verblijfsjaar, studierichting en onderwijssoort. Relevant voor beleid rond instroom, retentie en spreiding van internationals. | [CBS Open Data 85125NED](https://opendata.cbs.nl/ODataApi/OData/85125NED) | | Jaarlijks | |
| CBS | Hbo-cohorten; eerste hbo-diploma, studierichting | HBO, WO | Cohortdata van HBO-starters die bijhoudt hoeveel studenten op verschillende peilmomenten hun eerste HBO-diploma hebben behaald. Standaardset voor diplomarendementsanalyse. | [CBS Open Data 83286NED](https://opendata.cbs.nl/ODataApi/OData/83286NED) | | Jaarlijks | |
| CBS | Ho-cohorten; behaalde hbo- en wo-diploma's | HBO, WO | Cohortdata van HO-starters die bijhoudt hoeveel studenten een HO-diploma behalen op verschillende peilmomenten. Vergelijkt HBO en WO rendement. | [CBS Open Data 83282NED](https://opendata.cbs.nl/ODataApi/OData/83282NED) | | Jaarlijks | |
| CBS | Wo-cohorten; eerste wo-diploma, studierichting | WO | Cohortdata van WO-starters die bijhoudt hoeveel studenten hun eerste WO-diploma behalen per studierichting. Geschikt voor rendements- en doorstroomanalyses per vakgebied. | [CBS Open Data 83285NED](https://opendata.cbs.nl/ODataApi/OData/83285NED) | | Jaarlijks | |
| CBS | Wo-cohorten; hoogst behaalde wo-diploma, vooropleiding | WO | Welk WO-diploma studenten uiteindelijk behalen, uitgesplitst naar vooropleiding en studiefase bij instroom. Inzicht in doorstroom van bachelor naar master. | [CBS Open Data 83305NED](https://opendata.cbs.nl/ODataApi/OData/83305NED) | | Jaarlijks | |

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
| CBS | Mbo; gediplomeerden, niveau, leerweg, studierichting, regiokenmerken | MBO | Aantal gediplomeerden in het MBO per niveau, leerweg, studierichting en regio. Kernset voor diplomarendementsanalyses en regionale arbeidsmarktaansluiting. | [CBS Open Data 85356NED](https://opendata.cbs.nl/ODataApi/OData/85356NED) | | Jaarlijks | |
| CBS | Mbo; gediplomeerden, niveau, leerweg, studierichting, herkomst | MBO | MBO-gediplomeerden uitgesplitst naar niveau, leerweg, studierichting en herkomst. Inzicht in diplomarendement per herkomstgroep en kansen op diplomering. | [CBS Open Data 85355NED](https://opendata.cbs.nl/ODataApi/OData/85355NED) | | Jaarlijks | |
| CBS | Mbo; gediplomeerden, niveau, leerweg, herkomst | MBO | Lange tijdreeks van MBO-gediplomeerden naar niveau, leerweg en herkomst. Geschikt voor trendanalyses van diplomarendement per herkomstgroep over meer dan tien jaar. | [CBS Open Data 85357NED](https://opendata.cbs.nl/ODataApi/OData/85357NED) | | Jaarlijks | |
| CBS | Ho; gediplomeerden, soort diploma, opleidingsvorm | HBO, WO | Gediplomeerden in het hoger onderwijs naar soort diploma (bachelor/master/ad) en opleidingsvorm (voltijd/deeltijd/duaal). Kernset voor diplomarendementsanalyse in HO. | [CBS Open Data 85424NED](https://opendata.cbs.nl/ODataApi/OData/85424NED) | | Jaarlijks | |
| CBS | Ho; gediplomeerden, soort diploma, studierichting, herkomst | HBO, WO | HO-gediplomeerden uitgesplitst naar studierichting, diplomasoort en herkomst. Inzicht in studiesucces per richting en herkomstgroep. | [CBS Open Data 85425NED](https://opendata.cbs.nl/ODataApi/OData/85425NED) | | Jaarlijks | |
| CBS | Uitstromers mbo; arbeidskenmerken na verlaten onderwijs | MBO | Arbeidskenmerken van MBO-uitstromers (met en zonder diploma) na verlaten van de opleiding. Kernset voor arbeidsmarktaansluiting en VSV-beleidsevaluatie. | [CBS Open Data 85698NED](https://opendata.cbs.nl/ODataApi/OData/85698NED) | | Jaarlijks | |
| CBS | Uitstromers mbo; arbeidsmarktpositie na verlaten onderwijs | MBO | Arbeidsmarktpositie (werkend/werkzoekend/inactief) van MBO-uitstromers na verlaten onderwijs. Inzicht in succesvolle overgang naar de arbeidsmarkt. | [CBS Open Data 85696NED](https://opendata.cbs.nl/ODataApi/OData/85696NED) | | Jaarlijks | |
| CBS | Uitstromers mbo; uitkering na verlaten onderwijs | MBO | Uitkeringsontvangers onder MBO-uitstromers na verlaten onderwijs, uitgesplitst naar leeftijd en diplomastatus. Relevant voor beleid rond voortijdig schoolverlaten en sociale zekerheid. | [CBS Open Data 85700NED](https://opendata.cbs.nl/ODataApi/OData/85700NED) | | Jaarlijks | |
| CBS | Uitstromers mbo met werk; bedrijfstak na verlaten onderwijs | MBO | In welke bedrijfstakken MBO-uitstromers terechtkomen na verlaten van de opleiding. Inzicht in de match tussen MBO-opleidingen en arbeidsmarkt per sector. | [CBS Open Data 85699NED](https://opendata.cbs.nl/ODataApi/OData/85699NED) | | Jaarlijks | |
| CBS | Uitstromers mbo werkzaam als werknemers; uurloon na verlaten onderwijs | MBO | Uurloon van werkzame MBO-uitstromers na verlaten onderwijs, uitgesplitst naar studierichting en bedrijfstak. Inzicht in de financiële arbeidsmarktwaarde van MBO-diploma's. | [CBS Open Data 83832NED](https://opendata.cbs.nl/ODataApi/OData/83832NED) | | Jaarlijks | |
| CBS | Uitstromers ho; arbeidskenmerken na verlaten onderwijs | HBO, WO | Arbeidskenmerken van HO-uitstromers na verlaten onderwijs, uitgesplitst naar geslacht en diplomastatus. Brede set voor arbeidsmarktaansluitingsanalyses in het hoger onderwijs. | [CBS Open Data 85777NED](https://opendata.cbs.nl/ODataApi/OData/85777NED) | | Jaarlijks | |
| CBS | Uitstromers ho; arbeidsmarktpositie na verlaten onderwijs | HBO, WO | Arbeidsmarktpositie van HO-uitstromers uitgesplitst naar geslacht, herkomst en diplomastatus. Inzicht in kansen op werk na HO per doelgroep. | [CBS Open Data 85776NED](https://opendata.cbs.nl/ODataApi/OData/85776NED) | | Jaarlijks | |
| CBS | Uitstromers ho met werk; bedrijfstak na verlaten onderwijs | HBO, WO | In welke bedrijfstakken werkzame HO-uitstromers terechtkomen, uitgesplitst naar studierichting. Inzicht in aansluiting tussen HO-opleidingen en arbeidsmarkt per sector. | [CBS Open Data 85778NED](https://opendata.cbs.nl/ODataApi/OData/85778NED) | | Jaarlijks | |
| CBS | Uitstromers ho; uitkering na verlaten onderwijs | HBO, WO | Uitkeringsontvangers onder HO-uitstromers na verlaten onderwijs. Inzicht in kwetsbaarheid op de arbeidsmarkt, ook voor internationale studenten. | [CBS Open Data 85779NED](https://opendata.cbs.nl/ODataApi/OData/85779NED) | | Jaarlijks | |
| CBS | Uitstromers ho werkzaam als werknemers; uurloon na verlaten onderwijs | HBO, WO | Uurloon van werkzame HO-uitstromers uitgesplitst naar studierichting en bedrijfstak. Inzicht in de financiële arbeidsmarktwaarde van HO-diploma's per richting. | [CBS Open Data 83815NED](https://opendata.cbs.nl/ODataApi/OData/83815NED) | | Jaarlijks | |

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
| Onderwijsinspectie | Sectorindeling HO | HBO, WO | Sectoren van opleidingen | https://www.onderwijsinspectie.nl/documenten/2023/02/14/overzicht-sectorindeling-ho | | Onbekend | |

## Adresgegevens

| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | CEDA repository | Frequentie | Publieke informatieproducten |
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| DUO | Adressen instellingen | HBO, WO | Adressen | https://www.duo.nl/open_onderwijsdata/hoger-onderwijs/adressen/ | | Jaarlijks | |




# Externe software bronnen met Vusaverse package

Het team Education Analytics op de Vrije Universiteit Amsterdam heeft een collectie (de VusaVerse) aan R packages ontwikkeld, waaronder voor API's.


| Leverancier | Bron | Onderwijstype | Doel | Documentatie URL | VusaVerse repository | Frequentie | Publieke informatieproducten | 
|-------------|------|---------------|------|-----------------|-----------------|-------------|----------------------------|
| Instructure | Canvas LMS | MBO, HBO, WO | Leer management systeem | [API documentatie](https://developerdocs.instructure.com/services/canvas) | [R package vvcanvas](https://github.com/vusaverse/vvcanvas) | Real-Time |  |
| Semestry | Termtime | MBO, HBO, WO | Roostering |   | [R package vvtermtime](https://github.com/vusaverse/vvtermtime) | Real-Time | nvt |

