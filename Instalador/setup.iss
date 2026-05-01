; BitCraft Antivirus Installer Script
[Setup]
AppName=BitCraft Antivirus
AppVersion=1.0
AppPublisher=BitCraft Security
DefaultDirName={autopf}\BitCraft_Antivirus
DefaultGroupName=BitCraft Antivirus
OutputDir=.
OutputBaseFilename=BitCraft_Antivirus_Setup
SetupIconFile=icon.ico
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Files]
Source: "BitCraft_Antivirus\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\BitCraft Antivirus"; Filename: "{app}\BitCraft_Antivirus.exe"
Name: "{group}\Desinstalar BitCraft"; Filename: "{uninstallexe}"
Name: "{autodesktop}\BitCraft Antivirus"; Filename: "{app}\BitCraft_Antivirus.exe"

[Run]
Filename: "{app}\BitCraft_Antivirus.exe"; Description: "Iniciar BitCraft Antivirus"; Flags: nowait postinstall skipifsilent