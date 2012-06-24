Summary:	Lynx-like text WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa tekstowa przegl�darka WWW
Summary(pt_BR):	O links � um browser para modo texto, similar ao lynx
Summary(ru):	��������� WWW ������� ���� Lynx
Summary(uk):	��������� WWW ������� ���� Lynx
Name:		links
Version:	0.99pre13
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://artax.karlin.mff.cuni.cz/~mikulas/links/download/%{name}-%{version}.tar.gz
# Source0-md5:	3da202f9c1c855f30d0f60d92bf35e03
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
URL:		http://artax.karlin.mff.cuni.cz/~mikulas/links/
Patch0:		http://www.misiek.eu.org/ipv6/%{name}-0.92-ipv6-20000921.patch.gz
Patch1:		%{name}-dump_codepage.patch
Patch2:		%{name}-gzip_fallback.patch
Patch3:		%{name}-content_encoding.patch
Patch4:		%{name}-home_etc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.7c
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
Links es un browser WWW modo texto, al parecido similar al Lynx, mas algo diferente:

- plasma las tablas y los marcos
- muestra colores tales como especificados en la p�gina HTML actual,
- se controla con un men� (como el de Midnight Commander),
- puede hacer baja archivos en segundo plano.

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/*
