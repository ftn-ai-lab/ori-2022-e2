### Priprema - primeri zadataka
#### Lak
* Robot: doći od starta do cilja, uz prvobitno kupljenje jedne plave kutije. Kada robot pokupi kutiju može da se kreće i dijagonalno.
* Robot: doći od starta do cilja, uz prvobitno kupljenje prvo plave, pa narandžaste kutije.
#### Srednji
* Robot: doći od starta do cilja, uz prvobitno kupljenje tačno tri plave kutije. Na tabli može biti proizvoljan broj plavih kutija.
* Robot: doći od starta do cilja, uz korišćenje portala (žuto polje) koji omogućavaju teleportaciju na ostale portale. Kada robot prođe kroz portal (stane i "odluči" da će otići na neki drugi portal), postoji šansa od 70% da će se zaista teleportovati na drugi portal, i šansa od 30% da će biti teleportovan na početnu poziciju.
#### Težak
* Robot: doći od starta do cilja, uz prvobitno kupljenje tačno tri plave i dve narandžaste kutije. Na tabli može biti proizvoljan broj plavih i narandžastih kutija. Da bi robot mogao da pokupi narandžastu kutiju, mora kod sebe imati barem jednu više plavu kutiju.
* Robot: doći od starta do cilja, uz prvobitno kupljenje određenog broja kutija, ali uz izbegavanje polja koja predstavljaju vatru (ideja je da robot radije ide putem koji je dalji od vatre).


## Primer kolokvijuma (realan primer od prethodnih godina)
Robot predstavlja tenisera i njegov zadatak jeste da osvoji tekući gem u meču. Vaš zadatak jeste da ispunite kriterijum definisan zadatkom i da završite tekući gem.
#### Lak
Teniser treba da osvoji tačno četiri poena da bi završio gem. Pozicije za osvajanje poena na tabli su predstavljene ljubičastom kutijom. Dok još uvek osvaja poene, teniser se kreće do tri polja levo ili desno (jedno, dva ili tri polja levo ili desno), jedno polje gore ili jedno polje dole. Kada osvoji sve poene, teniser treba da zatvori gem tako što će otići do crvene kutije krećući se po jedno polje gore, dole, levo ili desno.
#### Srednji
Teniser se kreće po terenu i dolazi do pozicija sa kojih se lako osvajaju poeni (ljubičasta polja) i do pozicija sa kojih će sigurno napraviti grešku (narandžasta polja). Kada teniser dođe na ljubičasto polje on osvaja poen, a kada dođe u narandžasto polje on sigurno gubi poen. Kada teniser osvoji četiri poena ili izgubi četiri poena, treba da ode do crvene kutije i da zatvori tekući gem. Teniser se sve vreme kreće kao figura kraljice u šahu. Na konzoli ispisivati trenutni rezultat u gemu i pri završetku gema ispisati da li ga je teniser osvojio ili izgubio.
#### Težak
Teniser se kreće po terenu i dolazi do pozicija sa kojih se lako osvajaju poeni (ljubičasta polja) i do nezgodnih pozicija u kojima postoji verovatnoća od 75% da će napraviti grešku (narandžasta polja). Ako teniser dođe na nezgodnu poziciju (narandžasto polje) u kojoj je odlučeno da je on napravio grešku, teniser traži challenge (sistem zvani „oko sokolovo“) i postoji verovatnoća od 50% da je sudija pogrešio. Ako je sudija pogrešio teniser ipak dobija poen, a ako je sudija bio u pravu prethodna odluka ostaje i teniser je zaista izgubio poen. Ukoliko se dođe do situacije da je rezultat 3:3 (u tenisu predstavljeno kao 40:40 - DEUCE), teniser će igrati dok god ne osvoji dva poena zaredom ili dok ne izgubi dva poena zaredom. Kada teniser osvoji ili izgubi dovoljno poena da bi gem bio završen, treba da ode do crvene kutije i da ga završi. Teniser se u toku igre kreće kao figura kraljice u šahu, a kada se uslovi za završetak gema ispune, on se do crvene kutije kreće kao figura kralja u šahu. Na konzoli ispisivati trenutni rezultat gema, ukoliko teniser napravi grešku ispisati da li je challenge nakon nje bio uspešan ili ne, a pri završetku gema ispisati da li ga je teniser osvojio ili izgubio.
