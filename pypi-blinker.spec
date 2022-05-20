#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-blinker
Version  : 1.4
Release  : 48
URL      : https://files.pythonhosted.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz
Summary  : Fast, simple object-to-object and broadcast signaling
Group    : Development/Tools
License  : MIT
Requires: pypi-blinker-license = %{version}-%{release}
Requires: pypi-blinker-python = %{version}-%{release}
Requires: pypi-blinker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Blinker
        
        Blinker provides a fast dispatching system that allows any number of
        interested parties to subscribe to events, or "signals".
        
        Signal receivers can subscribe to specific senders or receive signals
        sent by any sender.
        
            >>> from blinker import signal
            >>> started = signal('round-started')

%package license
Summary: license components for the pypi-blinker package.
Group: Default

%description license
license components for the pypi-blinker package.


%package python
Summary: python components for the pypi-blinker package.
Group: Default
Requires: pypi-blinker-python3 = %{version}-%{release}

%description python
python components for the pypi-blinker package.


%package python3
Summary: python3 components for the pypi-blinker package.
Group: Default
Requires: python3-core
Provides: pypi(blinker)

%description python3
python3 components for the pypi-blinker package.


%prep
%setup -q -n blinker-1.4
cd %{_builddir}/blinker-1.4
pushd ..
cp -a blinker-1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653006243
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-blinker
cp %{_builddir}/blinker-1.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-blinker/15f4d259a18581c81f42f3dd47da3f66e2a72e1c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-blinker/15f4d259a18581c81f42f3dd47da3f66e2a72e1c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
