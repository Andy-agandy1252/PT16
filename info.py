from tkinter import *
#---------1frame photos-----
miestusaraso_foto = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\miestai.png')
paminklu_foto = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\paminklai.png')
muzieju_foto = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\muziejai.png')
kulturos_foto = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\kultura.png')

#--------2frame info----
photo1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\miestai\\1vln.png')
photo2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\2kau.png')
photo3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\3kla.png')
photo4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\4sau.png')
photo5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\5pan.png')
photo6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\6aly.png')
photo7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\7mar.png')
photo8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\8maz.png')
photo9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\9jon.png')
photo10 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\10ute.png')
photo11 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\11ked.png')
photo12 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\12tau.png')
photo13 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\13tel.png')
photo14 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\miestai\\14ukm.png')
city_list = {"Ukmergė": [photo14, "Ukmergė – miestas Aukštaitijoje, Vilniaus apskrityje (76 km\n"
                                       " į šiaurės vakarus nuo Vilniaus ir 71 km į šiaurės rytus nuo Kauno),\n"
                                       "Ukmergės rajono savivaldybės centras."],
                  "Telšiai": [photo13, "Telšiai – miestas šiaurės vakarų Lietuvoje, Žemaičių aukštumoje,\n"
                                       " prie Masčio ežero ir Durbinio upelio, 69 km į vakarus nuo Šiaulių.\n"
                                       " Telšių apskrities ir Telšių rajono savivaldybės centras, Žemaitijos\n"
                                       " sostinė. Miesto centrinė dalis yra urbanistikos paminklas."],
                  "Tauragė": [photo12, "Tauragė – miestas vakarų Lietuvoje, Žemaitijoje, Karšuvos \n"
                                       "žemumoje, kairiajame Jūros upės krante. Apskrities ir Tauragės\n"
                                       "rajono savivaldybė centras, Tauragės miesto seniūnija,\n"
                                       "apylinkių seniūnijos centras."],
                  "Kėdainiai": [photo11, "Kėdainiai – miestas vidurio Lietuvoje, Kauno apskrityje,\n"
                                         "abipus Nevėžio, už 51 km į šiaurę nuo Kauno. Kėdainių rajono\n"
                                         "savivaldybės ir seniūnijos centras."],
                  "Utena": [photo10, "Utena – miestas šiaurės rytų Lietuvoje, Utenos aukštumoje\n"
                                     "(Aukštaičių aukštumos dalis), 92 km į šiaurę nuo Vilniaus.\n"
                                     "Utenos apskrities ir Utenos rajono savivaldybės centras,\n"
                                     "Utenos miesto seniūnija, apylinkių seniūnijos centras."],
                  "Jonava": [photo9, "Jonava – devintas pagal gyventojų skaičių Lietuvos miestas,\n"
                                     "esantis Kauno apskrityje, prie Neries, žemiau Šventosios\n"
                                     "žiočių, 30 km į šiaurės rytus nuo Kauno. Jonavos rajono centras."],
                  "Mažeikiai": [photo8, "Mažeikiai – miestas šiaurės vakarų Lietuvoje, Žemaitijoje,\n"
                                        "Telšių apskrityje, 46 km į šiaurę nuo Telšių. Mažeikių\n"
                                        "rajono savivaldybės centras, Mažeikių seniūnija, yra\n"
                                        "apylinkės seniūnijos ir Reivyčių seniūnijos\n"
                                        "administracinis centras."],
                  "Marijampolė": [photo7, "Marijampolė – miestas pietvakarių Lietuvoje,\n"
                                          "56 km į pietvakarius nuo Kauno. Neoficiali\n"
                                          "Suvalkijos (Sūduvos) sostinė, taip pat Marijampolės\n"
                                          "apskrities, Marijampolės savivaldybės ir\n"
                                          "kaimiškosios seniūnijos centras."],
                  "Alytus": [photo6, "Alytus – didžiausias Pietų Lietuvos miestas,\n"
                                     "įsikūręs prie Nemuno, 65 km į pietus nuo Kauno\n"
                                     "ir 108 km į pietvakarius nuo Vilniaus. Apskrities,\n"
                                     "Alytaus rajono savivaldybės centras, Alytaus miesto\n"
                                     "savivaldybė, Alytaus seniūnijos ir katalikų dekanato centras."],
                  "Panevėžys": [photo5, "Panevėžys – miestas šiaurės Lietuvoje, Vidurio\n"
                                        "Lietuvos žemumoje, abipus Nevėžio, 136 km į\n"
                                        "šiaurės vakarus nuo Vilniaus. Vienas didžiųjų\n"
                                        "Lietuvos miestų (penktasis pagal dydį). "],
                  "Šiauliai": [photo4, "Šiauliai – miestas šiaurės Lietuvoje, ketvirtasis\n"
                                       "pagal gyventojų skaičių šalies miestas; Šiaulių\n"
                                       "apskrities ir Šiaulių rajono savivaldybės\n"
                                       "administracinis centras. Šiauliai yra svarbus\n"
                                       "ekonominis ir susisiekimo centras, jame veikia\n"
                                       "Vilniaus universiteto Šiaulių akademija, miestas\n"
                                       "yra katalikiškos vyskupystės centras."],
                  "Klaipėda": [photo3, "Klaipėda – trečias pagal gyventojų skaičių\n"
                                       "ir plotą Lietuvos miestas, įsikūręs Vakarų\n"
                                       "Lietuvoje, Pajūrio žemumoje, ties Kuršių marių\n"
                                       "ir Baltijos jūros santakos vieta. Miestas taip\n"
                                       "pat yra Klaipėdos apskrities administracinis\n"
                                       "centras. Svarbiausias Vakarų Lietuvos pramonės\n"
                                       "centras, kelių, geležinkelių ir jūrų transporto mazgas."],
                  "Kaunas": [photo2, "Kaunas – antrasis pagal dydį Lietuvos miestas\n"
                                     "šalies centrinėje dalyje, Nemuno ir Neries\n"
                                     "santakoje. Svarbus pramonės, transporto, mokslo\n"
                                     "ir kultūros centras, Laikinoji sostinė. Kauno\n"
                                     "miesto savivaldybės, Kauno rajono savivaldybės,\n"
                                     "arkivyskupijos centras. Gyventojų skaičius – 298,8 tūkst."],
                  "Vilnius": [photo1, "Vilnius – Lietuvos Respublikos sostinė, \n"
                                      "Vilniaus apskrities, Vilniaus rajono savivaldybės \n"
                                      "ir Vilniaus miesto savivaldybės centras. 2022 m.\n"
                                      " pradžioje mieste gyveno 592 389 gyventojai."]}
vlnvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\1vlnvieta.png')
vlnvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\2vlnvieta.png')
vlnvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\3vlnvieta.png')
vlnvieta4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\4vlnvieta.png')
vlnvieta5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\5vlnvieta.png')
vlnvieta6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\6vlnvieta.png')
vlnvieta7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\7vlnvieta.png')
vlnvieta8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\8vlnvieta.png')
vlnvieta9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\9vlnvieta.png')
vlnvieta10 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\10vlnvieta.png')
vlnvieta11 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\11vlnvieta.png')
vlnvieta12 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\12vlnvieta.png')
vlnvieta13 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\13vlnvieta.png')
vlnvieta14 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\14vlnvieta.png')
vlnvieta15 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\vln\\15vlnvieta.png')
vilniaus_paminklai = {"Vilnius - Paminklas LDK didžiajam kunigaikščiui Gediminui": [vlnvieta1, "Gediminas yra Trakų ir Vilniaus miesto įkūrėjas ir vienas\n"
                                                                                     " garsiausių senosios Lietuvos valdovų, gyvenęs 1275–1341 metais,\n"
                                                                                     " Lietuvos Didžiąją Kunigaikštystę valdęs 25-erius metus."],
                      "Vilnius - Paminklas Frankui Zappai": [vlnvieta2, "Paminklo istorija išties komiška. Po vizito JAV menininkas Saulius Paukštys\n"
                                                              " visiems papasakojo istoriją, kaip susidraugavo su pačiu muzikantu. Tai tebuvo\n"
                                                              " pramanai, tačiau Frankas Zappa patraukė kitų Lietuvos menininkų dėmesį ir tapo\n"
                                                              " laisvės simboliu. "],
                      "Vilnius - Miesto vartų sargybinio skulptūra": [vlnvieta3, "Viduramžiais Vilnių juosė 1503 m. miestiečių pradėta statyti siena, skirta\n"
                                                                       " apsiginti nuo gresiančių totorių antpuolių. Vieneri iš devynerių miesto\n"
                                                                       " vartų, kuriuose nuolat budėjo sargybiniai, buvo Trakų ir Pylimo gatvių\n"
                                                                       " sankirtoje. Taigi šios skulptūros vieta nėra neatsitiktinė. "],
                      "Vilnius - Žemaitės skulptūra": [vlnvieta4, "Per savo gyvenimą Žemaitė parašė 354 kūrinius: apsakymus, apysakas,\n"
                                                        " apybraižas, vaizdelius, keliolika pjesių, pasakojimą apie savo vaikystę,\n"
                                                        " publicistinių straipsnių, korespondencijų. Žymiausi jos kūriniai yra\n"
                                                        " „Marti“, „Topylis“, „Petras Kurmelis“, „Sučiuptas velnias“ ir „Sutkai“. "],
                      "Vilnius - Karaliaus Mindaugo paminklas": [vlnvieta5, "Paminklą vieninteliam Lietuvos karaliui Mindaugui galima pamatyti priešais\n"
                                                                  " Lietuvos nacionalinį muziejų. Ten jis pastatytas 2003 m. minint Mindaugo\n"
                                                                  " karūnavimo 750 metų jubiliejų."]}
vilniaus_muziejai = {"Vilniaus miesto muziejus": [vlnvieta6, "Laisvalaikio metu atostogaudami Vilniaus rajone esančioje kaimo turizmo\n"
                                                 " sodyboje užsukite į sostinę. Atvykę nepraleiskite progos ir užkopkite į\n"
                                                 " Plikąjį kalną, kur jus didžiai pasitiks Trijų Kryžių paminklas."],
                    "Vilnius - Lietuvos meno pažinimo centras „Tartle“": [vlnvieta7, "Savo pavadinimą jį įgavo XIX a. pr. žinomo rašytojo Adomo Mickevičiaus\n"
                                                    " garbei. Apie tai, kad poetas anksčiau čia gyveno liudija trys lentos\n"
                                                    " ant namo sienų lietuvių, lenkų bei rusų kalbomis."],
                    "Vilnius - Parodų erdvė Istorijų namai": [vlnvieta8, "Iki šių dienų išlikęs tvirtovės vakarinis bokštas pavadintas Gedimino\n"
                                                    " vardu. Trijuose aukštuose įrengtas muziejus, o viršuje – apžvalgos\n"
                                                    " aikštelė, iš kurios atsiveria plati miesto panorama."],
                    "Vilnius - MO muziejus": [vlnvieta9, "XVI a. stovėjęs gynybinis bokštas įgavo didingą prasmę ir\n"
                                                               " tapo katedros varpine. Tačiau dabartinę išvaizdą įgijo tik\n"
                                                               " XIX a. pradžioje. Jos aukštis siekia 52 m, o su\n"
                                                               " kryžiumi net 57 metrus."],
                    "Vilnius - Senasis arsenalas": [vlnvieta10, "Atvykę pamatysite modernią edukacinę erdvę, kurioje detaliai\n"
                                                                 " pristatoma kaip veikia valstybė. Taip pat demonstruojama\n"
                                                                 " informacija kaip demokratinės valstybės kūrime ir valdyme\n"
                                                                 " dalyvauja jos piliečiai."]}
