Summary:	Lynx-like text WWW browser
Summary(es.UTF-8):	El links es un browser para modo texto, similar a lynx
Summary(pl.UTF-8):	Podobna do Lynksa tekstowa przeglądarka WWW
Summary(pt_BR.UTF-8):	O links é um browser para modo texto, similar ao lynx
Summary(ru.UTF-8):	Текстовый WWW броузер типа Lynx
Summary(uk.UTF-8):	Текстовий WWW броузер типу Lynx
Name:		links
Version:	1.03
Release:	4.1
Epoch:		2
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.jikos.cz/~mikulas/links/download/%{name}-%{version}.tar.gz
# Source0-md5:	41ab5dd9ffdd5b8dbed2214eee2bc23c
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
Patch0:		%{name}-0.92-ipv6-20000921.patch
Patch1:		%{name}-gzip_fallback.patch
Patch2:		%{name}-content_encoding.patch
Patch3:		%{name}-home_etc.patch
Patch4:		openssl.patch
URL:		http://www.jikos.cz/~mikulas/links/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
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

%description -l es.UTF-8
Links es un browser WWW modo texto, al parecido similar al Lynx, mas
algo diferente:

- plasma las tablas y los marcos
- muestra colores tales como especificados en la página HTML actual,
- se controla con un menú (como el de Midnight Commander),
- puede hacer baja archivos en segundo plano.

%description -l pl.UTF-8
Links jest tekstową przeglądarką WWW, na pierwszy rzut oka podobną do
Lynksa, ale mimo wszystko inną:

- renderuje tabelki i ramki,
- wyświetla kolory zgodnie z definicjami w oglądanej stronie HTML,
- używa opuszczanego menu (jak w Midnight Commanderze),
- może ściągać pliki w tle.

%description -l pt_BR.UTF-8
Links é um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conexões
HTTP/1.1 keepalive.

%description -l ru.UTF-8
Links - это текстовый WWW броузер, на первый взгляд похожий на Lynx,
но несколько отличающийся:

- отображает таблицы и (скоро) фреймы,
- показывает цвета как указано в HTML странице,
- использует выпадающие меню (как в Midnight Commander),
- может загружать файлы в фоне.

%description -l uk.UTF-8
Links - це текстовий WWW броузер, на перший погляд схожий на Lynx, але
трохи відмінний від нього:

- відображає таблиці та (незабаром) фрейми,
- показує кольори як вказано в HTML сторінці,
- використовує випадаючі меню (як в Midnight Commander),
- може завантажувати файли в фоні.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1

#cd intl
#./gen-intl

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README SITES TODO
%attr(755,root,root) %{_bindir}/links
%{_desktopdir}/links.desktop
%{_pixmapsdir}/links.png
%{_mandir}/man1/links.1*
%lang(pl) %{_mandir}/pl/man1/links.1*
