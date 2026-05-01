// Reglas YARA - SecureGuard Security
// Versión: 1.0
// Uso educativo y de protección

rule Ransomware_Behavior {
    meta:
        description = "Detecta comportamiento típico de ransomware"
        author = "SecureGuard Security"
        severity = "high"
    strings:
        $encrypt = "Encrypt" nocase
        $decrypt = "Decrypt" nocase
        $ransom = "ransom" nocase
        $bitcoin = "bitcoin" nocase wide
        $tor = ".onion" nocase
    condition:
        3 of them
}

rule Mimikatz_Detection {
    meta:
        description = "Detecta Mimikatz y variantes"
        author = "SecureGuard Security"
    strings:
        $m1 = "mimikatz" nocase
        $m2 = "sekurlsa::logonpasswords" nocase
        $m3 = "lsadump::sam" nocase
        $m4 = "privilege::debug" nocase
    condition:
        any of them
}

rule Keylogger_Strings {
    meta:
        description = "Strings comunes en keyloggers"
        author = "SecureGuard Security"
    strings:
        $k1 = "GetAsyncKeyState" nocase
        $k2 = "SetWindowsHookEx" nocase
        $k3 = "keylog" nocase
        $k4 = "KeyboardProc" nocase
    condition:
        2 of them
}