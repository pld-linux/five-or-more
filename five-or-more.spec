Summary:	"Five or more" game for GNOME
Summary(pl.UTF-8):	Gra "pięć lub więcej" dla GNOME
Name:		five-or-more
Version:	3.32.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/five-or-more/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	507e662de3fada6c058c411097add343
URL:		https://wiki.gnome.org/Apps/Five%20or%20more
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgnome-games-support-devel >= 1
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	meson >= 0.43.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	vala
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-librsvg >= 2.32.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.32
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.8
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/glib-2.0/schemas/org.gnome.five-or-more.gschema.xml
%{_datadir}/five-or-more
%{_datadir}/metainfo/org.gnome.five-or-more.appdata.xml
%{_desktopdir}/org.gnome.five-or-more.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.five-or-more.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.five-or-more-symbolic.svg
%{_mandir}/man6/five-or-more.6*
