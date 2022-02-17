Name: python3
Summary: Interpreter of the Python3 programming language
URL: https://www.python.org/

Version: 3.7.9
Release: 19
License: Python

%global branchversion 3.7
%global pyshortver 37

%ifarch %{ix86} x86_64
%bcond_with optimizations
%else
%bcond_with optimizations
%endif

%global pylibdir %{_libdir}/python%{branchversion}
%global dynload_dir %{pylibdir}/lib-dynload

# See  http://www.python.org/dev/peps/pep-3149/
%global ABIFLAGS_optimized m
%global ABIFLAGS_debug     dm

%global LDVERSION_optimized %{branchversion}m
%global LDVERSION_debug     %{branchversion}dm

%global SOABI_optimized cpython-%{pyshortver}m-%{_arch}-linux%{_gnu}
%global SOABI_debug     cpython-%{pyshortver}dm-%{_arch}-linux%{_gnu}

# See  http://www.python.org/dev/peps/pep-3147/
%global bytecode_suffixes .cpython-%{pyshortver}*.pyc

%global py_INSTSONAME_optimized libpython%{LDVERSION_optimized}.so.1.0
%global py_INSTSONAME_debug     libpython%{LDVERSION_debug}.so.1.0

%undefine py_auto_byte_compile

%global wordsize 64

BuildRequires: autoconf
BuildRequires: bluez-libs-devel
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel

BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: glibc-all-langpacks
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: libappstream-glib
BuildRequires: libffi-devel
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: libGL-devel
BuildRequires: libuuid-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel

BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: system-rpm-config
BuildRequires: sqlite-devel
BuildRequires: gdb

BuildRequires: tar
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel

BuildRequires: valgrind-devel

BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: systemtap-sdt-devel

BuildRequires: net-tools

BuildRequires: python-setuptools-wheel
BuildRequires: python-pip-wheel

Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz
Source1: pyconfig.h

Patch1:   00001-rpath.patch
Patch102: 00102-lib64.patch
Patch111: 00111-no-static-lib.patch
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch
Patch155: 00155-avoid-ctypes-thunks.patch
Patch160: 00160-disable-test_fs_holes-in-rpm-build.patch
Patch170: 00170-gc-assertions.patch
Patch178: 00178-dont-duplicate-flags-in-sysconfig.patch
Patch189: 00189-use-rpm-wheels.patch
Patch205: 00205-make-libpl-respect-lib64.patch
Patch251: 00251-change-user-install-location.patch
Patch316: 00316-mark-bdist_wininst-unsupported.patch
Patch317: CVE-2019-17514.patch
Patch318: CVE-2019-9674.patch
Patch319: python3-add-generic-os-support.patch
Patch320: CVE-2020-27619.patch

Patch6000: CVE-2021-3177.patch
Patch6001: backport-CVE-2021-23336.patch

Patch6003:  backport-20104-Expose-posix_spawn-in-the-os-module-GH-510.patch
Patch6004:  backport-20104-Fix-leaks-and-errors-in-new-os.posix_spawn.patch
Patch6005:  backport-20104-Improve-error-handling-and-fix-a-reference.patch
Patch6006:  backport-33630-Fix-using-of-freed-memory-in-old-versions-.patch
Patch6007:  backport-33332-Add-signal.valid_signals-GH-6581.patch
Patch6008:  backport-33441-Make-the-sigset_t-converter-available-in-o.patch
Patch6009:  backport-20104-Add-flag-capabilities-to-posix_spawn-GH-66.patch
Patch6010:  backport-33455-Pass-os.environ-in-test_posix-test_specify.patch
Patch6011:  backport-Fix-TestPosixSpawn.test_close_file-GH-8992.patch
Patch6012:  backport-20104-Change-the-file_actions-parameter-of-os.po.patch
Patch6013:  backport-35537-subprocess-uses-os.posix_spawn-in-some-cas.patch
Patch6014:  backport-35674-Add-os.posix_spawnp-GH-11554.patch
Patch6015:  backport-35537-subprocess-can-use-posix_spawn-with-pipes-.patch
Patch6016:  backport-subprocess-close-pipes-fds-by-using-ExitStack-GH-116.patch
Patch6017:  backport-34862-Guard-definition-of-convert_sched_p.patch
Patch6018:  backport-35537-Add-setsid-parameter-to-os.posix_spawn-and.patch
Patch6019:  backport-35537-Skip-test_start_new_session-of-posix_spawn.patch
Patch6020:  backport-35537-Fix-function-name-in-os.posix_spawnp-error.patch
Patch6021:  backport-36814-ensure-os.posix_spawn-handles-None-GH-1314.patch
Patch6022:  backport-35537-Rewrite-setsid-test-for-os.posix_spawn-GH-.patch
Patch6023:  backport-36046-Add-user-and-group-parameters-to-subproces.patch
Patch6024:  backport-36046-Fix-buildbot-failures-GH-16091.patch
Patch6025:  backport-36046-posix_spawn-doesn-t-support-uid-gid-GH-163.patch
Patch6026:  backport-38417-Add-umask-support-to-subprocess-GH-16726.patch
Patch6027:  backport-38456-Use-bin-true-in-test_subprocess-GH-16736.patch
Patch6028:  backport-38456-Handle-the-case-when-there-is-no-true-comm.patch
Patch6029:  backport-39855-Fix-test_subprocess-if-nobody-user-doesn-t.patch
Patch6030:  backport-35823-subprocess-Use-vfork-instead-of-fork-on-Li.patch
Patch6031:  backport-35823-subprocess-Fix-handling-of-pthread_sigmask.patch
Patch6032:  backport-35823-Allow-setsid-after-vfork-on-Linux.-GH-2294.patch
Patch6033:  backport-42146-Fix-memory-leak-in-subprocess.Popen-in-cas.patch
Patch6034:  backport-42146-Unify-cleanup-in-subprocess_fork_exec-GH-2.patch
patch6035:  backport-Remove-thread-objects-which-finished-process-its-request.patch
patch6036:  backport-CVE-2021-3426.patch
patch6037:  backport-32494-Use-gdbm_count-for-dbm_length-if-possible.patch

