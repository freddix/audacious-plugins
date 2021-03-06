Summary:	Plugins for Audacious media player
Name:		audacious-plugins
Version:	3.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	f1a2ef5fac0afa08d7f54b12f6f64a4e
URL:		http://audacious-media-player.org/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	audacious-devel >= %{version}
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	glib-gio-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmtp-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsidplayfp-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	mpg123-libs-devel
BuildRequires:	neon-devel
BuildRequires:	pkg-config
BuildRequires:	wavpack-devel
Requires:	audacious >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Audacious media player.

%prep
%setup -qn %{name}-%{version}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	--disable-adplug	\
	--enable-amidiplug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/audacious/paranormal/Presets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/id{_ID,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/ml{_IN,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/sr{_RS,}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{cmn,fa_IR,sr/sr_RS}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/audacious/Skins
%attr(755,root,root) %{_libdir}/audacious/Container/asx.so
%attr(755,root,root) %{_libdir}/audacious/Container/asx3.so
%attr(755,root,root) %{_libdir}/audacious/Container/audpl.so
%attr(755,root,root) %{_libdir}/audacious/Container/m3u.so
%attr(755,root,root) %{_libdir}/audacious/Container/pls.so
%attr(755,root,root) %{_libdir}/audacious/Container/xspf.so

%attr(755,root,root) %{_libdir}/audacious/Effect/compressor.so
%attr(755,root,root) %{_libdir}/audacious/Effect/crossfade.so
%attr(755,root,root) %{_libdir}/audacious/Effect/crystalizer.so
%attr(755,root,root) %{_libdir}/audacious/Effect/echo.so
%attr(755,root,root) %{_libdir}/audacious/Effect/ladspa.so
%attr(755,root,root) %{_libdir}/audacious/Effect/mixer.so
%attr(755,root,root) %{_libdir}/audacious/Effect/resample.so
%attr(755,root,root) %{_libdir}/audacious/Effect/silence-removal.so
%attr(755,root,root) %{_libdir}/audacious/Effect/speed-pitch.so
%attr(755,root,root) %{_libdir}/audacious/Effect/stereo.so
%attr(755,root,root) %{_libdir}/audacious/Effect/voice_removal.so

%attr(755,root,root) %{_libdir}/audacious/General/alarm.so
%attr(755,root,root) %{_libdir}/audacious/General/albumart.so
%attr(755,root,root) %{_libdir}/audacious/General/aosd.so
%attr(755,root,root) %{_libdir}/audacious/General/cd-menu-items.so
%attr(755,root,root) %{_libdir}/audacious/General/delete-files.so
%attr(755,root,root) %{_libdir}/audacious/General/gnomeshortcuts.so
%attr(755,root,root) %{_libdir}/audacious/General/gtkui.so
%attr(755,root,root) %{_libdir}/audacious/General/hotkey.so
%attr(755,root,root) %{_libdir}/audacious/General/lyricwiki.so
%attr(755,root,root) %{_libdir}/audacious/General/mpris2.so
%attr(755,root,root) %{_libdir}/audacious/General/notify.so
%attr(755,root,root) %{_libdir}/audacious/General/playlist-manager.so
%attr(755,root,root) %{_libdir}/audacious/General/scrobbler.so
%attr(755,root,root) %{_libdir}/audacious/General/search-tool.so
%attr(755,root,root) %{_libdir}/audacious/General/skins.so
%attr(755,root,root) %{_libdir}/audacious/General/song_change.so
%attr(755,root,root) %{_libdir}/audacious/General/statusicon.so

%attr(755,root,root) %{_libdir}/audacious/Input/aac-raw.so
%attr(755,root,root) %{_libdir}/audacious/Input/amidi-plug.so
%attr(755,root,root) %{_libdir}/audacious/Input/cdaudio-ng.so
%attr(755,root,root) %{_libdir}/audacious/Input/console.so
%attr(755,root,root) %{_libdir}/audacious/Input/ffaudio.so
%attr(755,root,root) %{_libdir}/audacious/Input/flacng.so
%attr(755,root,root) %{_libdir}/audacious/Input/madplug.so
%attr(755,root,root) %{_libdir}/audacious/Input/metronom.so
%attr(755,root,root) %{_libdir}/audacious/Input/modplug.so
%attr(755,root,root) %{_libdir}/audacious/Input/psf2.so
%attr(755,root,root) %{_libdir}/audacious/Input/sid.so
%attr(755,root,root) %{_libdir}/audacious/Input/sndfile.so
%attr(755,root,root) %{_libdir}/audacious/Input/tonegen.so
%attr(755,root,root) %{_libdir}/audacious/Input/vorbis.so
%attr(755,root,root) %{_libdir}/audacious/Input/vtx.so
%attr(755,root,root) %{_libdir}/audacious/Input/wavpack.so
%attr(755,root,root) %{_libdir}/audacious/Input/xsf.so

%attr(755,root,root) %{_libdir}/audacious/Output/alsa.so
%attr(755,root,root) %{_libdir}/audacious/Output/filewriter.so
%attr(755,root,root) %{_libdir}/audacious/Output/jack-ng.so
%attr(755,root,root) %{_libdir}/audacious/Output/sdlout.so

%attr(755,root,root) %{_libdir}/audacious/Transport/gio.so
%attr(755,root,root) %{_libdir}/audacious/Transport/mms.so
%attr(755,root,root) %{_libdir}/audacious/Transport/neon.so

%attr(755,root,root) %{_libdir}/audacious/Visualization/blur_scope.so
%attr(755,root,root) %{_libdir}/audacious/Visualization/cairo-spectrum.so
%attr(755,root,root) %{_libdir}/audacious/Visualization/gl-spectrum.so

%{_datadir}/audacious/paranormal

