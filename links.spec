Summary:	Lynx-like text WWW browser
Summary(pl):	Podobna do Lynxa tekstowa przegl�darka WWW
Name:		links
Version:	0.95
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://artax.karlin.mff.cuni.cz/~mikulas/links/download/%{name}-%{version}.tar.gz
Source1;	%{name}.desktop
Patch0:		http://www.misiek.eu.org/ipv6/%{name}-0.92-ipv6-20000921.patch.gz
URL:		http://artax.karlin.mff.cuni.cz/~mikulas/links/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel => 5.1
BuildRequires:	openssl-devel
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
Links jest tekstow� przegl�dark� WWW, na pierwszy rzut oka podobn� do
Lynxa, ale mimo wszystko inn�:

- renderuje tabelki i ramki
- wy�wietla kolory zgodnie z definicjami w ogl�danej stronie HTML
- u�ywa opuszczanego menu (jak w Midnight Commanderze)
- mo�e �ci�ga� pliki w tle

%prep
%setup  -q
#%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
insall -d $RPM_BUILD_ROOT%{_applnkdir}/Networl/WWW

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networl/WWW

gzip -9nf AUTHORS BUGS ChangeLog README SITES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Networl/WWW/*
%{_mandir}/man*/*