Patch6038:  backport-36333-36356-Fix-_PyEval_FiniThreads-GH-12432.patch
Patch6039:  backport-37169-Rewrite-_PyObject_IsFreed-unit-tests-GH-13.patch
Patch6040:  backport-44363-Get-test_capi-passing-with-address-sanitiz.patch
Patch6041:  backport-36253-Remove-use-after-free-reference-in-ctypes-.patch
Patch6042:  backport-36356-Fix-memory-leak-in-_asynciomodule.c-GH-165.patch
Patch6043:  backport-CVE-2021-3733.patch
Patch6044:  backport-CVE-2021-3737.patch
Patch6045:  backport-bpo-44022-Improve-the-regression-test.patch

patch9000:  Don-t-override-PYTHONPATH-which-is-already-set.patch
patch9001:  add-the-sm3-method-for-obtaining-the-salt-value.patch

Recommends: %{name}-help = %{version}-%{release}
Provides: python%{branchversion} = %{version}-%{release}
Provides: python(abi) = %{branchversion}

Provides: python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver}

Requires: python-setuptools-wheel
Requires: python-pip-wheel
Provides: python3-libs
Obsoletes: python3-libs
Provides: python3-enum34 = 1.0.4-5
Obsoletes: python3-enum34 < 1.0.4-5

Recommends: python3-setuptools
Recommends: python3-pip

%global __requires_exclude ^/usr/bin/python3

%description
Python combines remarkable power with very clear syntax. It has modules,
classes, exceptions, very high level dynamic data types, and dynamic
typing. There are interfaces to many system calls and libraries, as well
as to various windowing systems. New built-in modules are easily written
in C or C++ (or other languages, depending on the chosen implementation).
Python is also usable as an extension language for applications written
in other languages that need easy-to-use scripting or automation interfaces.

This package Provides python version 3.

%package devel
Summary: Libraries and header files needed for Python development
Requires: %{name} = %{version}-%{release}
BuildRequires: python-rpm-macros
Requires: python-rpm-macros
Requires: python3-rpm-macros
Requires: python3-rpm-generators
Requires: python3-setuptools
Provides: %{name}-2to3 = %{version}-%{release}
Provides: 2to3 = %{version}-%{release}
Conflicts: %{name} < %{version}-%{release}
Provides: python3-idle
Obsoletes: python3-idle
Provides: python3-test
Obsoletes: python3-test
Provides: python3-tkinter
Obsoletes: python3-tkinter
Provides: %{name}-tools = %{version}-%{release}
Obsoletes: %{name}-tools < %{version}-%{release}

%description devel
This package contains the header files and configuration needed to develop
python3 modules.

%package debug
Summary: Debug version of the Python runtime

Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}

%description debug
python3-debug provides a version of the Python runtime with numerous debugging
features enabled, aimed at advanced Python users such as developers of Python
extension modules.

%package_help

%prep
%setup -q -n Python-%{version}
find -name '*.exe' -print -delete
rm -r Modules/expat

%patch1 -p1
%patch102 -p1
%patch111 -p1
%patch132 -p1
%patch155 -p1
%patch160 -p1
%patch170 -p1
%patch178 -p1

