Summary:	NextStep theme
Summary(pl):	Motyw NextStep
Name:		nautilus-theme-NextStep
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
#http://www.lucidus.uklinux.net/index.php?theme=nautilus&get=nextstep.tar.gz
Source0:	nautilus-nextstep.tar.gz
URL:		http://sunshineinabag.co.uk/
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
NextStep-like icons and backgrounds. Contains a full set of original
mime-type icons.

%description -l pl
Ikony i t³a w stylu NextStep. Zawiera pe³ny zestaw oryginalnych ikonek
dla ró¿nych typów plików.

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
