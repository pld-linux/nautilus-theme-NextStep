Summary:	NextStep theme
Summary(pl.UTF-8):   Motyw NextStep
Name:		nautilus-theme-NextStep
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
#http://www.lucidus.uklinux.net/index.php?theme=nautilus&get=nextstep.tar.gz
Source0:	nautilus-nextstep.tar.gz
# Source0-md5:	9ec899f201b74ba9357ca896b54ab5d6
URL:		http://sunshineinabag.co.uk/
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
NextStep-like icons and backgrounds. Contains a full set of original
mime-type icons.

%description -l pl.UTF-8
Ikony i tła w stylu NextStep. Zawiera pełny zestaw oryginalnych ikonek
dla różnych typów plików.

%prep
%setup -q -n NextStep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/NextStep

mv * $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/NextStep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/NextStep