%patch189 -p1
rm Lib/ensurepip/_bundled/*.whl
%patch205 -p1
%patch251 -p1
%patch316 -p1
%patch317 -p1
%patch318 -p1
%patch319 -p1
%patch320 -p1
%patch6000 -p1
%patch6001 -p1

%patch6003 -p1
%patch6004 -p1
%patch6005 -p1
%patch6006 -p1
%patch6007 -p1
%patch6008 -p1
%patch6009 -p1
%patch6010 -p1
%patch6011 -p1
%patch6012 -p1
%patch6013 -p1
%patch6014 -p1
%patch6015 -p1
%patch6016 -p1
%patch6017 -p1
%patch6018 -p1
%patch6019 -p1
%patch6020 -p1
%patch6021 -p1
%patch6022 -p1
%patch6023 -p1
%patch6024 -p1
%patch6025 -p1
%patch6026 -p1
%patch6027 -p1
%patch6028 -p1
%patch6029 -p1
%patch6030 -p1
%patch6031 -p1
%patch6032 -p1
%patch6033 -p1
%patch6034 -p1
%patch6035 -p1
%patch6036 -p1
%patch6037 -p1
%patch6038 -p1
%patch6039 -p1
%patch6040 -p1
%patch6041 -p1
%patch6042 -p1
%patch6043 -p1
%patch6044 -p1
%patch6045 -p1
%patch9000 -p1
%patch9001 -p1

sed -i "s/generic_os/%{_vendor}/g" Lib/platform.py
rm configure pyconfig.h.in

%build
autoconf
autoheader

topdir=$(pwd)

%if %{with optimizations}
%global optimizations_flag "--enable-optimizations"
%else
%global optimizations_flag "--disable-optimizations"
%endif

%global extension_cflags ""
%global extension_ldflags ""

export CFLAGS="%{extension_cflags} -D_GNU_SOURCE -fPIC -fwrapv"
export CFLAGS_NODIST="%{build_cflags} -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="%{extension_cxxflags} -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="$(pkg-config --cflags-only-I libffi)"
export OPT="%{extension_cflags} -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
export CFLAGS="$CFLAGS $(pkg-config --cflags openssl)"
export LDFLAGS="%{extension_ldflags} -g $(pkg-config --libs-only-L openssl)"
export LDFLAGS_NODIST="%{build_ldflags} -g $(pkg-config --libs-only-L openssl)"

DebugBuildDir=build/debug
mkdir -p ${DebugBuildDir}
pushd ${DebugBuildDir}

%global _configure $topdir/configure

%configure \
  --enable-ipv6 \
  --enable-shared \
  --with-computed-gotos=yes \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
  --enable-loadable-sqlite-extensions \
  --with-dtrace \
  --with-ssl-default-suites=openssl \
  --with-valgrind \
  --without-ensurepip \
  --with-pydebug

%make_build EXTRA_CFLAGS="$CFLAGS -Og"

popd

OptimizedBuildDir=build/optimized
mkdir -p ${OptimizedBuildDir}
pushd ${OptimizedBuildDir}

%global _configure $topdir/configure

%configure \
  --enable-ipv6 \
  --enable-shared \
  --with-computed-gotos=yes \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
  --enable-loadable-sqlite-extensions \
  --with-dtrace \
  --with-ssl-default-suites=openssl \
  --with-valgrind \
  --without-ensurepip \
  %{optimizations_flag}

%make_build EXTRA_CFLAGS="$CFLAGS"

popd

%install

topdir=$(pwd)

DirHoldingGdbPy=%{_prefix}/lib/debug/%{_libdir}
mkdir -p %{buildroot}$DirHoldingGdbPy

%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h
%global _pyconfig_h pyconfig-%{wordsize}.h

DebugBuildDir=build/debug
mkdir -p ${DebugBuildDir}
pushd ${DebugBuildDir}
make DESTDIR=%{buildroot} INSTALL="install -p" EXTRA_CFLAGS="-O0" install
popd

PathOfGdbPy=$DirHoldingGdbPy/%{py_INSTSONAME_debug}-%{version}-%{release}.%{_arch}.debug-gdb.py
cp Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy

mv %{buildroot}%{_bindir}/python%{LDVERSION_debug}-{,`uname -m`-}config
echo -e '#!/bin/sh\nexec `dirname $0`/python'%{LDVERSION_debug}'-`uname -m`-config "$@"' > \
  %{buildroot}%{_bindir}/python%{LDVERSION_debug}-config
echo '[ $? -eq 127 ] && echo "Could not find python'%{LDVERSION_debug}'-`uname -m`-config. Look around to see available arches." >&2' >> \
  %{buildroot}%{_bindir}/python%{LDVERSION_debug}-config
  chmod +x %{buildroot}%{_bindir}/python%{LDVERSION_debug}-config

mv %{buildroot}%{_includedir}/python%{LDVERSION_debug}/pyconfig.h \
   %{buildroot}%{_includedir}/python%{LDVERSION_debug}/%{_pyconfig_h}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_includedir}/python%{LDVERSION_debug}/pyconfig.h

OptimizedBuildDir=build/optimized
mkdir -p ${OptimizedBuildDir}
pushd ${OptimizedBuildDir}
make DESTDIR=%{buildroot} INSTALL="install -p" EXTRA_CFLAGS="" install
popd

PathOfGdbPy=$DirHoldingGdbPy/%{py_INSTSONAME_optimized}-%{version}-%{release}.%{_arch}.debug-gdb.py
cp Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy

mv %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-{,`uname -m`-}config
echo -e '#!/bin/sh\nexec `dirname $0`/python'%{LDVERSION_optimized}'-`uname -m`-config "$@"' > \
  %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config
echo '[ $? -eq 127 ] && echo "Could not find python'%{LDVERSION_optimized}'-`uname -m`-config. Look around to see available arches." >&2' >> \
  %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config
  chmod +x %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config

mv %{buildroot}%{_includedir}/python%{LDVERSION_optimized}/pyconfig.h \
   %{buildroot}%{_includedir}/python%{LDVERSION_optimized}/%{_pyconfig_h}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_includedir}/python%{LDVERSION_optimized}/pyconfig.h
install -d -m 0755 %{buildroot}%{pylibdir}/site-packages/__pycache__
install -d -m 0755 %{buildroot}%{_prefix}/lib/python%{branchversion}/site-packages/__pycache__

install -D -m 0644 Lib/idlelib/Icons/idle_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/idle3.png
install -D -m 0644 Lib/idlelib/Icons/idle_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/idle3.png
install -D -m 0644 Lib/idlelib/Icons/idle_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/idle3.png

sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
  %{buildroot}%{pylibdir}/sysconfig.py

cp -p Tools/scripts/pathfix.py %{buildroot}%{_bindir}/

for tool in pygettext msgfmt; do
  cp -p Tools/i18n/${tool}.py %{buildroot}%{_bindir}/${tool}%{branchversion}.py
  ln -s ${tool}%{branchversion}.py %{buildroot}%{_bindir}/${tool}3.py
done

LD_LIBRARY_PATH=./build/optimized ./build/optimized/python \
  Tools/scripts/pathfix.py \
  -i "%{_bindir}/python%{branchversion}" -pn \
  %{buildroot} \
  %{buildroot}%{_bindir}/*%{branchversion}.py \
  %{?with_gdb_hooks:%{buildroot}$DirHoldingGdbPy/*.py}

rm -rf %{buildroot}%{pylibdir}/test/test_tools

find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

find %{buildroot} -name \*.bat -exec rm {} \;

find %{buildroot}/ -name "*~" -exec rm -f {} \;
find . -name "*~" -exec rm -f {} \;

rm %{buildroot}%{pylibdir}/LICENSE.txt

find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{branchversion} %{buildroot}%{_libdir}/python%{branchversion}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{branchversion} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2], optimize=opt) for opt in range(3) for f in sys.argv[1:]]' || :

rm -rf %{buildroot}%{_bindir}/__pycache__

find %{buildroot} -perm 555 -exec chmod 755 {} \;

ln -s \
  %{_bindir}/python%{LDVERSION_debug} \
  %{buildroot}%{_bindir}/python3-debug

mv %{buildroot}%{_bindir}/2to3-%{branchversion} %{buildroot}%{_bindir}/2to3

%check
topdir=$(pwd)

BEP_WHITELIST_TMP="$BEP_WHITELIST"
BEP_GTDLIST_TMP="$BEP_GTDLIST"
export BEP_WHITELIST="python python-debug "$BEP_WHITELIST""
export BEP_GTDLIST=`echo $BEP_GTDLIST | sed 's/ python / /g'`

export OPENSSL_CONF=/non-existing-file

LD_LIBRARY_PATH=$(pwd)/build/debug $(pwd)/build/debug/python -m test.pythoninfo

WITHIN_PYTHON_RPM_BUILD= \
LD_LIBRARY_PATH=$(pwd)/build/debug $(pwd)/build/debug/python -m test.regrtest \
    -wW --slowest -j0 \
    -x test_distutils \
    -x test_bdist_rpm \
    -x test_gdb \
    -x test_socket \
    -x test_asyncio

export OPENSSL_CONF=/non-existing-file

LD_LIBRARY_PATH=$(pwd)/build/optimized $(pwd)/build/optimized/python -m test.pythoninfo

WITHIN_PYTHON_RPM_BUILD= \
LD_LIBRARY_PATH=$(pwd)/build/optimized $(pwd)/build/optimized/python -m test.regrtest \
    -wW --slowest -j0 \
    -x test_distutils \
    -x test_bdist_rpm \
    -x test_gdb \
    -x test_socket \
    -x test_asyncio

export BEP_WHITELIST="$BEP_WHITELIST_TMP"
export BEP_GTDLIST="$BEP_GTDLIST_TMP"

%files
%license LICENSE
%doc README.rst

%{_bindir}/pydoc*
%{_bindir}/python3
%{_bindir}/pyvenv

%{_bindir}/python%{branchversion}
%{_bindir}/python%{branchversion}m
%{_bindir}/pyvenv-%{branchversion}

%dir %{pylibdir}
%dir %{dynload_dir}

%{pylibdir}/lib2to3
%exclude %{pylibdir}/lib2to3/tests

%dir %{pylibdir}/unittest/
%dir %{pylibdir}/unittest/__pycache__/
%{pylibdir}/unittest/*.py
%{pylibdir}/unittest/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/asyncio/
%dir %{pylibdir}/asyncio/__pycache__/
%{pylibdir}/asyncio/*.py
%{pylibdir}/asyncio/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/venv/
%dir %{pylibdir}/venv/__pycache__/
%{pylibdir}/venv/*.py
%{pylibdir}/venv/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/venv/scripts

%{pylibdir}/wsgiref
%{pylibdir}/xmlrpc

%dir %{pylibdir}/ensurepip/
%dir %{pylibdir}/ensurepip/__pycache__/
%{pylibdir}/ensurepip/*.py
%{pylibdir}/ensurepip/__pycache__/*%{bytecode_suffixes}

%exclude %{pylibdir}/ensurepip/_bundled

%dir %{pylibdir}/test/
%dir %{pylibdir}/test/__pycache__/
%dir %{pylibdir}/test/support/
%dir %{pylibdir}/test/support/__pycache__/
%{pylibdir}/test/__init__.py
%{pylibdir}/test/__pycache__/__init__%{bytecode_suffixes}
%{pylibdir}/test/support/*.py
%{pylibdir}/test/support/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/concurrent/
%dir %{pylibdir}/concurrent/__pycache__/
%{pylibdir}/concurrent/*.py
%{pylibdir}/concurrent/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/concurrent/futures/
%dir %{pylibdir}/concurrent/futures/__pycache__/
%{pylibdir}/concurrent/futures/*.py
%{pylibdir}/concurrent/futures/__pycache__/*%{bytecode_suffixes}

%{pylibdir}/pydoc_data

%{dynload_dir}/_blake2.%{SOABI_optimized}.so
%{dynload_dir}/_md5.%{SOABI_optimized}.so
%{dynload_dir}/_sha1.%{SOABI_optimized}.so
%{dynload_dir}/_sha256.%{SOABI_optimized}.so
%{dynload_dir}/_sha3.%{SOABI_optimized}.so
%{dynload_dir}/_sha512.%{SOABI_optimized}.so

%{dynload_dir}/_asyncio.%{SOABI_optimized}.so
%{dynload_dir}/_bisect.%{SOABI_optimized}.so
%{dynload_dir}/_bz2.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_cn.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_hk.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_iso2022.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_jp.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_kr.%{SOABI_optimized}.so
%{dynload_dir}/_codecs_tw.%{SOABI_optimized}.so
%{dynload_dir}/_contextvars.%{SOABI_optimized}.so
%{dynload_dir}/_crypt.%{SOABI_optimized}.so
%{dynload_dir}/_csv.%{SOABI_optimized}.so
%{dynload_dir}/_ctypes.%{SOABI_optimized}.so
%{dynload_dir}/_curses.%{SOABI_optimized}.so
%{dynload_dir}/_curses_panel.%{SOABI_optimized}.so
%{dynload_dir}/_dbm.%{SOABI_optimized}.so
%{dynload_dir}/_decimal.%{SOABI_optimized}.so
%{dynload_dir}/_elementtree.%{SOABI_optimized}.so
%{dynload_dir}/_gdbm.%{SOABI_optimized}.so
%{dynload_dir}/_hashlib.%{SOABI_optimized}.so
%{dynload_dir}/_heapq.%{SOABI_optimized}.so
%{dynload_dir}/_json.%{SOABI_optimized}.so
%{dynload_dir}/_lsprof.%{SOABI_optimized}.so
%{dynload_dir}/_lzma.%{SOABI_optimized}.so
%{dynload_dir}/_multibytecodec.%{SOABI_optimized}.so
%{dynload_dir}/_multiprocessing.%{SOABI_optimized}.so
%{dynload_dir}/_opcode.%{SOABI_optimized}.so
%{dynload_dir}/_pickle.%{SOABI_optimized}.so
%{dynload_dir}/_posixsubprocess.%{SOABI_optimized}.so
%{dynload_dir}/_queue.%{SOABI_optimized}.so
%{dynload_dir}/_random.%{SOABI_optimized}.so
%{dynload_dir}/_socket.%{SOABI_optimized}.so
%{dynload_dir}/_sqlite3.%{SOABI_optimized}.so
%{dynload_dir}/_ssl.%{SOABI_optimized}.so
%{dynload_dir}/_struct.%{SOABI_optimized}.so
%{dynload_dir}/array.%{SOABI_optimized}.so
%{dynload_dir}/audioop.%{SOABI_optimized}.so
%{dynload_dir}/binascii.%{SOABI_optimized}.so
%{dynload_dir}/cmath.%{SOABI_optimized}.so
%{dynload_dir}/_datetime.%{SOABI_optimized}.so
%{dynload_dir}/fcntl.%{SOABI_optimized}.so
%{dynload_dir}/grp.%{SOABI_optimized}.so
%{dynload_dir}/math.%{SOABI_optimized}.so
%{dynload_dir}/mmap.%{SOABI_optimized}.so
%{dynload_dir}/nis.%{SOABI_optimized}.so
%{dynload_dir}/ossaudiodev.%{SOABI_optimized}.so
%{dynload_dir}/parser.%{SOABI_optimized}.so
%{dynload_dir}/pyexpat.%{SOABI_optimized}.so
%{dynload_dir}/readline.%{SOABI_optimized}.so
%{dynload_dir}/resource.%{SOABI_optimized}.so
%{dynload_dir}/select.%{SOABI_optimized}.so
%{dynload_dir}/spwd.%{SOABI_optimized}.so
%{dynload_dir}/syslog.%{SOABI_optimized}.so
%{dynload_dir}/termios.%{SOABI_optimized}.so
%{dynload_dir}/_testmultiphase.%{SOABI_optimized}.so
%{dynload_dir}/unicodedata.%{SOABI_optimized}.so
%{dynload_dir}/_uuid.%{SOABI_optimized}.so
%{dynload_dir}/xxlimited.%{SOABI_optimized}.so
%{dynload_dir}/zlib.%{SOABI_optimized}.so

%dir %{pylibdir}/site-packages/
%dir %{pylibdir}/site-packages/__pycache__/
%{pylibdir}/site-packages/README.txt
%{pylibdir}/*.py
%dir %{pylibdir}/__pycache__/
%{pylibdir}/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/collections/
%dir %{pylibdir}/collections/__pycache__/
%{pylibdir}/collections/*.py
%{pylibdir}/collections/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/ctypes/
%dir %{pylibdir}/ctypes/__pycache__/
%{pylibdir}/ctypes/*.py
%{pylibdir}/ctypes/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/ctypes/macholib

%{pylibdir}/curses

%dir %{pylibdir}/dbm/
%dir %{pylibdir}/dbm/__pycache__/
%{pylibdir}/dbm/*.py
%{pylibdir}/dbm/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/distutils/
%dir %{pylibdir}/distutils/__pycache__/
%{pylibdir}/distutils/*.py
%{pylibdir}/distutils/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/distutils/README
%{pylibdir}/distutils/command

%dir %{pylibdir}/email/
%dir %{pylibdir}/email/__pycache__/
%{pylibdir}/email/*.py
%{pylibdir}/email/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/email/mime
%doc %{pylibdir}/email/architecture.rst

%{pylibdir}/encodings

%{pylibdir}/html
%{pylibdir}/http

%dir %{pylibdir}/importlib/
%dir %{pylibdir}/importlib/__pycache__/
%{pylibdir}/importlib/*.py
%{pylibdir}/importlib/__pycache__/*%{bytecode_suffixes}

%dir %{pylibdir}/json/
%dir %{pylibdir}/json/__pycache__/
%{pylibdir}/json/*.py
%{pylibdir}/json/__pycache__/*%{bytecode_suffixes}

%{pylibdir}/logging
%{pylibdir}/multiprocessing

%dir %{pylibdir}/sqlite3/
%dir %{pylibdir}/sqlite3/__pycache__/
%{pylibdir}/sqlite3/*.py
%{pylibdir}/sqlite3/__pycache__/*%{bytecode_suffixes}

%exclude %{pylibdir}/turtle.py
%exclude %{pylibdir}/__pycache__/turtle*%{bytecode_suffixes}

%{pylibdir}/urllib
%{pylibdir}/xml

%attr(0755,root,root) %dir %{_prefix}/lib/python%{branchversion}
%attr(0755,root,root) %dir %{_prefix}/lib/python%{branchversion}/site-packages
%attr(0755,root,root) %dir %{_prefix}/lib/python%{branchversion}/site-packages/__pycache__/

%dir %{pylibdir}/config-%{LDVERSION_optimized}-%{_arch}-linux%{_gnu}/
%{pylibdir}/config-%{LDVERSION_optimized}-%{_arch}-linux%{_gnu}/Makefile
%dir %{_includedir}/python%{LDVERSION_optimized}/
%{_includedir}/python%{LDVERSION_optimized}/%{_pyconfig_h}

%{_libdir}/%{py_INSTSONAME_optimized}
%{_libdir}/libpython3.so


%files devel
%{_bindir}/2to3

%{pylibdir}/config-%{LDVERSION_optimized}-%{_arch}-linux%{_gnu}/*
%exclude %{pylibdir}/config-%{LDVERSION_optimized}-%{_arch}-linux%{_gnu}/Makefile
%exclude %{_includedir}/python%{LDVERSION_optimized}/%{_pyconfig_h}
%{_includedir}/python%{LDVERSION_optimized}/*.h
%{_includedir}/python%{LDVERSION_optimized}/internal/
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit

%{_bindir}/python3-config
%{_libdir}/pkgconfig/python3.pc
%{_bindir}/pathfix.py
%{_bindir}/pygettext3.py
%{_bindir}/msgfmt3.py

%{_bindir}/pygettext%{branchversion}.py
%{_bindir}/msgfmt%{branchversion}.py

%{_bindir}/python%{branchversion}-config
%{_bindir}/python%{LDVERSION_optimized}-config
%{_bindir}/python%{LDVERSION_optimized}-*-config
%{_libdir}/libpython%{LDVERSION_optimized}.so
%{_libdir}/pkgconfig/python-%{LDVERSION_optimized}.pc
%{_libdir}/pkgconfig/python-%{branchversion}.pc

%{_bindir}/idle*
%{pylibdir}/idlelib

%{_datadir}/icons/hicolor/*/apps/idle3.*

