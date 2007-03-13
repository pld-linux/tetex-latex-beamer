%define	short_name	beamer
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
#
Summary:	A LaTeX class for producing beamer presentations
Summary(pl.UTF-8):	Klasa LaTeXa do tworzenia prezentacji rzutnikowych
Name:		tetex-latex-beamer
Version:	3.07
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/latex-beamer-%{version}.tar.gz
# Source0-md5:	a908b9fa5c98b1e1ef49bda302dd2af6
URL:		http://latex-beamer.sourceforge.net/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires:	tetex-pgf >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A LaTeX class for producing beamer presentations.

%description -l pl.UTF-8
Klasa LaTeXa do tworzenia prezentacji rzutnikowych.

%package examples
Summary:	Example presentations created using the LaTeX Beamer class
Summary(pl.UTF-8):	Przykładowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}

%description examples
Example presentations created using the LaTeX Beamer class.

%description examples -l pl.UTF-8
Przykładowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer.

%package lyx
Summary:	LyX templates for the LaTeX Beamer class
Summary(pl.UTF-8):	Szablony klasy LateX Beamer dla programu LyX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}
Requires:	lyx

%description lyx
LyX templates for the LaTeX Beamer class.

%description lyx -l pl.UTF-8
Szablony klasy LateX Beamer dla programu LyX.

%prep
%setup -q -n latex-%{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/tex/latex/%{short_name},%{_examplesdir}/%{name}-%{version}}
install -d $RPM_BUILD_ROOT%{_datadir}/lyx/templates
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/lyx

cp -a base emulation extensions themes $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

cp -a examples/* solutions $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/solutions/*/*.lyx $RPM_BUILD_ROOT%{_datadir}/lyx/templates

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/*.pdf README TODO
%{_datadir}/texmf/tex/latex/%{short_name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files lyx
%defattr(644,root,root,755)
%{_datadir}/lyx/templates/*
