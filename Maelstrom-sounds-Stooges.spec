Summary:	Rockin' asteroids game - extra sounds
Summary(pl.UTF-8):	Gra, w której strzelasz do asteroidów - dodatkowe dźwięki
Name:		Maelstrom-sounds-Stooges
Version:	1
Release:	1
License:	unknown
Group:		X11/Applications/Games
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Stooges_Sounds.zip
# Source0-md5:	f5004b158aece52154ccde47571b0f20
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-sounds
Obsoletes:	Maelstrom-sounds-AoD
Obsoletes:	Maelstrom-sounds-BB
Obsoletes:	Maelstrom-sounds-Funky
Obsoletes:	Maelstrom-sounds-Martin
Obsoletes:	Maelstrom-sounds-Simpsons
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
Extra sounds for Maelstrom.

%description -l pl.UTF-8
Dźwięki dla Maelstroma.

%prep
%setup -q -n Stooges_Sounds

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install Maelstrom_Sounds.bin $RPM_BUILD_ROOT%{_gamedir}/"%Maelstrom_Sounds"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_gamedir}/*