%{pylibdir}/tkinter
%exclude %{pylibdir}/tkinter/test
%{dynload_dir}/_tkinter.%{SOABI_optimized}.so
%{pylibdir}/turtle.py
%{pylibdir}/__pycache__/turtle*%{bytecode_suffixes}
%dir %{pylibdir}/turtledemo
%{pylibdir}/turtledemo/*.py
%{pylibdir}/turtledemo/*.cfg
%dir %{pylibdir}/turtledemo/__pycache__/
%{pylibdir}/turtledemo/__pycache__/*%{bytecode_suffixes}

%{pylibdir}/ctypes/test
%{pylibdir}/distutils/tests
%{pylibdir}/sqlite3/test
%{pylibdir}/test
%exclude %{pylibdir}/test/allsans.pem
%exclude %{pylibdir}/test/badcert.pem
%exclude %{pylibdir}/test/badkey.pem
%exclude %{pylibdir}/test/idnsans.pem
%exclude %{pylibdir}/test/keycert2.pem
%exclude %{pylibdir}/test/keycert3.pem
%exclude %{pylibdir}/test/keycert4.pem
%exclude %{pylibdir}/test/keycertecc.pem
%exclude %{pylibdir}/test/keycert.pem
%exclude %{pylibdir}/test/pycakey.pem
%exclude %{pylibdir}/test/ssl_key.pem
%exclude %{pylibdir}/test/keycert3.pem
%exclude %{pylibdir}/test/ssl_key.pem
%{dynload_dir}/_ctypes_test.%{SOABI_optimized}.so
%{dynload_dir}/_testbuffer.%{SOABI_optimized}.so
%{dynload_dir}/_testcapi.%{SOABI_optimized}.so
%{dynload_dir}/_testimportmultiple.%{SOABI_optimized}.so
%{dynload_dir}/_xxtestfuzz.%{SOABI_optimized}.so
%{pylibdir}/lib2to3/tests
%{pylibdir}/tkinter/test
%{pylibdir}/unittest/test

%exclude %dir %{pylibdir}/test/
%exclude %dir %{pylibdir}/test/__pycache__/
%exclude %{pylibdir}/test/__init__.py
%exclude %{pylibdir}/test/__pycache__/__init__%{bytecode_suffixes}
%exclude %{pylibdir}/test/support/

%files debug
%{_bindir}/python3-debug

%{_bindir}/python%{LDVERSION_debug}

%{dynload_dir}/_blake2.%{SOABI_debug}.so
%{dynload_dir}/_md5.%{SOABI_debug}.so
%{dynload_dir}/_sha1.%{SOABI_debug}.so
%{dynload_dir}/_sha256.%{SOABI_debug}.so
%{dynload_dir}/_sha3.%{SOABI_debug}.so
%{dynload_dir}/_sha512.%{SOABI_debug}.so

%{dynload_dir}/_asyncio.%{SOABI_debug}.so
%{dynload_dir}/_bisect.%{SOABI_debug}.so
%{dynload_dir}/_bz2.%{SOABI_debug}.so
%{dynload_dir}/_codecs_cn.%{SOABI_debug}.so
%{dynload_dir}/_codecs_hk.%{SOABI_debug}.so
%{dynload_dir}/_codecs_iso2022.%{SOABI_debug}.so
%{dynload_dir}/_codecs_jp.%{SOABI_debug}.so
%{dynload_dir}/_codecs_kr.%{SOABI_debug}.so
%{dynload_dir}/_codecs_tw.%{SOABI_debug}.so
%{dynload_dir}/_contextvars.%{SOABI_debug}.so
%{dynload_dir}/_crypt.%{SOABI_debug}.so
%{dynload_dir}/_csv.%{SOABI_debug}.so
%{dynload_dir}/_ctypes.%{SOABI_debug}.so
%{dynload_dir}/_curses.%{SOABI_debug}.so
%{dynload_dir}/_curses_panel.%{SOABI_debug}.so
%{dynload_dir}/_dbm.%{SOABI_debug}.so
%{dynload_dir}/_decimal.%{SOABI_debug}.so
%{dynload_dir}/_elementtree.%{SOABI_debug}.so
%{dynload_dir}/_gdbm.%{SOABI_debug}.so
%{dynload_dir}/_hashlib.%{SOABI_debug}.so
%{dynload_dir}/_heapq.%{SOABI_debug}.so
%{dynload_dir}/_json.%{SOABI_debug}.so
%{dynload_dir}/_lsprof.%{SOABI_debug}.so
%{dynload_dir}/_lzma.%{SOABI_debug}.so
%{dynload_dir}/_multibytecodec.%{SOABI_debug}.so
%{dynload_dir}/_multiprocessing.%{SOABI_debug}.so
%{dynload_dir}/_opcode.%{SOABI_debug}.so
%{dynload_dir}/_pickle.%{SOABI_debug}.so
%{dynload_dir}/_posixsubprocess.%{SOABI_debug}.so
%{dynload_dir}/_queue.%{SOABI_debug}.so
%{dynload_dir}/_random.%{SOABI_debug}.so
%{dynload_dir}/_socket.%{SOABI_debug}.so
%{dynload_dir}/_sqlite3.%{SOABI_debug}.so
%{dynload_dir}/_ssl.%{SOABI_debug}.so
%{dynload_dir}/_struct.%{SOABI_debug}.so
%{dynload_dir}/array.%{SOABI_debug}.so
%{dynload_dir}/audioop.%{SOABI_debug}.so
%{dynload_dir}/binascii.%{SOABI_debug}.so
%{dynload_dir}/cmath.%{SOABI_debug}.so
%{dynload_dir}/_datetime.%{SOABI_debug}.so
%{dynload_dir}/fcntl.%{SOABI_debug}.so
%{dynload_dir}/grp.%{SOABI_debug}.so
%{dynload_dir}/math.%{SOABI_debug}.so
%{dynload_dir}/mmap.%{SOABI_debug}.so
%{dynload_dir}/nis.%{SOABI_debug}.so
%{dynload_dir}/ossaudiodev.%{SOABI_debug}.so
%{dynload_dir}/parser.%{SOABI_debug}.so
%{dynload_dir}/pyexpat.%{SOABI_debug}.so
%{dynload_dir}/readline.%{SOABI_debug}.so
%{dynload_dir}/resource.%{SOABI_debug}.so
%{dynload_dir}/select.%{SOABI_debug}.so
%{dynload_dir}/spwd.%{SOABI_debug}.so
%{dynload_dir}/syslog.%{SOABI_debug}.so
%{dynload_dir}/termios.%{SOABI_debug}.so
%{dynload_dir}/_testmultiphase.%{SOABI_debug}.so
%{dynload_dir}/unicodedata.%{SOABI_debug}.so
%{dynload_dir}/_uuid.%{SOABI_debug}.so
%{dynload_dir}/_xxtestfuzz.%{SOABI_debug}.so
%{dynload_dir}/zlib.%{SOABI_debug}.so

%{_libdir}/%{py_INSTSONAME_debug}

%{pylibdir}/config-%{LDVERSION_debug}-%{_arch}-linux%{_gnu}
%{_includedir}/python%{LDVERSION_debug}
%{_bindir}/python%{LDVERSION_debug}-config
%{_bindir}/python%{LDVERSION_debug}-*-config
%{_libdir}/libpython%{LDVERSION_debug}.so
%{_libdir}/libpython%{LDVERSION_debug}.so.1.0
%{_libdir}/pkgconfig/python-%{LDVERSION_debug}.pc

%{dynload_dir}/_tkinter.%{SOABI_debug}.so

%{dynload_dir}/_ctypes_test.%{SOABI_debug}.so
%{dynload_dir}/_testbuffer.%{SOABI_debug}.so
%{dynload_dir}/_testcapi.%{SOABI_debug}.so
%{dynload_dir}/_testimportmultiple.%{SOABI_debug}.so

%undefine _debuginfo_subpackages

%files help
%{_mandir}/*/*

