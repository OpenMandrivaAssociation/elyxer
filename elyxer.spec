# Spec is based on Cristobal Lopez's work in MIB
# and Damir Shayhutdinov's work in ALT Linux

Name:		elyxer
Version:	1.2.5
Release:	1
Summary:	Convert LyX source files to HTML output
License:	GPLv3
Group:		Text tools
URL:		https://www.nongnu.org/elyxer/
Source0:	http://download.savannah.gnu.org/releases-noredirect/%{name}/%{name}-%{version}.tar.gz
Source1:	elyxer.1
Source2:	loremipsumize.1
BuildRequires:	python-devel
BuildRequires:	gettext-devel
BuildRequires:	pygtk2.0-devel
Requires:	pygtk2.0 >= 2.10
Requires:	gettext
Requires:	python
BuildArch:	noarch

%description
eLyXer converts a LyX source file to a HTML page. Full documentation in HTML
format can be found at docs/index.html, or on the web:
http://www.nongnu.org/elyxer/

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --install-lib=%{py_puresitedir}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/locale
cp -rf ./po/locale/* %{buildroot}%{_datadir}/locale

mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE1} %{SOURCE2} %{buildroot}%{_mandir}/man1/

for i in %{buildroot}%{_bindir}/*.py; do
mv $i %{buildroot}%{_bindir}/`basename $i .py`
done

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{py_puresitedir}/*.egg-info
%{_mandir}/man1/*
