# generated by cabal-rpm-2.0.9
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name text-short
%global pkgver %{pkg_name}-%{version}

# testsuite missing deps: quickcheck-instances

Name:           ghc-%{pkg_name}
Version:        0.1.3
Release:        6%{?dist}
Summary:        Memory-efficient representation of Unicode text strings

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-text-prof
# End cabal-rpm deps

%description
This package provides the 'ShortText' type which is suitable for keeping many
short strings in memory. This is similiar to how 'ShortByteString' relates to
'ByteString'.

The main difference between 'Text' and 'ShortText' is that 'ShortText' uses
UTF-8 instead of UTF-16 internally and also doesn't support zero-copy slicing
(thereby saving 2 words). Consequently, the memory footprint of a (boxed)
'ShortText' value is 4 words (2 words when unboxed) plus the length of the
UTF-8 encoded payload.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.1.3-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.1.3-1
- update to 0.1.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.1.2-7
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.1.2-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.1.2-3
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-1
- update to 0.1.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.1.1-2
- rebuild

* Sat Nov 18 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.1-1
- spec file generated by cabal-rpm-0.11.2
