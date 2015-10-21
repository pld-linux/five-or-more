Summary:	"Five or more" game for GNOME
Summary(pl.UTF-8):	Gra "pięć lub więcej" dla GNOME
Name:		five-or-more
Version:	3.18.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/five-or-more/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	f2f6fe100d49a4b9ba75d99675e4dc03
URL:		https://wiki.gnome.org/Apps/Five%20or%20more
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gnome-common
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool >= 0.50
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.12.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-glines = 1:%{version}-%{release}
Obsoletes:	gnome-games-glines < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Five-or-more is a GNOME port of a once-popular computer game. Align
five or more objects of the same color into a line to cause them to
disappear and score points.

%description -l pl.UTF-8
Five-or-more to port GNOME popularnej niegdyś gry komputerowej. Celem
jest wyrównanie w rzędzie pięciu lub większej liczby obiektów jednego
koloru, co powoduje zniknięcie ich i zdobycie punktów.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/five-or-more
%{_datadir}/appdata/five-or-more.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.five-or-more.gschema.xml
%{_datadir}/five-or-more
%{_desktopdir}/five-or-more.desktop
%{_iconsdir}/hicolor/*x*/apps/five-or-more.png
%{_iconsdir}/hicolor/scalable/apps/five-or-more.svg
%{_iconsdir}/hicolor/scalable/apps/five-or-more-symbolic.svg
%{_mandir}/man6/five-or-more.6*
