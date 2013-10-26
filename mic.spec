# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       mic

# >> macros
# << macros

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Summary:    Image Creator for Linux Distributions
Version:    0.14
Release:    8
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
Source1:    mic.conf
Source100:  mic.yaml
Patch0:     0001-Add-486-to-permitted-arch-list.patch
Patch1:     0002-If-du-fails-report-which-file-it-fails-on.patch
Patch2:     0003-Don-t-cross-filesystem-boundaries-when-doing-du.patch
Patch3:     0004-Add-mipsel-to-architecture-list-to-fix-MER-497.patch
Patch4:     0005-don-t-ignore-mtab-on-copying-the-fs-image.patch
Patch5:     0006-don-t-tamper-with-mtab-on-mic-chroot.patch
Patch6:     0007-Fix-zypp-backend.patch
Patch7:     0008-Add-new-recording-file-.urls-which-contains-urls-of-.patch
Patch8:     0009-Extract-uImage-files-from-boot-when-using-copy-kerne.patch
Patch9:     0010-Refactor-common-creator-options-and-add-token-map-fe.patch
Patch10:     0011-Fixup-for-usage-with-.netrc-enabled-urlgrabber-and-z.patch
Patch11:     0012-Workaround-for-repos-with-broken-repomd.xml-files.patch
Patch12:     0013-Replace-upstream-packaging-with-mer-packaging.patch
Patch13:     0014-Misc.-fixes.patch
Patch14:     0015-tmp-permissions-should-be-1777.patch
Patch15:     0016-use-bash-as-post-script-interpreter-to-get-job-contr.patch
Patch16:     0017-kill-leftover-processes-running-in-post-chroot.patch
Patch17:     0018-fix-liveusb-due-to-change-in-dc1873f32c0b4f8c8735b65.patch
Patch18:     0019-Fix-two-zypper-patterns-use-cases.patch
Patch19:     0020-Preserve-sparseness-of-files-on-packing.patch
Patch20:     0021-Generate-complete-fstab-for-loop-images.patch
Patch21:     0022-Add-support-for-pre-scripts-and-erroronfail.patch
Patch22:     0023-Fix-bug-when-mic-crashes-if-there-is-no-pattern-in-k.patch
Patch23:     0024-Add-an-rpmmisc.checkRpmChecksum-to-verify-a-cached-r.patch
Patch24:     0025-Add-mipsel-support-to-mic.patch
Patch25:     0026-let-blkid-use-dev-null-as-cache-file.patch
Patch26:     0027-kickstart-pack-and-attachemnt-sections-and-btrfs-com.patch
Patch27:     0028-btrfs-use-subvolume-name-instead-of-id-in-fstab.patch
Patch28:     0029-a-couple-of-small-bugfixes-for-post-and-pack-hnadlin.patch
Patch29:     0030-Fix-tmp-dir-access-right-handling-for-pre-post-scrip.patch
Requires:   util-linux
Requires:   coreutils
Requires:   python >= 2.5
Requires:   e2fsprogs
Requires:   dosfstools >= 2.11-8
Requires:   yum >= 3.2.24
Requires:   syslinux >= 3.82
Requires:   kpartx
Requires:   parted
Requires:   device-mapper
Requires:   /usr/bin/genisoimage
Requires:   cpio
Requires:   isomd5sum
Requires:   gzip
Requires:   bzip2
Requires:   python-urlgrabber
Requires:   squashfs-tools >= 4.0
Requires:   btrfs-progs
Requires:   python-m2crypto
Requires:   python-zypp >= 0.5.9.1
Requires:   psmisc
BuildRequires:  python-devel

%description
The tool mic is used to create and manipulate images for Linux distributions.
It is composed of three subcommand\: create, convert, chroot. Subcommand create
is used to create images with different types; subcommand convert is used to
convert an image to a specified type; subcommand chroot is used to chroot into
an image.


%prep
%setup -q -n src

# 0001-Add-486-to-permitted-arch-list.patch
%patch0 -p1
# 0002-If-du-fails-report-which-file-it-fails-on.patch
%patch1 -p1
# 0003-Don-t-cross-filesystem-boundaries-when-doing-du.patch
%patch2 -p1
# 0004-Add-mipsel-to-architecture-list-to-fix-MER-497.patch
%patch3 -p1
# 0005-don-t-ignore-mtab-on-copying-the-fs-image.patch
%patch4 -p1
# 0006-don-t-tamper-with-mtab-on-mic-chroot.patch
%patch5 -p1
# 0007-Fix-zypp-backend.patch
%patch6 -p1
# 0008-Add-new-recording-file-.urls-which-contains-urls-of-.patch
%patch7 -p1
# 0009-Extract-uImage-files-from-boot-when-using-copy-kerne.patch
%patch8 -p1
# 0010-Refactor-common-creator-options-and-add-token-map-fe.patch
%patch9 -p1
# 0011-Fixup-for-usage-with-.netrc-enabled-urlgrabber-and-z.patch
%patch10 -p1
# 0012-Workaround-for-repos-with-broken-repomd.xml-files.patch
%patch11 -p1
# 0013-Replace-upstream-packaging-with-mer-packaging.patch
%patch12 -p1
# 0014-Misc.-fixes.patch
%patch13 -p1
# 0015-tmp-permissions-should-be-1777.patch
%patch14 -p1
# 0016-use-bash-as-post-script-interpreter-to-get-job-contr.patch
%patch15 -p1
# 0017-kill-leftover-processes-running-in-post-chroot.patch
%patch16 -p1
# 0018-fix-liveusb-due-to-change-in-dc1873f32c0b4f8c8735b65.patch
%patch17 -p1
# 0019-Fix-two-zypper-patterns-use-cases.patch
%patch18 -p1
# 0020-Preserve-sparseness-of-files-on-packing.patch
%patch19 -p1
# 0021-Generate-complete-fstab-for-loop-images.patch
%patch20 -p1
# 0022-Add-support-for-pre-scripts-and-erroronfail.patch
%patch21 -p1
# 0023-Fix-bug-when-mic-crashes-if-there-is-no-pattern-in-k.patch
%patch22 -p1
# 0024-Add-an-rpmmisc.checkRpmChecksum-to-verify-a-cached-r.patch
%patch23 -p1
# 0025-Add-mipsel-support-to-mic.patch
%patch24 -p1
# 0026-let-blkid-use-dev-null-as-cache-file.patch
%patch25 -p1
# 0027-kickstart-pack-and-attachemnt-sections-and-btrfs-com.patch
%patch26 -p1
# 0028-btrfs-use-subvolume-name-instead-of-id-in-fstab.patch
%patch27 -p1
# 0029-a-couple-of-small-bugfixes-for-post-and-pack-hnadlin.patch
%patch28 -p1
# 0030-Fix-tmp-dir-access-right-handling-for-pre-post-scrip.patch
%patch29 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{__python} setup.py install --root=%{buildroot} -O1

# >> install post
# install our mic.conf
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf
# << install post

%files
%defattr(-,root,root,-)
# >> files
%doc README.rst
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{python_sitelib}/*
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/*
%{_bindir}/*
# << files