vilniaus_kultura = {"Vilnius - Trys Kryžiai": [vlnvieta11, "Laisvalaikio metu atostogaudami Vilniaus rajone esančioje kaimo turizmo\n"
                                                 " sodyboje užsukite į sostinę. Atvykę nepraleiskite progos ir užkopkite į\n"
                                                 " Plikąjį kalną, kur jus didžiai pasitiks Trijų Kryžių paminklas."],
                    "Vilnius - Literatų gatvė": [vlnvieta12, "Savo pavadinimą jį įgavo XIX a. pr. žinomo rašytojo Adomo Mickevičiaus\n"
                                                     " garbei. Apie tai, kad poetas anksčiau čia gyveno liudija trys lentos\n"
                                                     " ant namo sienų lietuvių, lenkų bei rusų kalbomis."],
                    "Vilnius - Gedimino pilis": [vlnvieta13, "Iki šių dienų išlikęs tvirtovės vakarinis bokštas pavadintas Gedimino vardu.\n"
                                                     " Trijuose aukštuose įrengtas muziejus, o viršuje – apžvalgos aikštelė, iš\n"
                                                     " kurios atsiveria plati miesto panorama."],
                    "Vilniaus katedros varpinė": [vlnvieta14, "XVI a. stovėjęs gynybinis bokštas įgavo didingą prasmę ir tapo katedros varpine.\n"
                                                                " Tačiau dabartinę išvaizdą įgijo tik XIX a. pradžioje. Jos aukštis siekia 52 m,\n"
                                                                " o su kryžiumi net 57 metrus."],
                    "Vilnius - Valstybės pažinimo centras": [vlnvieta15, "Atvykę pamatysite modernią edukacinę erdvę, kurioje detaliai pristatoma kaip\n"
                                                                 " veikia valstybė. Taip pat demonstruojama informacija kaip demokratinės\n"
                                                                 " valstybės kūrime ir valdyme dalyvauja jos piliečiai."]}
kauvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\1kauvieta.png')
kauvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\2kauvieta.png')
kauvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\3kauvieta.png')
kauvieta4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\4kauvieta.png')
kauvieta5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\5kauvieta.png')
kauvieta6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\6kauvieta.png')
kauvieta7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\7kauvieta.png')
kauvieta8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\8kauvieta.png')
kauvieta9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\9kauvieta.png')
kauvieta10 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\10kauvieta.png')
kauvieta11 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\11kauvieta.png')
kauvieta12 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\12kauvieta.png')
kauvieta13 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\13kauvieta.png')
kauvieta14 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\14kauvieta.png')
kauvieta15 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kau\\15kauvieta.png')
kauno_paminklai = {"Kaunas - Lietuvos partizanų stovyklos vieta": [kauvieta1, "Šioje žeminėje 1944-1945 m. slapstėsi devyniolika partizanų. Tarp jų - ir \n"
                                                                     "sužeistas Lietuvos laisvės kovų sąjudžio štabo viršininkas buvęs partizanas\n"
                                                                     " Vytautas Balsys slapyvardžiu Uosis. Sovietmečiu žuvusiems atminti prie\n"
                                                                     " žeminės V. Balsys pastatė kryžių."],
                   "Kaunas - Dievų ir deivių slėnis": [kauvieta2, "Kulautuvos pėsčiųjų sveikatingumo take įkurtas dievų ir deivių slėnis, vietinių\n"
                                                         " dažnai vadinamas tiesiog skulptūrų parku. Čia Lietuvos skulptorių vasaros\n"
                                                         " pleneruose sukurtos iš ąžuolo skulptūros, įprasminančios svarbiausius pagoniškus\n"
                                                         " dievus ir deives – Perkūną, Patrimpą, Pykuolį, Žemyną, Gabiją, Kovą, Laimą ir kt."],
                   "Kaunas - Žalgirio mūšio memorialinis parkas": [kauvieta3, "1990 m., minint Žalgirio mūšio 580-ąsias metines, ties Cinkiškių kaimu, prie\n"
                                                                     " autostrados Kaunas – Klaipėda, įkurtas Žalgirio mūšio memorialinis parkas\n"
                                                                     " Kryžiuočių ordino sutriuškinimui atminti."],
                   "Kaunas - Monumentas nužudytiems žydams atminti": [kauvieta4, "Kauno rajono savivaldybės ir JAV gyvenančių litvakų pastangomis šalia senųjų\n"
                                                                        " Vandžiogalos kapinių pastatytas memorialas skirtas 1941 m. liepos mėn. 8 d.\n"
                                                                        " nužudytiems žydų tautybės žmonėms atminti. Monumentas įamžina 37 aukų, tarp\n"
                                                                        " kurių 34 žydai, 2 lietuviai, 1 rusas, atminimą."],
                   "Kaunas - Lietuvos Nepriklausomybės dešimtmečio paminklas": [kauvieta5, "Nepriklausomybės paminklas Lapėse buvo pastatytas 1928 metais, minint\n"
                                                                                  " valstybingumo atkūrimo dešimtmetį. Lapių klebonas Juozas Jasas parašė\n"
                                                                                  " raštą, įdėjo jį į butelį ir įmūrijo į pamatą; prie paminklo buvo\n"
                                                                                  " pasodinti du ąžuoliukai, o trečias – atsarginis – prie klebonijos."]}
kauno_muziejai = {"Kaunas - Tautines muzikos skyrius": [kauvieta6, "Modernioje ekspozicijoje galima ne tik apžiūrėti unikalius senuosius lietuviškus\n"
                                                          " muzikos instrumentus, bet ir išgirsti jų muzikos, pagroti, sudainuoti sutartinių\n"
                                                          " karaokę ir net peržiūrėti postfolkloro atlikėjų vaizdo klipus. "],
                  "Kaunas - Kiemo galerija": [kauvieta7, "Prieš daugiau nei dešimtmetį į namą šiame kieme atsikraustęs menininkas\n"
                                                " Vytenis Jakas pastebėjo, kad kaimynai susvetimėję ir pamiršę bendrą\n"
                                                " kiemo praeitį. "],
                  "Kaunas - Sakralinis muziejus": [kauvieta8, "Pietinė oficina pastatyta XVII – XVIII a. sandūroje. XVIII a. tebevykstant vienuolyno\n"
                                                     " statyboms ji tarnavo kaip gyvenamasis namas su virtuve, amžiaus pabaigoje\n"
                                                     " kamalduliai pradėjo naudoti pastatą kalvystės darbams."],
                  "Kaunas - Paveikslu galerija": [kauvieta9, "Galerija atidaryta 1979 m. (architektai Liucija Gedgaudienė, Jonas Navakas).\n"
                                                    " Ji buvo skirta vieno žymiausių kolekcininkų Mykolo Žilinsko Kauno miestui\n"
                                                    " dovanotai kolekcijai."],
                  "Kaunas - Art deko muziejus": [kauvieta10, "Viešnagė į autentiškus namus – tai lyg kelionė laiku, papildoma pikantiškomis,\n"
                                                    " niekur dar neskaitytomis istorijomis."]}

