Summary:	A complete software to manage CD/DVD images rich of features
Name:		acetoneiso2
Version:	2.0.1
Release:	0.1
License:	GPL v3
######		Unknown group!
Group:		System/GUI/KDE
Source0:	http://dl.sourceforge.net/acetoneiso2/%{name}_%{version}-source.tar.gz
# Source0-md5:	ab7e77fdd5ca7f2407166338982ec819
URL:		http://www.acetoneteam.org
BuildRequires:	libqt4-sql >= 4.3.2
BuildRequires:	libqt4-devel >= 4.3.2
BuildRequires:	libqt4 >= 4.3.2
BuildRequires:	libqt4-qt3support >= 4.3.2
BuildRequires:	libqt4-x11 >= 4.3.2
BuildRequires:	update-desktop-files
BuildRequires:	glib2-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
Requires:	cdrdao
Requires:	p7zip
Requires:	gpg2
Requires:	pinentry-qt
Requires:	fuse
Requires:	fuseiso
Requires:	mkisofs
Requires:	cdrkit-cdrtools-compat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete software to manage CD/DVD images rich of features. In
example it can Mount typical proprietary images formats of the windows
world and do plenty of other things.

%prep
%setup -q -n %{name}

%build
cd src/
qmake
%{__make} %{?jobs:-j %jobs}

%install
rm -rf $RPM_BUILD_ROOT
cd src/
rpm -fr $RPM_BUILD_ROOT

%__make INSTALL_ROOT=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_desktopdir}/AcetoneISO.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README
%attr(755,root,root) %{_bindir}/acetoneiso2
%{_mydir}/isofolder
%{_mydir}/mfolder
%{_mydir}/smiso
%{_mydir}/ufolder
%{_desktopdir}/acetoneiso2.desktop
%{_pixmapsdir}/Acetino2.png
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-folder.desktop
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-iso.desktop
