Summary:	Lynx-like text WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa tekstowa przegl╠darka WWW
Summary(pt_BR):	O links И um browser para modo texto, similar ao lynx
Summary(ru):	Текстовый WWW броузер типа Lynx
Summary(uk):	Текстовий WWW броузер типу Lynx
Name:		links
Version:	0.98
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://artax.karlin.mff.cuni.cz/~mikulas/links/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
URL:		http://artax.karlin.mff.cuni.cz/~mikulas/links/
Patch0:		http://www.misiek.eu.org/ipv6/%{name}-0.92-ipv6-20000921.patch.gz
Patch1:		%{name}-dump_codepage.patch
Patch2:		%{name}-gzip_fallback.patch
Patch3:		%{name}-content_encoding.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	zlib-devel
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Links is a text based WWW browser, at first look similiar to Lynx, but
somehow different:

- renders tables and frames,
- displays colors as specified in current HTML page,
- uses drop-down menu (like in Midnight Commander),
- can download files in background.

%description -l es
Links es un browser WWW modo texto, similar al Lynx. El links muestra
tablas, hace baja archivos en segundo plano, y usa conexiones HTTP/1.1
keepalive.

%description -l pl
Links jest tekstow╠ przegl╠dark╠ WWW, na pierwszy rzut oka podobn╠ do
Lynksa, ale mimo wszystko inn╠:

- renderuje tabelki i ramki,
- wy╤wietla kolory zgodnie z definicjami w ogl╠danej stronie HTML,
- u©ywa opuszczanego menu (jak w Midnight Commanderze),
- mo©e ╤ci╠gaФ pliki w tle.

%description -l pt_BR
Links И um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conexУes
HTTP/1.1 keepalive.

%description -l ru
Links - это текстовый WWW броузер, на первый взгляд похожий на Lynx,
но несколько отличающийся:

- отображает таблицы и (скоро) фреймы,
- показывает цвета как указано в HTML странице,
- использует выпадающие меню (как в Midnight Commander),
- может загружать файлы в фоне.

%description -l uk
Links - це текстовий WWW броузер, на перший погляд схожий на Lynx, але
трохи в╕дм╕нний в╕д нього:

- в╕добража╓ таблиц╕ та (незабаром) фрейми,
- показу╓ кольори як вказано в HTML стор╕нц╕,
- використову╓ випадаюч╕ меню (як в Midnight Commander),
- може завантажувати файли в фон╕.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/*