kauno_kultura = {"Kaunas - Raudondvario dvaras": [kauvieta11, "Kauno rajone įsikūręs, dar XVI a. pab. menantis Raudondvario dvaro\n"
                                                     " architektūrinis ansamblis – vienas įspūdingiausių atgimusių renesanso\n"
                                                     " architektūros paminklų Lietuvoje."],
                 "Kaunas - Pažaislio kamaldulių vienuolynas": [kauvieta12, "Pažaislio bažnyčios ir vienuolyno ansamblis pastatytas 17- 18 a. LDK\n"
                                                                  "  Didžiajam kancleriui Kristupui Zigmuntui Pacui remiant. "],
                 "Kauno pilis": [kauvieta13, "Kauno pilis seniausias miesto istorinis objektas. Ji pastatyta 14 a. antroje pusėje.\n"
                                             " Pirmą kartą Kauno pilis istoriniuose šaltiniuose paminėta 1361 m. Ji nuolat buvo\n"
                                             " puldinėjama kryžiuočių, tad atliko gynybinę funkciją. "],
                 "Kauno tvirtovės VII fortas": [kauvieta14, "Kauno tvirtovės VII fortas - naujosios kartos muziejus. Fortas savo duris\n"
                                                            " lankytojams atvėrė 2011 metais."],
                 "Kaunas - Svetingumo kompleksas MONTE PACIS": [kauvieta15, "Svetingumo kompleksas MONTE PACIS įsikūręs išskirtinėje Lietuvos vietoje \n"
                                                                   "- Pažaislio vienuolyno ansamblyje, pastatyme beveik prieš 350 metų. XVII a. "]}
klavieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\1klavieta.png')
klavieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\2klavieta.png')
klavieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\3klavieta.png')
klavieta4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\4klavieta.png')
klavieta5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\5klavieta.png')
klavieta6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\6klavieta.png')
klavieta7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\7klavieta.png')
klavieta8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\8klavieta.png')
klavieta9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\9klavieta.png')
klavieta10 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\10klavieta.png')
klavieta11 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\11klavieta.png')
klavieta12 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\12klavieta.png')
klavieta13 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\13klavieta.png')
klavieta14 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\14klavieta.png')
klavieta15 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\kla\\15klavieta.png')
klaipedos_paminklai = {"Klaipeda - Ferdinando aikštė": [klavieta1, "Archeologinių kasinėjimų metu aikštės vietoje aptikta vėlyvojo neolito senovės\n"
                                                        " gyvenvietė (apie 2500 m. pr. Kr.), virvelinės keramikos,\n"
                                                        " titnago dirbinių, gintaro."],
                      "Klaipeda - Prieglauda seniems amatininkams": [klavieta2, "Buvusi prieglauda seniems amatininkams stovi S. Nėries gatvės pradžioje.\n"
                                                                     " Dabartinė S. Nėries gatvė pavadinimą gavo sovietmečiu, o iki Antrojo\n"
                                                                     " pasaulinio karo ji buvo vadinama Stoties gatve (vok. Bahnhofstraße). "],
                      "Klaipeda - Agluonėnų kapinės": [klavieta3, "Šios kapinės atspindi unikalią Klaipėdos krašto konfesinę ir čia gyvenusių\n"
                                                       " žmonių dvasinę savastį. Kapinėse dominuoja mediniai ir metaliniai kryžiai."],
                      "Klaipeda - Lietuvininkų parkas": [klavieta4, "Lietuvininkų parko sodinimo iniciatorius 1990 m. − Mažosios Lietuvos\n"
                                                         " enciklopedijos rėmėjas, Lietuvininkų bendrijos „Mažoji Lietuva“ vienas\n"
                                                         " steigėjų, pirmasis jos pirmininkas (1989–1999) Viktoras Petraitis."],
                      "Klaipeda - Vaclovo Into sodyba": [klavieta5, "1957 m. Mosėdyje buvo įsteigta ligoninė, kurios vedėju buvo paskirtas jaunas\n"
                                                         " gydytojas Vaclovas Intas. Mosėdis tuo metu buvo pilkas, medinėmis trobelėmis\n"
                                                         " apstatytas miestelis. Ligoninę supo senas, 1,5 ha sodas."]}
klaipedos_muziejai = {"Klaipeda - Gintaro muziejus „AMBER QUEEN“": [klavieta6, "„Amber Queen“ muziejus įsikūręs pačioje Klaipėdos senamiesčio širdyje.\n"
                                                                    " Čia jūsų laukia susitikimas su nepakartojamais šiuolaikiniais ir\n"
                                                                    " senoviniais gintaro kūriniais! "],
                      "Klaipeda - Lietuvos jūrų muziejus ir delfinariumas": [klavieta7, "Muziejus įsikūręs šiauriausiame Kuršių nerijos taške – Kopgalyje, kur baigiasi\n"
                                                                             " 98 kilometrų ilgio Kuršių nerijos pusiasalis ir atsiveria\n"
                                                                             " Klaipėdos uosto vartai."],
                      "Klaipeda - Rezistencijos ir tremties ekspozicija": [klavieta8, "Šio pastato kamerose 1945-1954 m. kalėjo 8 268 žmonės. Siekiant fiziškai ir\n"
                                                                           " psichologiškai palaužti suimtuosius, jie slapta buvo tardomi ir kankinami,\n"
                                                                           " nemažai žmonių – nužudyta."],
                      "Klaipeda - Pilies muziejus": [klavieta9, "Autentiškose XVI-XVIII a. poternose susipažinsite su pilies ir miesto raida. \n"
                                                     "Pamatysite piliavietėje ir senamiestyje rastus ir eksponuojamus archeologinius\n"
                                                     " radinius, dokumentus, Klaipėdos miesto antspaudus,\n"
                                                     " rekonstruotus XVII a. kostiumus."],
                      "Klaipeda - Kalvystės muziejus": [klavieta10, "iejus Klaipėdoje įsikūręs rekonstruotame pastate, priklausiusiam žinomam\n"
                                                         " Klaipėdos šaltkalviui Fr. Grimui (Fr. Grimm). Kiemelyje Jus pasitiks\n"
                                                         " Klaipėdos krašte kaldinti metaliniai kryžiai."]}
