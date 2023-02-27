%define oname Workbench
Name:           workbench
Version:        43.3
Release:        1
Summary:        Learn and prototype with GNOME technologies
License:        GPL-3.0-or-later
URL:            https://github.com/sonnyp/Workbench
Source0:        https://github.com/sonnyp/Workbench/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  appstream-util
BuildRequires:  appstream
BuildRequires:  gjs
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  python-blueprint-compiler

%description
Workbench goal is to let you experiment with GNOME technologies, no matter if tinkering for the first time or building and testing a GTK user interface.
Among other things, Workbench comes with realtime GTK/CSS preview library of examples
- 1000+ icons
- JavaScript and Vala support
- XML and Blueprint for describing user interface
- syntax highlighting, undo/redo, autosave, session restore
- code formatter
- console logs

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
  
%files
