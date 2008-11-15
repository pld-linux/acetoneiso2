Summary:	A complete software to manage CD/DVD images rich of features
Summary(pl.UTF-8):	Kompletne oprogramowanie o dużych możliwościach do zarządzania obrazami CD/DVD
Name:		acetoneiso2
Version:	2.0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications/File
Source0:	http://dl.sourceforge.net/acetoneiso2/%{name}_%{version}-source.tar.gz
# Source0-md5:	ab7e77fdd5ca7f2407166338982ec819
URL:		http://www.acetoneteam.org/
BuildRequires:	Qt3Support-devel >= 4.3.2
BuildRequires:	QtGui-devel >= 4.3.2
BuildRequires:	QtSql-devel >= 4.3.2
BuildRequires:	glib2-devel
BuildRequires:	qt4-build >= 4.3.2
BuildRequires:	qt4-devel >= 4.3.2
BuildRequires:	qt4-qmake >= 4.3.2
BuildRequires:	libstdc++-devel
Requires:	cdrdao
Requires:	cdrkit-cdrtools-compat
Requires:	fuse
Requires:	fuseiso
Requires:	gnupg2
Requires:	mkisofs
Requires:	p7zip
Requires:	pinentry-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete software to manage CD/DVD images rich of features. In
example it can mount typical proprietary images formats of the Windows
world and do plenty of other things.

%description -l pl.UTF-8
Kompletne oprogramowanie o dużych możliwościach do zarządzania
obrazami CD/DVD. Potrafi na przykład montować typowe własnościowe
formaty obrazów spotykane w świecie Windows i wykonywać wiele innych
czynności.

%prep
%setup -q -n %{name}

%build
cd src
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_desktopdir}/AcetoneISO.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README
%attr(755,root,root) %{_bindir}/acetoneiso2
# XXX: FIXME
/opt/acetoneiso/isofolder
/opt/acetoneiso/mfolder
/opt/acetoneiso/smiso
/opt/acetoneiso/ufolder
%{_desktopdir}/acetoneiso2.desktop
%{_pixmapsdir}/Acetino2.png
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-folder.desktop
%{_datadir}/apps/konqueror/servicemenus/acetoneiso2-iso.desktop
