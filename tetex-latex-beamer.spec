%define	short_name	beamer
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
#
Summary:	A LaTeX class for producing beamer presentations
Summary(pl.UTF-8):   Klasa LaTeXa do tworzenia prezentacji rzutnikowych
Name:		tetex-latex-beamer
Version:	3.06
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/latex-beamer-%{version}.tar.gz
# Source0-md5:	ab7eeb972d75e758117460aabdddb1e6
URL:		http://latex-beamer.sourceforge.net/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires:	tetex-pgf >= 0.95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A LaTeX class for producing beamer presentations.

%description -l pl.UTF-8
Klasa LaTeXa do tworzenia prezentacji rzutnikowych.

%package examples
Summary:	Example presentations created using the LaTeX Beamer class
Summary(pl.UTF-8):   Przykładowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}

%description examples
Example presentations created using the LaTeX Beamer class.

%description examples -l pl.UTF-8
Przykładowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer.

%package lyx
Summary:	LyX templates for the LaTeX Beamer class
Summary(pl.UTF-8):   Szablony klasy LateX Beamer dla programu LyX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}
Requires:	lyx

%description lyx
LyX templates for the LaTeX Beamer class.

%description lyx -l pl.UTF-8
Szablony klasy LateX Beamer dla programu LyX.

%package emacs
Summary:	Emacs mode for the LaTeX Beamer class
Summary(pl.UTF-8):   Emacsowy tryb edycji plików LaTeX z klasą Beamer
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}
Requires:	emacs-common

%description emacs
Emacs mode for the LaTeX Beamer class.

%description emacs -l pl.UTF-8
Emacsowy tryb edycji plików źródłowych LaTeXa znający klasę Beamer.

%prep
%setup -q -n latex-%{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/tex/latex/%{short_name},%{_examplesdir}/%{name}-%{version}}
install -d $RPM_BUILD_ROOT%{_datadir}/lyx/{layouts,templates}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/lyx
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d

cp -a base emulation extensions themes $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

cp -a examples/* solutions $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/solutions/*/*.lyx $RPM_BUILD_ROOT%{_datadir}/lyx/templates
cp -a lyx/layouts/beamer.layout $RPM_BUILD_ROOT%{_datadir}/lyx/layouts
cp -a lyx/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/lyx

cp -a emacs/beamer.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d

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
%{_datadir}/lyx/layouts/beamer.layout
%{_datadir}/lyx/templates/*

%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/site-start.d/*