%changelog
* Thu Feb 10 2022 shixuantong <shixuantong@h-partners.com> - 3.7.9-19
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:disable profile guided optimizations for x86_64 and i686 architectures

* Sat Oct 30 2021 hanxinke<hanxinke@huawei.com> - 3.7.9-18
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add the sm3 method for obtaining the salt value

* Fri Sep 24 2021 shixuantong<shixuantong@huawei.com> - 3.7.9-17
- Type:CVE
- CVE:CVE-2021-3733 CVE-2021-3737
- SUG:NA
- DESC:fix CVE-2021-3733 CVE-2021-3737

* Thu Aug 19 2021 hehuazhen<hehuazhen@huawei.com> - 3.7.9-16
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix _PyEval_FiniThreads
       rewrite _PyObject_IsFreed unit tests
       get test_capi passing with address sanitize
       remove use after free reference in ctypes
       fix memory leak in _asynciomodule.c

* Fri Jun 25 2021 hehuazhen<hehuazhen@huawei.com> - 3.7.9-15
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Use gdbm_count for dbm_length if possible
       Don't override PYTHONPATH which is already set by the user

* Mon May 31 2021 shixuantong<shixuantong@huawei.com> - 3.7.9-14
- Type:CVE
- CVE:CVE-2021-3426
- SUG:NA
- DESC:fix CVE-2021-3426

