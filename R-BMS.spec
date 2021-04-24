#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BMS
Version  : 0.3.4
Release  : 23
URL      : https://cran.r-project.org/src/contrib/BMS_0.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BMS_0.3.4.tar.gz
Summary  : Bayesian Model Averaging Library
Group    : Development/Tools
License  : Artistic-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n BMS
cd %{_builddir}/BMS

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589514556

%install
export SOURCE_DATE_EPOCH=1589514556
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMS
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc BMS || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BMS/CITATION
/usr/lib64/R/library/BMS/DESCRIPTION
/usr/lib64/R/library/BMS/INDEX
/usr/lib64/R/library/BMS/Meta/Rd.rds
/usr/lib64/R/library/BMS/Meta/data.rds
/usr/lib64/R/library/BMS/Meta/demo.rds
/usr/lib64/R/library/BMS/Meta/features.rds
/usr/lib64/R/library/BMS/Meta/hsearch.rds
/usr/lib64/R/library/BMS/Meta/links.rds
/usr/lib64/R/library/BMS/Meta/nsInfo.rds
/usr/lib64/R/library/BMS/Meta/package.rds
/usr/lib64/R/library/BMS/Meta/vignette.rds
/usr/lib64/R/library/BMS/NAMESPACE
/usr/lib64/R/library/BMS/NEWS
/usr/lib64/R/library/BMS/R/BMS
/usr/lib64/R/library/BMS/R/BMS.rdb
/usr/lib64/R/library/BMS/R/BMS.rdx
/usr/lib64/R/library/BMS/data/datafls.rda
/usr/lib64/R/library/BMS/demo/BMS.growth.R
/usr/lib64/R/library/BMS/doc/bmasmall.bib
/usr/lib64/R/library/BMS/doc/bms.R
/usr/lib64/R/library/BMS/doc/bms.Rnw
/usr/lib64/R/library/BMS/doc/bms.pdf
/usr/lib64/R/library/BMS/doc/index.html
/usr/lib64/R/library/BMS/help/AnIndex
/usr/lib64/R/library/BMS/help/BMS.rdb
/usr/lib64/R/library/BMS/help/BMS.rdx
/usr/lib64/R/library/BMS/help/aliases.rds
/usr/lib64/R/library/BMS/help/paths.rds
/usr/lib64/R/library/BMS/html/00Index.html
/usr/lib64/R/library/BMS/html/R.css
