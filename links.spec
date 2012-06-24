#
# Conditional build:
# _without_javascript - don't use javascript interpreter
# _without_graphics - don't use graphics
# _without_svgalib - compile without svgalib graphics driver
# _without_x - compile without X Window System graphics driver
# _without_fb - compile without Linux Framebuffer graphics driver
# _without_pmshell - compile without PMShell graphics driver
# _without_atheos - compile without Atheos graphics driver

Summary:	Lynx-like WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa przegl�darka WWW
Summary(pt_BR):	O links � um browser para modo texto, similar ao lynx
Summary(ru):	��������� WWW ������� ���� Lynx
Summary(uk):	��������� WWW ������� ���� Lynx
Name:		links
Version:	2.1pre2
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/links/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
Source4:	g%{name}.desktop
Patch0:		%{name}-links-g_if_glinks.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-ac25x.patch
Patch3:		%{name}-current-reallyquit.patch
Patch4:		%{name}-img.patch
Patch5:		%{name}-convert-old-bookmarks.patch
Patch6:		%{name}-cookies-save.patch
Patch7:		%{name}-cookie-parsing.patch
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	zlib-devel
%if%{!?_without_graphics:1}%{?_without_graphics:0}
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
%{!?_without_javascript:BuildRequires:	flex}
%{!?_without_javascript:BuildRequires:	bison}
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
%{!?_without_x:BuildRequires:	XFree86-devel}
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
Links jest przegl�dark� WWW, na pierwszy rzut oka podobn� do Lynksa,
ale mimo wszystko inn�:

- renderuje tabelki i ramki,
- wy�wietla kolory zgodnie z definicjami w ogl�danej stronie HTML,
- u�ywa opuszczanego menu (jak w Midnight Commanderze),
- mo�e �ci�ga� pliki w tle.

%{!?_without_graphics:Ta wersja mo�e pracowa� w trybie graficznym.}
%{!?_without_javascript:Ta wersja obs�uguje JavaScript.}

%description -l pt_BR
Links � um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conex�es
HTTP/1.1 keepalive.

%description -l ru
Links - ��� ��������� WWW �������, �� ������ ������ ������� �� Lynx,
�� ��������� ������������:

- ���������� ������� � (�����) ������,
- ���������� ����� ��� ������� � HTML ��������,
- ���������� ���������� ���� (��� � Midnight Commander),
- ����� ��������� ����� � ����.

%description -l uk
Links - �� ��������� WWW �������, �� ������ ������ ������ �� Lynx, ���
����� צ�ͦ���� צ� �����:

- צ�������� �����æ �� (���������) ������,
- �����դ ������� �� ������� � HTML ���Ҧ�æ,
- ����������դ �������ަ ���� (�� � Midnight Commander),
- ���� ������������� ����� � ��Φ.

%prep
%setup -q
%{!?_without_graphics:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
rm -f missing
aclocal
%{__automake}
%{__autoconf}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"; export CPPFLAGS
fi
%configure \
	%{!?_without_graphics:--enable-graphics} \
	%{!?_without_javascript:--enable-javascript} \
	%{?_without_svgalib:--without-svgalib} \
	%{?_without_x:--without-x} \
	%{?_without_fb:--without-fb} \
	%{?_without_pmshell:--without-pmshell} \
	%{?_without_atheos:--without-atheos}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

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
%doc AUTHORS BUGS ChangeLog README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/*