* Sat May 29 2021 BruceGW<gyl93216@163.com> -3.7.9-13
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix memory leak in socketserver.ThreadingMixIn

* Tue May 25 2021 hanxinke<hanxinke@huawei.com> - 3.7.9-12
- Type:enhancement
- CVE:NA
- SUG:NA
- DESC:expose posix_spawn in os module
       fix leaks and errors in new os.posix_spawn
       improve error handing and fix a reference
       fix using of freed memory in old versions
       add signal.valid_signals
       make the sigset_t converter available
       add flag capabilities to posix_spawn
       pass os.environ in test_posix test_specify
       fix TestPosixSpawn.test_close_file
       change the file_actions parameter of os.posix_spawn
       subprocess uses os.posix_spawn in some case
       add os.posix_spawnp
       subprocess can use posix_spawn with pipes
       subprocess close pipes fds by using ExitStack
       guard definition of convert_sched_param with POSIX_SPAWN_SETSCHEDULER
       add setsid parameter to os.posix_spawn() and os.posix_spawnp()
       skip test_start_new_session() of posix_spawn
       fix function name in os.posix_spawnp() errors
       ensure os.posix_spawn() handles None
       rewrite setsid test for os.posix_spawn
       add user and group parameters to subproces
       fix buildbot failures
       posix_spawn doesn't support uid gid
       add umask support to subprocess
       use bin true in test_subprocess
       handle the case when there is no 'true' command
       fix test_subprocess if nobody user doesn't exist
       subprocess: Use vfork() instead of fork() on Linux when safe
       subprocess: Fix handling of pthread_sigmask() errors
       allow setsid() after vfork() on Linux
       fix memory leak in subprocess.Popen() in case of uid/gid overflow
       Unify cleanup in subprocess_fork_exec()

