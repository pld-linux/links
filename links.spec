#
# Conditional build:
# _without_javascript - don't use javascript interpreter
# _without_graphics - don't use graphics
# _without_svgalib - compile without svgalib graphics driver
# _without_x - compile without X Window System graphics driver
# _without_fb - compile without Linux Framebuffer graphics driver
# _without_pmshell - compile without PMShell graphics driver
# _without_atheos - compile without Atheos graphics driver

%define _snap 20020516

Summary:	Lynx-like WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx.
Summary(pl):	Podobna do Lynksa przegl╠darka WWW
Summary(pt_BR):	O links И um browser para modo texto, similar ao lynx.
Summary(ru):	Текстовый WWW броузер типа Lynx
Summary(uk):	Текстовий WWW броузер типу Lynx
Name:		links
Version:	current
Release:	%{_snap}.4
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://atrey.karlin.mff.cuni.cz/~clock/twibright/%{name}/download/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
%if%{!?_without_graphics:1}%{?_without_graphics:0}
Source4:	g%{name}.desktop
Patch0:		%{name}-links-g_if_glinks.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-ac25x.patch
%endif
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/links
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel => 5.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	zlib-devel
%if%{!?_without_graphics:1}%{?_without_graphics:0}
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
%{!?_without_svgalib:BuildRequires:  svgalib-devel}
%{!?_without_x:BuildRequires:  XFree86-devel}
%endif
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Links is a WWW browser, at first look similiar to Lynx, but somehow
different:

- renders tables and frames,
- displays colors as specified in current HTML page,
- uses drop-down menu (like in Midnight Commander),
- can download files in background.

%{!?_without_graphics:This version can work in graphical mode.}
%{!?_without_javascript:This version has support for JavaScript.}

%description -l es
Links es un browser WWW modo texto, similar al Lynx. El links muestra
tablas, hace baja archivos en segundo plano, y usa conexiones HTTP/1.1
keepalive.

%description -l pl
Links jest przegl╠dark╠ WWW, na pierwszy rzut oka podobn╠ do Lynksa,
ale mimo wszystko inn╠:

- renderuje tabelki i ramki,
- wy╤wietla kolory zgodnie z definicjami w ogl╠danej stronie HTML,
- u©ywa opuszczanego menu (jak w Midnight Commanderze),
- mo©e ╤ci╠gaФ pliki w tle.

%{!?_without_graphics:Ta wersja mo©e pracowaФ w trybie graficznym.}
%{!?_without_javascript:Ta wersja posiada wsparcie dla JavaScript.}

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
- может загружать файлы в фоне

%description -l uk
Links - це текстовий WWW броузер, на перший погляд схожий на Lynx, але
трохи в╕дм╕нний в╕д нього:

- в╕добража╓ таблиц╕ та (незабаром) фрейми
- показу╓ кольори як вказано в HTML стор╕нц╕
- використову╓ випадаюч╕ меню (як в Midnight Commander)
- може завантажувати файли в фон╕

%prep
%setup -q
%{!?_without_graphics:%patch0 -p1}
%patch1 -p1
%patch2 -p1

%build
rm -f mssing
aclocal
automake -a -c -f
autoconf
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
    CPPFLAGS="`pkg-config libpng12 --cflags`"; export CPPFLAGS
fi
%configure \
    %{!?_wihout_graphics:--enable-graphics} \
    %{!?_without_javascript:--enable-javascript} \
		%{?_without_svgalib:--without-svgalib} \
		%{?_without_x:--without-x} \
		%{?_without_fb:--without-fb} \
		%{?_without_pmshell:--without-pmshell} \
		%{?_without_atheos:--without-atheos}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir},%{_mandir}/pl/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%if%{!?_without_graphics:1}%{?_without_graphics:0}
ln -sf links $RPM_BUILD_ROOT%{_bindir}/glinks
echo ".so links.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glinks.1
echo ".so links.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/glinks.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README SITES TODO NEWS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/links.png
