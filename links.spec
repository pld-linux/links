Summary:	Lynx-like text WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa tekstowa przegl╠darka WWW
Summary(pt_BR):	O links И um browser para modo texto, similar ao lynx
Summary(ru):	Текстовый WWW броузер типа Lynx
Summary(uk):	Текстовий WWW броузер типу Lynx
Name:		links
Version:	2.0pre5
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/links/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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

- отображает таблицы и (скоро) фреймы
- показывает цвета как указано в HTML странице
- использует выпадающие меню (как в Midnight Commander)
- может загружать файлы в фоне.

%description -l uk
Links - це текстовий WWW броузер, на перший погляд схожий на Lynx, але
трохи в╕дм╕нний в╕д нього:

- в╕добража╓ таблиц╕ та (незабаром) фрейми
- показу╓ кольори як вказано в HTML стор╕нц╕
- використову╓ випадаюч╕ меню (як в Midnight Commander)
- може завантажувати файли в фон╕.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
#autoheader
%{__automake}
%configure \
	--enable-javascript \
	--enable-graphics \
	--with-ssl \
	--with-libjpeg \
	--with-libtiff \
	--without-svgalib \
	--without-fb \
	--without-pmshell \
	--without-atheos \
	--with-x

patch -p0 <<END
--- Makefile.orig	Wed May 29 21:50:45 2002
+++ Makefile	Wed May 29 21:51:07 2002
@@ -41,10 +41,10 @@
 pkgincludedir = \$(includedir)/links
 top_builddir = .
 
-ACLOCAL = /missing aclocal
-AUTOCONF = /missing autoconf
-AUTOMAKE = /missing automake
-AUTOHEADER = /missing autoheader
+ACLOCAL = ./missing aclocal
+AUTOCONF = ./missing autoconf
+AUTOMAKE = ./missing automake
+AUTOHEADER = ./missing autoheader
 
 INSTALL = /usr/bin/install -c
 INSTALL_PROGRAM = \${INSTALL}
END

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
%doc AUTHORS BUGS ChangeLog README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/*