* Mon May 24 2021 hehuazhen<hehuazhen@huawei.com> - 3.7.9-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update use rpm wheels patch and fix test case failure

* Thu Mar 30 2021 shenyangyang<shenyangyang4@huawei.com> - 3.7.9-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Rebuild for openEuler-rpm-config moving /usr/lib/rpm/openEuler/xxxx
       to /usr/lib/xxxx

* Web Mar 03 2021 wuchaochao<wuchaochao4@huawei.com> - 3.7.9-9
- Type:cves
- ID:CVE-2021-23336
- SUG:NA
- DESC:fix CVE-2021-23336

* Wed Feb 24 2021 hehuazhen<hehuazhen@huawei.com> - 3.7.9-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:revert fix a reference leak if a thread is not joined

* Sun Feb 07 2021 shangyibin<shangyibin1@huawei.com> - 3.7.9-7
- Type:cves
- ID:CVE-2021-3177
- SUG:NA
- DESC:fix CVE-2021-3177

* Mon Feb 01 2021 shixuantong<shixuantong@huawei.com> - 3.7.9-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix a reference leak if a thread is not joined

* Sat Nov 14 2020 shixuantong<shixuantong@huawei.com> - 3.7.9-5
- Type:cves
- ID:CVE-2020-27619
- SUG:NA
- DESC:fix CVE-2020-27619