klaipedos_kultura = {"Klaipeda - Skulptūrų maršrutas": [klavieta11, "Ypatingas maršrutas, leisiantis dar geriau pažinti ypatinga pajūrio atmosfera\n"
                                                         " alsuojantį Klaipėdos miestą."],
                      "Klaipeda - Skulptūrų parkas": [klavieta12, "Tai moderniosios lietuvių skulptūros galeriją po atviru dangumi, įkurta dar 1977 m.\n"
                                                       " Šiandien 12 ha ploto parke eksponuojama 116 skulptūrų, kurias sukūrė 67 Lietuvos\n"
                                                       " menininkai-skulptoriai. "],
                      "Klaipeda - Senieji sandėliai": [klavieta13, "Danės krantinė XVI a. jau buvo užstatyta sandėliais, tą rodo ir seniausias miesto\n"
                                                        " vaizdas, ženklinamas 1535 m. data. XVII a. pradžioje Žvejų gatvėje stovėjo\n"
                                                        " mūriniai gyvenamieji namai ir sandėliai."],
                      "Klaipeda - Mokomasis burlaivis – Meridianas": [klavieta14, "Mokomasis burlaivis “Meridianas” pastatytas 1948 metais Suomijoje, Turku\n"
                                                                       " laivų statykloje, kaip kontribucija Tarybų Sąjungai po Antrojo\n"
                                                                       " pasaulinio karo kartu su kitais 48 tokio tipo burlaiviais."],
                      "Klaipeda - Klaipėdos universiteto pastatų kompleksas": [klavieta15, "Klaipėdos universitetas yra jauniausias Lietuvoje. 1904-1907 metais buvo\n"
                                                                                " pastatyta didžioji dalis pastatų komplekso. "]}
sauvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\1sauvieta.png')
sauvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\2sauvieta.png')
sauvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\3sauvieta.png')
sauvieta4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\4sauvieta.png')
sauvieta5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\5sauvieta.png')
sauvieta6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\6sauvieta.png')
sauvieta7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\7sauvieta.png')
sauvieta8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\8sauvieta.png')
sauvieta9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\sau\\9sauvieta.png')
siauliu_paminklai = {"Šiaulių iždinės pastatas": [sauvieta1, "Pastatas buvo pastatytas 1927 metais, kai Lietuva buvo nepriklausoma valstybė."],
                      "Akmenys su dubenėliais": [sauvieta2, "Dubenėtas akmuo- akmuo, archeologijos ir mitologijos paminklas, susijęs su\n"
                                                            " senovės žmogaus veikla. „Dubenėtieji akmenys“ su įvairių dydžių įdubomis.\n"
                                                            " Tokie akmenys dažniausiai aptinkami su didesnėmis a mažesnėmis, gamtos ar\n"
                                                            " žmogaus, sukurtomis įdubomis ir atliko aukuro paskirtį."],
                      "Šiaulių žudynių vieta": [sauvieta3, "1941 m. 732 žmonės buvo atvežti iš Šiaulių kalėjimo į Šiaulių miesto Pročiūnų\n"
                                                           " gatvę, kur buvo kankinti ir sušaudyti nacių."]}
siauliu_muziejai = {"Šiaulių „Aušros“ muziejus": [sauvieta4, "Beveik šimtmetį skaičiuojantis Šiaulių „Aušros“ muziejus nuolat keisdamasis ir\n"
                                                             " modernėdamas šiandien yra vienas iš didžiausių ir įvairialypių Lietuvos\n"
                                                             " muziejų."],
                      "Šiaulių istorijos muziejus, Šiaulių „Aušros“ muziejus": [sauvieta5, "Beveik šimtmetį skaičiuojantis Šiaulių „Aušros“ muziejus nuolat keisdamasis\n"
                                                                                           " ir modernėdamas šiandien yra vienas iš didžiausių ir įvairialypių\n"
                                                                                           " Lietuvos muziejų."],
                      "Šiaulių „Aušros“ muziejus ": [sauvieta6, "Edukacija, Dviračių muziejus, Fotografijos muziejus, Radijo ir televizijos muziejus,\n"
                                                                                       " Chaimo Frenkelio, vila, ŠAM Edukacijos centras, Žaliūkių malūnininko sodyba,\n"
                                                                                       " Venclauskių namai"]}
siauliu_kultura = {"Šiaulių kultūros centras": [sauvieta7, "Šiaulių kultūros centras – organizacija, teikianti įvairiapuses kultūrines paslaugas\n"
                                                           " miestiečiams, sudaranti sąlygas visuomenei dalyvauti kultūros renginiuose, o \n"
                                                           "kiekvienam šiauliečiui – užsiimti saviraiška."],
                      "Šiauliai - Tautodailininkės Rasos Šiškuvienės karpinių iš popieriaus paroda": [sauvieta8, "Tautodailininkė Rasa Šiškuvienė gimė ir gyvena Šiaulių rajone. Pagal\n"
                                                                                                      " išsilavinimą yra ikimokyklinio ugdymo pedagogė, bet jau daug metų\n"
                                                                                                      " dirba Briduose, kultūros centre ir bibliotekoje."],
                      "Šiaulių dailės galerija": [sauvieta9, "Nertis iš kailio yra ne tik apie kūniškas patirtis, bet ir apie bandymą nutrinti\n"
                                                             " medijų ribas, naujai prakalbinti grafiką ir ją kvestionuoti pasitelkiant \n"
                                                             "skaitmenines fiksavimo priemones. "]}
panvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\1panvieta.png')
panvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\2panvieta.png')
panvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\3panvieta.png')
panvieta4 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\4panvieta.png')
panvieta5 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\5panvieta.png')
panvieta6 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\6panvieta.png')
panvieta7 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\7panvieta.png')
panvieta8 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\8panvieta.png')
panvieta9 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\pan\\9panvieta.png')
panevezio_paminklai = {"""Panevežys - Pieta"Atgimusiai tautai""": [panvieta1, "Pieta „Atgimusiai tautai“ – tai istoriniais 1990 m. prisikėlusios lietuvių tautos\n"
                                                                  " kančias simbolizuojantis paminklas."],
                      "Panevežys - Skulpturos Juozo Zikaro": [panvieta2, "XX amžiuje Panevėžio kraštas garsėjo savanoriais. Norint įamžinti\n"
                                                             " Nepriklausomybės kovas, visoje Lietuvoje buvo planuojama statyti\n"
                                                             " jas menančius paminklus."],
                      "Panevežys - ŠV.Jezaus širdies paminklas": [panvieta3, "Carinės okupacijos metais Panevėžyje paminklai nebuvo statomi viešose\n"
                                                                 " vietose. Respublikos laikais Panevėžys buvo įvairių tautų miestas."]}
panevezio_muziejai = {"Panevėžio kraštotyros muziejus": [panvieta4, "Muziejaus misija: kartu keliauti laiku atminties ir pažinimo takais, suteikiant\n"
                                                                    " saviraiškos, augimo ir bendravimo galimybes, vardan ateities ugdyti pilietiškumą,\n"
                                                                    " pasididžiavimą savo kraštu. Iš dūšios, iki paskutinio atodūsio."],
                      "Panevežys - Linų muziejus, Ėriškių kultūros centras": [panvieta5, "Ėriškių kultūros centre ir padalinyje Tradicinių amatų centre vykdoma meno\n"
                                                                             " mėgėjų veikla, rengiami puodžiaus ir audėjo amato mokymai, vykdomos\n"
                                                                             " edukacinės programos, meno būrelio, muziejinė veikla."],
                      "Panevežys - Aukštaitijos siaurasis geležinkelis": [panvieta6, "Įvairiais laikotarpiais keitėsi jo paskirtis. Savo gyvavimo pradžioje siaurukas\n"
                                                                         " gabeno įvairius krovinius, vežė keleivius. Pakilimą siaurasis geležinkelis \n"
                                                                         "išgyveno tarpukariu, kuomet buvo plačiai naudojamas įvairiose ūkio šakose. "]}
panevezio_kultura = {"Panevežys - Elenos Mezginaitės viešoji biblioteka": [panvieta7, "Moderni, kurianti vertę, orientuota į vartotoją institucija, lanksčiai prisitaikanti\n"
                                                                          " prie besikeičiančių gyvenimo sąlygų socialinėje bendruomenės struktūroje."],
                      "Panevežys - Miesto dailės galerija": [panvieta8, "Dailės galerija rengia įvairių žanrų personalines, grupines, vienos meninės\n"
                                                            " koncepcijos parodas. Čia eksponuojami Panevėžio, Aukštaitijos, Lietuvos ir\n"
                                                            " užsienio menininkų kūriniai."],
                      "Panevežys - Teatras „Menas“": [panvieta9, "Spektaklis Rimtai linksmos pasakaitės skirtas 7-11 metų vaikams ir jų tėveliams. \n"
                                                     "Jame linksmai ir šmaikščiai kalbama apie rimtus bei svarbius dalykus: tiesą ir\n"
                                                     " paskalas, darbštumą ir girtuoklystę, nuoširdumą ir tuščiagarbystę, vienatvę ir\n"
                                                     " bendruomeniškumą. "]}
alyvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\aly\\1alyvieta.png')
alyvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\aly\\2alyvieta.png')
alyvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\aly\\3alyvieta.png')
alytu_paminklai = {"Alytaus miesto parkas ": [alyvieta1, "Alytaus miesto parkas pradėtas formuoti dar 1926 m. natūraliame pušyne,\n"
                                                         " kūrimo darbai pradėti 1930 m. pagal inž. Stasio Taškūno projektą,\n"
                                                         " oficialiai įkurtas 1931 metais. "]}
alytu_muziejai = {"Alytaus Kraštotyros muziejus": [alyvieta2, "Pirmu alytiškių bandymu kurti tautos kultūra ir praeitimi besidominčią\n"
                                                              " organizaciją galime laikyti 1920 m. sausio 13 d. Alytaus apskrities\n"
                                                              " viršininko kanceliarijoje įregistruotą „Dzūkijos Aušros“ draugiją."]}
alytu_kultura = {"Alytaus piliakalnis": [alyvieta3, "Alytaus piliakalnis – tai šimtmečius menąs miesto įkūrimo liudininkas. Jis\n"
                                                    " apipintas nesuskaičiuojama gausybe legendų. Viena iš jų byloja apie meilę\n"
                                                    " ir miesto vardo atsiradimą. Yra labai romantiška versija – bajoro duktės\n"
                                                    " Migrausėlės ir kunigaikščio sūnaus Alytos meilė."]}
marvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\mar\\1marvieta.png')
marvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\mar\\2marvieta.png')
marvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\mar\\3marvieta.png')
marijampoles_paminklai = {"Marijampole - Paminklinis akmuo V. Kernagio": [marvieta1, "Nemarus kūrėjas, amžinai gyva ir jo daina. Iš tiesų, čia taip,"
                                                                       " gražu, kad pravirkt gali…"]}
marijampoles_muziejai = {"Marijampole - Prezidento Kazio Griniaus muziejus": [marvieta2, "Marijampolės krašto ir Prezidento Kazio Griniaus muziejus – vienas \n"
                                                                           "seniausių muziejų Suvalkijoje, įsteigtas 1933 metais, šiuo metu\n"
                                                                           " įsikūręs XIX a. pab. pastatų komplekse, buvusiuose teismo rūmuose."]}
marijampoles_kultura = {"Marijampolės kultūros centras": [marvieta3, "Moderni įstaiga, atsižvelgianti į laikmečio ir poreikių kaitą, puoselėjanti etninę\n"
                                                                     " kultūrą, mėgėjų meną, kurianti menines programas, organizuojanti profesionalaus\n"
                                                                     " meno sklaidą, edukacines ir pramogines veiklas."]}
mazvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\maz\\1mazvieta.png')
mazvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\maz\\2mazvieta.png')
mazvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\maz\\3mazvieta.png')
mazeikiu_paminklai = {"Mazeikiai - Dekorativinės skulptūros": [mazvieta1, "Senajame parke Mažeikiuose projektuotos stilizuotų gyvūnų skulptūros.\n"
                                                              " Medinio karkaso kompozicijos skirtos vaikų žaidimams. 2008m."]}
