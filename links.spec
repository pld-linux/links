# I dont know what release it should have
Summary:	Lynx-like text WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx.
Summary(pl):	Podobna do Lynksa tekstowa przegl�darka WWW
Summary(pt_BR):	O links � um browser para modo texto, similar ao lynx.
Summary(ru):	��������� WWW ������� ���� Lynx
Summary(uk):	��������� WWW ������� ���� Lynx
Name:		links
Version:	0.97
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://atrey.karlin.mff.cuni.cz/%7Eclock/twibright/%{name}/download/%{name}-current.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
URL:		http://atrey.karlin.mff.cuni.cz/%7Eclock/twibright/links
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel => 5.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  svgalib-devel
BuildRequires:  XFree86-devel
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
Links jest tekstow� przegl�dark� WWW, na pierwszy rzut oka podobn� do
Lynksa, ale mimo wszystko inn�:

- renderuje tabelki i ramki,
- wy�wietla kolory zgodnie z definicjami w ogl�danej stronie HTML,
- u�ywa opuszczanego menu (jak w Midnight Commanderze),
- mo�e �ci�ga� pliki w tle.

%description -l pt_BR
Links � um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conex�es
HTTP/1.1 keepalive.

%description -l ru
Links - ��� ��������� WWW �������, �� ������ ������ ������� �� Lynx,
�� ��������� ������������:

- ���������� ������� � (�����) ������
- ���������� ����� ��� ������� � HTML ��������
- ���������� ���������� ���� (��� � Midnight Commander)
- ����� ��������� ����� � ����

%description -l uk
Links - �� ��������� WWW �������, �� ������ ������ ������ �� Lynx, ���
����� צ�ͦ���� צ� �����:

- צ�������� �����æ �� (���������) ������
- �����դ ������� �� ������� � HTML ���Ҧ�æ
- ����������դ �������ަ ���� (�� � Midnight Commander)
- ���� ������������� ����� � ��Φ

%prep
%setup -q -n %{name}-current

%build
#rm -f mssing
#aclocal
#autoconf
#automake -a -c -f
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
    CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure2_13 CPPFLAGS="$CPPFLAGS" \
    --enable-graphics \
    --enable-javascript
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir},%{_mandir}/pl/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
gzip -9nf AUTHORS BUGS ChangeLog README SITES TODO NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/links.png