* Fri Nov 13 2020 wangjie<wangjie294@huawei.com> - 3.7.9-4
- Type:NA
- ID:NA
- SUG:NA
- DESC:Change the dependency on the help package from requires to recommends

* Fri Nov 6 2020 wangjie<wangjie294@huawei.com> - 3.7.9-3
- Type:NA
- ID:NA
- SUG:NA
- DESC:Adding help package to the installation dependency of the main package

* Wed Sep 2 2020 tianwei<tianwei12@huawei.com> - 3.7.9-2
- Type:NA
- ID:NA
- SUG:NA
- DESC:convert format for CVE

* Mon Aug 31 2020 shixuantong<shixuantong@huawei.com> - 3.7.9-1
- Type:NA
- ID:NA
- SUG:NA
- DESC:update version to 3.7.9

* Tue Aug 4 2020 wenzhanli<wenzhanli2@huawei.com> - 3.7.4-11
- Type:cves
- ID:NA
- SUG:NA
- DESC:Fix CVE-2019-20907

* Mon Jun 1 2020 hanxinke<hanxinke@huawei.com> - 3.7.4-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add generic_os support to python3

* Tue Apr 21 2020 hanxinke<hanxinke@huawei.com> - 3.7.4-9
- Type:cves
- ID:CVE-2019-9674
- SUG:NA
- DESC:fix CVE-2019-9674

* Tue Mar 17 2020 hanxinke<hanxinke@huawei.com> - 3.7.4-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:patch the CVE

* Sat Feb 22 2020 openEuler Buildteam <buildteam@openeuler.org> - 3.7.4-7
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:revert last commit

* Sat Feb 22 2020 chengquan<chengquan3@huawei.com> - 3.7.4-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Add the default version of python3

* Tue Dec 31 2019 hanxinke<hanxinke@huawei.com> - 3.7.4-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update spec file

* Thu Dec 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.7.4-4
- fix CVE-2019-16056 CVE-2019-16935 CVE-2019-17514
- Delete the test keys, fix BEP problem

* Thu Dec 12 2019 lvying <lvying6@huawei.com> - 3.7.4-3
- provides python3-enum34

* Wed Nov 13 2019 hexiaowen <hexiaowen@huawei.com> - 3.7.4-2
- Add system-rpm-config buildrequires

* Tue Aug 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.7.4-1
- Package init