mazeikiu_muziejai = {"Mažeikių muziejus": [mazvieta2, "Mažeikių muziejus įkurtas 1928 m. Jame saugomi ir eksponuojami Žemaitijos \n"
                                                      "krašto archeologijos, etnografijos, profesionalių dailininkų darbų ir\n"
                                                      " liaudies meno rinkiniai. "]}
mazeikiu_kultura = {"Mažeikių rajono savivaldybės kultūros centras": [mazvieta3, "Kultūros centro rūmai (Naftininkų g. 11) pastatyti 1987 m. Bendras\n"
                                                                                 " plotas – 7 586,84 kv. m. 2015-aisiais atnaujinta Didžioji salė sutalpina\n"
                                                                                 " 729 žiūrovus, Mažoji salė – 200, Pramogų salė – nuo 150 iki 600. "]}
jonvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\jon\\1jonvieta.png')
jonvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\jon\\2jonvieta.png')
jonvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\jon\\3jonvieta.png')
jonavos_paminklai = {"Jonava - Paminklai genocido aukoms": [jonvieta1, "Memorialas Neries pakrantėje užkastų 1944–1955 m. Jonavos apylinkėse \n"
                                                              "žuvusių ir Jonavos NKVD–MVD–MGB pastate nužudytų Didžiosios Kovos\n"
                                                              " apygardos partizanų atminimui."]}
jonavos_muziejai = {"Jonavos krašto muziejus": [jonvieta2, "Klasicistinio stiliaus Jonavos pašto stotis statyta 1833-1835 m., tiesiant pašto\n"
                                                           " kelią tarp svarbių Rusijos imperijos miestų – tuometinės sostinės Sankt\n"
                                                           " Peterburgo ir Varšuvos."]}
jonavos_kultura = {"Jonavos r. savivaldybes kulturos centras": [jonvieta3, "1983 m. pastatytas Jonavos rajono savivaldybės kultūros centro (JKC) pastatas\n"
                                                                           " priklausė tuometiniam Jonavos „Azotas“ gamybiniam susivienijimui. 1999 m."]}
utevieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ute\\1utevieta.png')
utevieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ute\\2utevieta.png')
utevieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ute\\3utevieta.png')
utenos_paminklai = {"Utena - Netradicinių skulptūrų parkas Antalgėje": [utevieta1, "Ar žinojote, kad netoli Utenos miesto yra unikalus skulptūrų parkas, kur\n"
                                                                           " svečius pasitinka daktaro Unikausko skulptūra, eglių pavėsyje įsitaisęs\n"
                                                                           " lenktynininkas Benediktas Vanagas, o painiame labirinte slepiasi\n"
                                                                           " animacinių filmukų herojai?"]}
utenos_muziejai = {"Utenos kraštotyros muziejus": [utevieta2, "Muziejus Utenoje buvo įkurtas 1929 metais. Tų metų lapkričio 22 dieną\n"
                                                              " Utenos apskrities valdyba savo raštu Nr. 3444 leido Utenos apskrities\n"
                                                              " antrojo rajono mokyklų inspektoriui Antanui Namikui steigti muziejų \n"
                                                              "ir paskyrė jį to muziejaus vedėju."]}
utenos_kultura = {"Utenos kultūros centras": [utevieta3, "1933 m. birželio 15 d. Utenoje naujai pastatytuose antrosios šaulių rinktinės\n"
                                                         " rūmuose atidaryti „Šaulių namai – tautos namai“, tapę to meto apskrities \n"
                                                         "kultūros centru. "]}
kedvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ked\\1kedvieta.png')
kedvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ked\\2kedvieta.png')
kedvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ked\\3kedvieta.png')
kedainiu_paminklai = {"Kedainiai - Česlovo Milošo gimtinė": [kedvieta1, "Poetas, rašytojas, Nobelio premijos laureatas Česlovas Milošas gimė\n"
                                                            " Šeteniuose, kukliame mamos Veronikos tėvų Zigmanto ir Juzefos\n"
                                                            " (Sirutytės) Kunatų dvare 1911 m. birželio 30 d. ir buvo pakrikštytas\n"
                                                            " šalia Šetenių esančioje Šventybrasčio bažnyčioje."]}
kedainiu_muziejai = {"Kėdainių krašto muziejus": [kedvieta2, "1922 m. įkurtas Kėdainių krašto muziejus yra vienas seniausių Lietuvoje.\n"
                                                             " Jo įkūrėjas ir pirmasis direktorius buvo Kėdainių apskrities valdybos\n"
                                                             " pirmininkas Vladas Rybelis, jis padovanojo muziejui apie 1000 savo\n"
                                                             " surinktų senienų."]}
kedainiu_kultura = {"Kedainiai - Buvusi spaustuvė": [kedvieta3, "Nors pagrindinis žydų knygų spaudos centras pirmosios nepriklausomybės\n"
                                                    " metais Lietuvoje buvo Kaunas, „Bibliografijos žiniose“ pateikiamos\n"
                                                    " informacijos analizė atskleidžia, kad daugiausia religinės paskirties\n"
                                                    " knygų (86 pavadinimai) 1928–1940 m. išspausdinta Kėdainiuose, \n"
                                                    "Movšovičiaus ir Kagano spaustuvėje."]}
tauvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tau\\1tauvieta.png')
tauvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tau\\2tauvieta.png')
tauvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tau\\3tauvieta.png')
taurages_paminklai = {"Taurage - Tauro skulptūra": [tauvieta1, "2018 metų rugsėjį prie Tauragės pilies prieigų atidengta kalvio Kęstučio\n"
                                                     " Plyskaičio nulieta Tauro skulptūra. Kūrinys – natūralaus tauro dydžio,\n"
                                                     " ragų smaigalyje siekia tris su puse metro."]}
taurages_muziejai = {"Tauragės krašto muziejus": [tauvieta2, "Tauragės krašto muziejus įkurtas 1990-09-01. Jis ilgą laiką veikė kaip\n"
                                                             " Tauragės rajono savivaldybės Kultūros centro padalinys ir vadinosi\n"
                                                             " „Santakos“ muziejumi."]}
