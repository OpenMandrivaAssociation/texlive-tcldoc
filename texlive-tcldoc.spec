# revision 22018
# category Package
# catalog-ctan /macros/latex/contrib/tclldoc
# catalog-date 2007-02-28 00:02:05 +0100
# catalog-license lppl
# catalog-version 2.40
Name:		texlive-tcldoc
Version:	2.40
Release:	3
Summary:	Doc/docstrip for tcl
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tclldoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tclldoc package and class simplify the application of the
doc/docstrip style of literate programming with Dr. John
Ousterhout's Tool Command Language (Tcl, pronounced "tickle",
a.k.a. The Cool Language). The tclldoc package is a bit like
the doc package is for LaTeX, whereas the tclldoc class more
parallels the ltxdoc class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tcldoc/tcldoc.cls
%{_texmfdistdir}/tex/latex/tcldoc/tcldoc.sty
%{_texmfdistdir}/tex/latex/tcldoc/tclldoc.cls
%{_texmfdistdir}/tex/latex/tcldoc/tclldoc.sty
%doc %{_texmfdistdir}/doc/latex/tcldoc/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/parsetcl.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/parsetcl.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/pdf.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/pdf.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/tclldoc.pdf
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/eemenu.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/eemenu.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/sourcedtx.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/sourcedtx.ins
#- source
%doc %{_texmfdistdir}/source/latex/tcldoc/tclldoc.dtx
%doc %{_texmfdistdir}/source/latex/tcldoc/tclldoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.40-2
+ Revision: 756515
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.40-1
+ Revision: 719659
- texlive-tcldoc
- texlive-tcldoc
- texlive-tcldoc

