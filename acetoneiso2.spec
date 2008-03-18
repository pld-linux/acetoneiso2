Summary:	A complete software to manage CD/DVD images rich of features
Name:		acetoneiso2
Version:	2.0.1
Release:	0.1
License:	GPL v3
Group:		System/GUI/KDE
Source0:	http://dl.sourceforge.net/acetoneiso2/%{name}_%{version}-source.tar.gz
# Source0-md5:	ab7e77fdd5ca7f2407166338982ec819
URL:		http://www.acetoneteam.org
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	libqt4 >= 4.3.2
BuildRequires:	libqt4-devel >= 4.3.2
BuildRequires:	libqt4-qt3support >= 4.3.2
BuildRequires:	libqt4-sql >= 4.3.2
BuildRequires:	libqt4-x11 >= 4.3.2
BuildRequires:	libstdc++-devel
BuildRequires:	update-desktop-files
Requires:	cdrdao
Requires:	cdrkit-cdrtools-compat
Requires:	fuse
Requires:	fuseiso
Requires:	gpg2
Requires:	mkisofs
Requires:	p7zip
Requires:	pinentry-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete software to manage CD/DVD images rich of features. In
example it can Mount typical proprietary images formats of the windows
world and do plenty of other things.

%prep
%setup -q -n %{name}

%build
cd src
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd src

%{__make} -C src install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_desktopdir}/AcetoneISO.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README
%attr(755,root,root) %{_bindir}/acetoneiso2
/opt/acetoneiso/isofolder
/opt/acetoneiso/mfolder
/opt/acetoneiso/smiso
/opt/acetoneiso/ufolder
%{_desktopdir}/acetoneiso2.desktop
%{_pixmapsdir}/Acetino2.png
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-folder.desktop
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-iso.desktop