taurages_kultura = {"Tauragės geležinkelio stoties rūmai": [tauvieta3, "Prie Tremtinių kelio gatvės savo šviesiais fasadais praeivių dėmesį traukia\n"
                                                                       " Edmundo Alfonso Fryko (1876–1944) pagal klasicizmo stiliaus tradicijas\n"
                                                                       " projektuoti ir 1927–1928 m. iškilę puošnūs geležinkelio stoties rūmai."]}
telvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tel\\1telvieta.png')
telvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tel\\2telvieta.png')
telvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\tel\\3telvieta.png')
telsiu_paminklai = {"Telšiai - Rotušės šulinys": [telvieta1, "Šioje vietoje iki karo stovėjo miesto šulinys. Apie tai byloja sena miesto\n"
                                                   " 1905 m. nuotrauka. Tuo metu buvę labai daug arklių, turgams reikėjo vandens."]}
telsiu_muziejai = {"""Telšiai - Žemaičių muziejus "Alka""""": [telvieta2, "Žemaičių muziejus „Alka” – svarbiausias LR Žemaitijos etnografinio regiono\n"
                                                                " istorijos muziejus Telšiuose. Jis plačiausiai atskleidžia savitą Žemaitijos\n"
                                                                " istorijos raidą, supažindina lankytojus su šio krašto gamta, žmonių buitimi\n"
                                                                " bei turtinga meno kūrinių kolekcija. "]}
telsiu_kultura = {"Telšiai - Amžiaus cenzas": [telvieta3, "Amžiaus cenzas vertintiniems archeologinio vertingųjų savybių pobūdžio\n"
                                                " objektams ar vietovėms yra iki 1800 metų, etnokultūrinio, istorinio ir\n"
                                                " sakralinio vertingųjų savybių pobūdžio objektams ar vietovėms."]}
ukmvieta1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ukm\\1ukmvieta.png')
ukmvieta2 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ukm\\2ukmvieta.png')
ukmvieta3 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\newpythonProject\\image\\vietos\\ukm\\3ukmvieta.png')
ukmerges_paminklai = {"Ukmerge - Nepriklausomybės paminklas": [ukmvieta1, "Lietuvos nepriklausomybės dešimtmečio paminklas"]}
ukmerges_muziejai = {"Ukmergės kraštotyros muziejus": [ukmvieta2, "Pagrindiniai Ukmergės kraštotyros muziejaus įkūrimo iniciatoriai – dailininkai\n"
                                                                  " Petras ir Domicelė Tarabildos, tuo metu ramesnio gyvenimo\n"
                                                                  " ieškoję provincijoje..."]}
ukmerges_kultura = {"Ukmergės kultūros centras": [ukmvieta3, "Ukmergės kultūros centras atveria duris į modernų, šiuolaikišką pasaulį,\n"
                                                             " kuriame vyksta spektakliai, koncertai, įvairūs kultūriniai renginiai,\n"
                                                             " tarptautinis perkusijos ir būgnų festivalis ."]}
#---------miestai----------
vilnius = {**vilniaus_paminklai, **vilniaus_muziejai, **vilniaus_kultura}
kaunas = {**kauno_paminklai, **kauno_muziejai, **kauno_kultura}
klaipeda = {**klaipedos_paminklai, **klaipedos_muziejai, **klaipedos_kultura}
siauliai = {**siauliu_paminklai, **siauliu_muziejai, **siauliu_kultura}
panevezys = {**panevezio_paminklai,**panevezio_muziejai, **panevezio_kultura}
alytus = {**alytu_paminklai, **alytu_muziejai, **alytu_kultura}
marijampole = {**marijampoles_paminklai, **marijampoles_muziejai,**marijampoles_kultura}
mazeikiai = {**mazeikiu_paminklai, **mazeikiu_muziejai, **mazeikiu_kultura}
jonava = {**jonavos_paminklai, **jonavos_muziejai, **jonavos_kultura}
utena = {**utenos_paminklai, **utenos_muziejai, **utenos_kultura}
kedainiai = {**kedainiu_paminklai, **kedainiu_muziejai, **kedainiu_kultura}
taurage = {**taurages_paminklai, **taurages_muziejai, **taurages_kultura}
telsiai = {**telsiu_paminklai, **telsiu_muziejai, **telsiu_kultura}
ukmerge = {**ukmerges_paminklai, **ukmerges_muziejai, **ukmerges_kultura}
#---------kategorijos----------
sarasas_visko = {**city_list, **vilnius,
                 **kaunas,
                 **klaipeda,
                 **siauliai,
                 **panevezys,
                 **alytus,
                 **marijampole,
                 **mazeikiai,
                 **jonava,
                 **utena,
                 **kedainiai,
                 **taurage,
                 **telsiai,
                 **ukmerge}
paminklai_visi = {**vilniaus_paminklai,
                  **kauno_paminklai,
                  **klaipedos_paminklai,
                  **siauliu_paminklai,
                  **panevezio_paminklai,
                  **alytu_paminklai,
                  **marijampoles_paminklai,
                  **mazeikiu_paminklai,
                  **jonavos_paminklai,
                  **utenos_paminklai,
                  **kedainiu_paminklai,
                  **taurages_paminklai,
                  **telsiu_paminklai,
                  **ukmerges_paminklai}
muzejai_visi = {**vilniaus_muziejai,
                **kauno_muziejai,
                **klaipedos_muziejai,
                **siauliu_muziejai,
                **panevezio_muziejai,
                **alytu_muziejai,
                **marijampoles_muziejai,
                **mazeikiu_muziejai,
                **jonavos_muziejai,
                **utenos_muziejai,
                **kedainiu_muziejai,
                **taurages_muziejai,
                **telsiu_muziejai,
                **ukmerges_muziejai}
kultura_visi = {**vilniaus_kultura,
                **kauno_kultura,
                **klaipedos_kultura,
                **siauliu_kultura,
                **panevezio_kultura,
                **alytu_kultura,
                **marijampoles_kultura,
                **mazeikiu_kultura,
                **jonavos_kultura,
                **utenos_kultura,
                **kedainiu_kultura,
                **taurages_kultura,
                **telsiu_kultura,
                **ukmerges_kultura}