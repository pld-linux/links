Summary:	Lynx-like text WWW browser
Summary(pl):	Podobna do Lynxa tekstowa przegl�darka WWW
Name:		links
Version:	23.05.2000
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	%{name}-%{version}.tar.gz
URL:		http://artax.karlin.mff.cuni.cz/~mikulas/links/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel => 5.0
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Links is a text based WWW browser, at first look similiar to Lynx, but
somehow different:

- renders tables and frames
- displays colors as specified in current HTML page
- uses drop-down menu (like in Midnight Commander)
- can download files in background

%description -l pl
Links jest tekstow� przegl�dark� WWW, na pierwszy rzut oka podobn� do Lynxa,
ale mimo wszystko inn�:

- renderuje tabelki i ramki
- wy�wietla kolory zgodnie z definicjami w ogl�danej stronie HTML
- u�ywa opuszczanego menu (jak w Midnight Commanderze)
- mo�e �ci�ga� pliki w tle

%prep
# temporary -n, to work with links-current snapshots
%setup  -q -n %{name}-current

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog README SITES TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
