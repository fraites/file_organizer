def getpath(extension):
    return extension_dict[extension]

extension_dict = {
    # No name
    'noname' : "Other/Uncategorized",
	'.vcf'   : "Other/Uncategorized",
    # Audio
    '.aif'   : "Media/Audio",
    '.cda'   : "Media/Audio",
    '.fit'   : "Media/Audio/Adobe",
    '.mid'   : "Media/Audio",
    '.midi'  : "Media/Audio",
    '.mp3'   : "Media/Audio",
    '.mpa'   : "Media/Audio",
    '.ogg'   : "Media/Audio",
    '.wav'   : "Media/Audio",
    '.wma'   : "Media/Audio",
    '.wpl'   : "Media/Audio",
    '.m3u'   : "Media/Audio",
    '.vox'   : "Media/Audio",
    '.8svx'  : "Media/Audio",
    '.sdt'  : "Media/Audio",
    '.mka'  : "Media/Audio",
    '.ac3'  : "Media/Audio",
    '.m3u8'  : "Media/Audio",
    '.m4a'  : "Media/Audio",
    '.mp2'  : "Media/Audio",
    '.mdc'  : "Media/Audio",


    # Text
    '.txt'   : "Text/TextFiles",
    '.doc'   : "Text/Word",
    '.docx'  : "Text/Word",
    '.fm'    : "Text/Adobe/Documents",
    '.odt'   : "Text/Word",
    '.pdf'   : "Text/PDF",
    '.rtf'   : "Text/TextFiles",
    '.md'    : "Text/TextFiles",
    '.tex'   : "Text/TextFiles",
    '.wks'   : "Text/TextFiles",
    '.wps'   : "Text/TextFiles",
    '.wpd'   : "Text/TextFiles",
	 '.xps'   : "Text/TextFiles",
    '.xps'   : "Text/TextFiles",
    '.apt'   : "Text/TextFiles",
    '.rft'   : "Text/TextFiles",
    '.plain'   : "Text/TextFiles",
    '.rtx'   : "Text/TextFiles",
    '.1st'   : "Text/TextFiles",
    '.602'   : "Text/TextFiles",
    '.ascii'   : "Text/TextFiles",
    # Video
    '.3g2'   : "Media/Video",
    '.3gp'   : "Media/Video",
    '.avi'   : "Media/Video",
    '.aep'   : "Media/Adobe/AfterEffects",
    '.dir'   : "Media/Adobe/Director",
    '.flv'   : "Media/Video",
    '.h264'  : "Media/Video",
    '.m4v'   : "Media/Video",
    '.mkv'   : "Media/Video",
    '.mov'   : "Media/Video",
    '.mp4'   : "Media/Video",
    '.mpg'   : "Media/Video",
    '.mpeg'  : "Media/Video",
    '.rm'    : "Media/Video",
    '.swf'   : "Media/Video",
    '.vob'   : "Media/Video",
    '.wmv'   : "Media/Video",
    #-
    '.3gpp'   : "Media/Video",
    '.mk3d'   : "Media/Video",
    '.m15'   : "Media/Video",
    '.mp4v'   : "Media/Video",
    '.hevc'   : "Media/Video",
    '.264'   : "Media/Video",
    '.mpeg4'   : "Media/Video",
    '.xvid'   : "Media/Video",

    # Images
    '.ai'    : "Media/Images",
    '.asc'   : "Media/Adobe/Flash",
    '.api'   : "Media/Adobe/Photoshop
    '.bmp'   : "Media/Images",
    '.eps'   : "Media/Adobe/Images",
    '.fla'   : "Media/Adobe/Flash",
    '.gif'   : "Media/Images",
    '.ico'   : "Media/Images",
    '.jpg'   : "Media/Images",
    '.jpeg'  : "Media/Images",
    '.png'   : "Media/Images",
    '.ps'    : "Media/Adobe/Images",
    '.psd'   : "Media/Adobe/Images",
    '.pbj'   : "Media/Adobe/Images",
    '.svg'   : "Media/Images",
    '.shp'   : "Media/Images",
    '.tif'   : "Media/Images",
    '.tiff'  : "Media/Images",
    '.CR2'   : "Media/Images",
    '.HEIC'  : "Media/Images",
    # Internet
    '.asp'   : "Other/Internet",
    '.aspx'  : "Other/Internet",
    '.cer'   : "Other/Internet",
    '.cfm'   : "Other/Internet",
    '.cgi'   : "Other/Internet",
    '.pl'    : "Other/Internet",
    '.css'   : "Other/Internet",
    '.scss'  : "Other/Internet",
    '.htm'   : "Other/Internet",
    '.js'    : "Other/Internet",
    '.jsp'   : "Other/Internet",
    '.part'  : "Other/Internet",
    '.php'   : "Other/Internet",
    '.rss'   : "Other/Internet",
    '.xhtml' : "Other/Internet",
	'.torrent': "Other/Internet",
    '.dhtml' : "Other/Internet",
    '.zhtml' : "Other/Internet",
    '.vrt' : "Other/Internet",
    '.jspa' : "Other/Internet",
    '.whtt' : "Other/Internet",
    '.fmp' : "Other/Internet",
    # Compressed
    '.7z'    : "Other/Compressed",
    '.arj'   : "Other/Compressed",
    '.cab'   : "Other/Compressed",
    '.deb'   : "Other/Compressed",
    '.dgm'   : "Other/Compressed",
    '.gz'    : "Other/Compressed",
    '.pkg'   : "Other/Compressed",
    '.rar'   : "Other/Compressed",
    '.rpm'   : "Other/Compressed",
    '.tgz'   : "Other/Compressed",
    '.xz'    : "Other/Compressed",
    '.z'     : "Other/Compressed",
    '.zip'   : "Other/Compressed",
    
    # Disc
    '.bin'   : "Other/Disc",
    '.cue'   : "Other/Disc",
    '.dmg'   : "Other/Disc",
    '.iso'   : "Other/Disc",
    '.toast' : "Other/Disc",
    '.vcd'   : "Other/Disc",
    # Database
    '.csv'   : "Programming/Database",
    '.dat'   : "Programming/Database",
    '.db'    : "Programming/Database",
    '.dbf'   : "Programming/Database",
    '.log'   : "Programming/Database",
    '.mdb'   : "Programming/Database",
    '.sav'   : "Programming/Database",
    '.sql'   : "Programming/Database",
    '.tar'   : "Programming/Database",
    '.xml'   : "Programming/Database",
    '.json'  : "Programming/Database",
    # Executables
    '.apk'   : "Other/Executables",
    '.aab'   : "Other/Executables",
    '.air'   : "Other/Executables/Adobe",
    '.bat'   : "Other/Executables",
    '.com'   : "Other/Executables",
    '.cpl'   : "Control Panel Extension/Windows/Executables",
    '.csh'   : "C Shell Script/macOS,linux/Executables",
    '.exe'   : "Other/Executables",
    '.gadget': "Other/Executables",
    '.jar'   : "Other/Executables",
    '.lnk'   : "File Shortcut/Windows/Executables",
    '.paf'   : "Portable Application Installer File/Windows/Executables",
    '.wsf'   : "Other/Executables",
    '.ws'    : "Other/Executables",
    '.wsh'   : "Other/Executables",
    # Fonts
    '.afm'   : "Other/Fonts",
    '.fnt'   : "Other/Fonts",
    '.fon'   : "Other/Fonts",
    '.otf'   : "Other/Fonts",
    '.ttf'   : "Other/Fonts",
    '.ufo'   : "Other/Fonts",
    # Presentations
    '.key'   : "Text/Presentations",
    '.odp'   : "Text/Presentations",
    '.pps'   : "Text/Presentations",
    '.ppt'   : "Text/Presentations",
    '.pptx'  : "Text/Presentations",
    # Programming
    '.c'     : "Programming/C++andC",
    '.class' : "Programming/Java",
    '.cfm'   : "Programming/Adobe/ColdFusion",
    '.cfml'  : "Programming/Adobe/ColdFusion",
    '.cpp'   : "Programming/C++andC",
    '.dart'  : "Programming/Dart",
    '.gml'   : "Programming/Geographic-Markup-File",
    '.h'     : "Programming/C++andC",
    '.html'  : "Programming/HTML",
    '.java'  : "Programming/Java",
    '.lua'   : "Programming/LUA",
    '.m'     : "Programming/MATLAB",
    '.scala' : "Programming/Scala",
    '.vala'  : "Programming/Vala",
    '.R'     : "Programming/R",
    '.cs'    : "Programming/C#",
    '.py'    : "Programming/Python",
    '.sh'    : "Programming/Shell",
    '.swift' : "Programming/Swift",
	'.sln'   : "Programming/VisualStudio",

    # Spreadsheets
    '.cvs'   : "Text/Spreadsheets",
    '.ods'   : "Text/Spreadsheets",
    '.xlr'   : "Text/Spreadsheets",
    '.xls'   : "Text/Spreadsheets",
    '.xlsx'  : "Text/Spreadsheets",
    # System
    '.bak'   : "Text/Other/System",
    '.cab'   : "Text/Other/System",
    '.cfg'   : "Text/Other/System",
    '.dem'   : "Text/Other/System",
    '.cpl'   : "Text/Other/System",
    '.cur'   : "Text/Other/System",
    '.dll'   : "Text/Other/System",
    '.dmp'   : "Text/Other/System",
    '.drv'   : "Text/Other/System",
    '.icns'  : "Text/Other/System",
    '.ini'   : "Text/Other/System",
    '.lnk'   : "Text/Other/System",
    '.msi'   : "Text/Other/System",
    '.sys'   : "Text/Other/System",
    '.tmp'   : "Text/Other/System"
}
