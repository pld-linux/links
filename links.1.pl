.\" Process this file with groff -man -Tascii links.1
.TH LINKS 1 "9 grudnia 1999"
.SH NAZWA
links \- Tekstowa przegl�darka WWW w stylu Lynx'a
.SH SK�ADNIA
.B links
.RI [ opcje ]
.I URL
.SH OPIS
.B links
to tekstowa przegl�darka www oparta na ncurses. Posiada kolorowy interfejs,
renderuje tabele, pobiera pliki w tle, posiada menu oraz prosty i zwarty kod.
.P 
W tej chwili jeszcze nie w pe�ni obs�uguje wy�wietlanie ramek, ale to 
nied�ugo si� zmieni.
.P
.B links
rozpoznaje lokalne (file://) oraz zdalne (http:// lub ftp://) typy URL-i.
.SH KLAWISZE
Mo�na u�ywa� nast�puj�cych kombinacji klawiszy:
.TP
.B ESC
wywo�uje menu
.TP
.B ^P, ^N   
przewi� ekran w g�r�, d�
.TP
.B [, ]
przewi� ekran w lewo, prawo
.TP
.B g�ra, d�
zaznacz odno�nik
.TP
.B ->
wybierz odno�nik
.TP
.B <-
powr�t
.TP
.B g
przejd� do URL
.TP
.B /
szukaj
.TP
.B ?
szukaj wstecz
.TP
.B n
znajd� nast�pne
.TP
.B N
znajd� poprzednie
.TP
.B =
informacje o dokumencie
.TP
.B \e
�r�d�o dokumentu
.TP
.B d
pobierz
.TP
.B ^C
wyj�cie
.SH OPCJE
Wi�kszo�� opcji mo�e by� ustawionych bezpo�rednio w przegl�darce lub w pliku
konfiguracyjnym, wi�c nie musisz przejmowa� si� zbytnio poni�szymi:
.TP
\f3-async-dns \f2<0>/<1>\f1
Asyncronous DNS resolver on(1)/off(0). 
.TP
\f3-max-connections \f2<maks>\f1
Maksymalna liczba jednoczesnych po��cze�.
(domy�lnie: 10)
.TP
\f3-max-connections-to-host \f2<maks>\f1
Maksymalna liczba jednoczesnych po��cze� z jednym serwerem.
(domy�lnie: 2)
.TP
\f3-retries \f2<pr�by>\f1
Liczba pr�b nawi�zania po��czenia.
(domy�lnie: 3)
.TP
\f3-receive-timeout \f2<sek>\f1
Maksymalny czas na nawiazanie po��czenia.
(domy�lnie: 120)
.TP
\f3-unrestartable-receive-timeout \f2<sek>\f1
Maksymalny czas na nawiazanie niewznawialnego po��czenia.
(domy�lnie: 600)
.TP
\f3-format-cache-size \f2<liczba>\f1
Liczba stron sformatowanych dokument�w w pami�ci podr�cznej.
(domy�lnie: 5)
.TP
\f3-memory-cache-size \f2<Kbajty>\f1
Pami�� podr�czna w kilobajtach.
(default: 1024)
.TP
\f3-http-proxy \f2<host:port>\f1
Nazwa i numer portu serwera HTTP proxy.
(domy�lnie: nic)
.TP
\f3-ftp-proxy \f2<host:port>\f1
Nazwa i numer portu serwera FTP proxy.
(domy�lnie: nic)
.TP
\f3-download-dir \f2<�cie�ka>\f1
Domy�lny katalog na pobierane pliki
(domy�lnie: aktualny katalog)
.TP
\f3-assume-codepage \f2<strona kodowa>\f1
Strona kodowa u�ywana gdy nie jest okre�lona �adna inna.
(domy�lnie: ISO 8859-1)
.TP
\f3-version\f1
Wy�wietla numer wersji
.BR links .
.SH PLIKI
.TP
.IP "\fI~/.links/.links.cfg\fR"
Plik konfiguracyjny tworzony automatycznie przez
.BR links .
.SH PLATFORMY
.B links
na pewno dzia�a na nast�puj�cych systemach Linux, FreeBSD, Solaris, IRIX, 
HPUX, Digital Unix oraz OS/2. Port dla Win32 jest nadal w fazie beta-test�w.
.SH B��DY
Nie mo�na ustanowi� po��czenia z niekt�rymi serwerami FTP (Novell, NT).
Po��czenie zawiesza si� na "Wysy�am ��danie".
.PP
OS/2: gdy nie powiedzie si� po��czenie zwracany jest b��d "Niew�a�ciwy
argument".
.PP
OS/2: gdy jest uruchomiony w trybie pe�noekranowym, myszka pozostawia cienie.
.PP
Prosz� wysy�a� informacje o wszelkich znalezionych b��dach pod adres Mikulas
Patocka <mikulas@artax.karlin.mff.cuni.cz>
.SH LICENCJA
.B links
jest oprogramowaniem wolnodost�pnym; mo�esz go rozprowadza� dalej i/lub
modyfikowa� na warunkach Powszechnej Licencji Publicznej GNU, wydanej przez
Fundacj� Wolnodost�pnego Oprogramowania - wed�ug wersji 2-giej tej Licencji
lub kt�rej� z p�niejszych wersji.
.SH AUTOR
Autorem
.B links
jest
.B Mikulas Patocka 
.BI <mikulas@artax.karlin.mff.cuni.cz>
.P
Ta strona manuala zosta�a napisana przez Grin <grin@tolna.net>,
wielkiego zwolennika
.BR links ,
kt�ry u�ywa tej przegl�darki na systemie Debian GNU/Linux.
.P 
T�umaczenia dokona� Arkadiusz 'Jo Joro' Sochala <jojoro@poczta.onet.pl>
.SH "ZOBACZ TAK�E"
.BR lynx (1),
.BR w3m (1)
