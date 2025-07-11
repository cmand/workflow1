from datetime import date, timedelta, datetime

num = "CS596"
name = "Mobile Device and Wireless Security"
quarter = "Fall AY2025"

def item(subdir, filename, ref):
  cle_base = "https://cle.nps.edu/access/content/group/48fe8508-7b80-4309-bd2c-ebea13b779db"
  s = '<a href="' + cle_base + '/' + subdir + '/' + filename + '" target="_blank">' + ref + '</a>'
  return s

#               Mon,   Tues,  Weds,  Thur,  Fri,   Sat,   Sun
lecture_days = [True, True, True, False, False, False, False]
lab_days =     [False, False, False, True, False, False, False]
#lecture_days = [False, True,  False, True, False, False, False]
#lab_days =     [False, True,  False, False, False, False, False]
first_lecture = date(2019, 4, 1)
last_lecture  = date(2019, 6, 10)

holidays = {
  date(2025, 9, 1) : 'Labor Day',
  date(2025, 11, 11) : 'Veterans Day',
  date(2025, 11, 27) : 'Thanksgiving',
}

skip = {
  date(2019, 4, 9) : '',
  date(2019, 4, 30) : '',
}

final = {
  date(2017, 2, 24) : '-',          
  date(2019, 6, 10) : 'Quiz: 11:00-13:00 (Open Book, Open Notes, No Network Access)',
}

lectures = [
  'Class overview: logistics, goals, the "why", course outline',
  'Introduction: Wireless characteristics, 802.11 channels and frames',
  'Introduction: 802.11 MAC',
  'Introduction: symmetric secrecy, cryptanalysis, perfect secrecy',
  'Introduction: OTP, XOR, block ciphers',
  'WEP protocol, authentication',
  'WEP: integrity, ICV, CRC',
  'WEP: key reuse, birthday paradox, RC4',
  'WEP: RC4, FMS key recovery',
  'WEP: obtaining weak IVs, fragmentation, chop-chop',
  'TKIP, integrity, and key mixing',
  'WPA, 802.11i, EAP, RADIUS',
#  '-- No class --',
  'WPA2',
  'WPA2 (cont)',
  'Dictionary Attack and Password Strength',
  'Hash chains',
#  'Asymmetric key crypto, WPA TLS-enterprise',
  'Rainbow Tables',
  'Rainbow Tables and WPA2',
  'Attacks on wireless clients, MITM, Rogue services',
#  'Device fingerprinting',
  'RFID: security and privacy',
  'RFID: hashlocks, DST-40',
  'RFID: DST-40, attack',
  'GSM: security and privacy I',
  'GSM: security and privacy II',
  'GSM: security and privacy III',
  'Bluetooth: security I', 
  'Bluetooth: security II', 
  'Mobile Device: Android security',
  #'GPS: security and privacy I',
  #'GPS: security and privacy II',
  'Review session',
  '-',
  '-',
  '-',
]

labs = [
  'Lab: 802.11',
  'Lab: Wifi network eavesdropping',
  'Lab: Wifi network access I',
  'Lab: WEP key recovery, ARP replay',
  'Lab: WEP key recovery II',
  'Lab: WPA/WPA2',
  'Lab: Client security I',
  'Lab: Client security II',
  'No lab. HW2 Q&A (opt)',
  'Lab: Final exam review',
  '-',
]

assignments_labs = {
  date(2019, 4, 4) : item("labs", "lab1.pdf", "Lab1"),
  date(2019, 4, 11) : item("labs", "lab2.pdf", "Lab2") + "<br>Lab1 Due",
  date(2019, 4, 18) : item("labs", "lab3.pdf", "Lab3") + "<br>Lab2 Due",
  date(2019, 4, 25) : item("labs", "lab4.pdf", "Lab4") + "<br>Lab3 Due",
  date(2019, 5, 9) : item("labs", "lab5.pdf", "Lab5") + "<br>Lab4 Due",
  date(2019, 5, 16) : item("labs", "lab6.pdf", "Lab6") + "<br>Lab5 Due",
  date(2019, 5, 30) : 'Lab6 Due',
}

assignments = {
#  date(2016, 1, 25)  : item("ps", "ps1.pdf", "HW1 assigned") + '<br>' + item("ps", "ps1sol.pdf", "[HW1 Sol'n]"),
  date(2019, 4, 29)  : item("ps", "ps1.pdf", "HW1 assigned"),
  date(2019, 5, 20) : "HW1 due <br>" + "<br>" + item("ps", "ps2.pdf", "HW2 assigned"),
#  date(2017, 2, 24) : "HW1 due <br>" + item("ps", "ps1sol.pdf", "[Sol'n]"),
  date(2019, 5, 15) : item("references", "franklin.pdf", "[FMTNVS06]"),
  date(2019, 5, 21)  : item("references", "rfid_hashlock.pdf", "[WSRE03]"),
  date(2019, 5, 22)  : item("references", "bono.pdf", "[BGSJRS05]"),
  date(2019, 5, 28) : item("references", "a5.pdf", "[BSW00]") + '<br><a href="https://youtu.be/iauwJfHzr1M" target=_blank>Video Lecture</a>',
  date(2019, 6, 4) : item("references", "spill.pdf", "[SB07]") + '<br><a href="https://youtu.be/D0_lv91Bg8I" target=_blank>Video Lecture</a>',
  date(2017, 3, 13) : item("references", "Vidas.pdf", "[VVC11]"),
#  date(2017, 3, 14) : item("references", "Enck.pdf", "[EGCCJMS10]"),
#  date(2017, 3, 15) : item("quizzes", "final-w11.pdf", "Sample Quiz 1") + '<br>' + item("quizzes", "finalsol-w11.pdf", "[Sol'n]"),
  date(2019, 6, 6) : item("quizzes", "final-w11.pdf", "Sample Quiz 1") + '<br>' + item("quizzes", "final-w12.pdf", "Sample Quiz 2"),
#  date(2016, 3, 16) : item("quizzes", "final-w11.pdf", "Sample Quiz"),
  date(2017, 3, 27) : 'HW2 due',
}

notes = {
  date(2019, 4, 1)  : item("lectures", "lec1.pdf", "L1"),
  date(2019, 4, 2)  : item("lectures", "lec2.pdf", "L2"),
  date(2019, 4, 3) : item("lectures", "lec3.pdf", "L3"),
  date(2019, 4, 4) : '-',
  date(2019, 4, 8) : item("lectures", "lec4.pdf", "L4"),
  date(2019, 4, 10) : item("lectures", "lec5.pdf", "L5"),
  date(2019, 4, 11) : '-',
  date(2019, 4, 15) : item("lectures", "lec6.pdf", "L6"),
  date(2019, 4, 16) : item("lectures", "lec7.pdf", "L7"),
  date(2019, 4, 17) : item("lectures", "lec8.pdf", "L8"),
  date(2019, 4, 18) : '-',
  date(2019, 4, 22) : item("lectures", "lec9.pdf", "L9"),
  date(2019, 4, 23) : item("lectures", "lec10.pdf", "L10"),
  date(2019, 4, 24) : item("lectures", "lec11.pdf", "L11"),
  date(2019, 4, 25) : '-',
  date(2019, 4, 29) : item("lectures", "lec12.pdf", "L12"),
  date(2019, 4, 30) : '-',
  date(2019, 5, 1)  : item("lectures", "lec13.pdf", "L13"),
  date(2019, 5, 2) : '-',
  date(2019, 5, 6) : '-',
  date(2019, 5, 7)  : item("lectures", "lec15.pdf", "L15"),
  date(2019, 5, 8)  : item("lectures", "lec16.pdf", "L16"),
  date(2019, 5, 9) : '-',
  date(2019, 5, 13) : item("lectures", "lec17.pdf", "L17"),
  date(2019, 5, 14) : item("lectures", "lec18.pdf", "L18"),
  date(2019, 5, 15) : item("lectures", "lec19.pdf", "L19"),
  date(2019, 5, 16) : '-',
  date(2019, 5, 20) : item("lectures", "rfid1.pdf", "L20"),
  date(2019, 5, 21) : item("lectures", "rfid2.pdf", "L21"),
  date(2019, 5, 22) : item("lectures", "lec22.pdf", "L22"),
  date(2019, 5, 23) : '-',
  date(2019, 5, 27) : '-',
  date(2019, 5, 28) : item("lectures", "gsmintro.pdf", "L23"),
  date(2019, 5, 29) : '-',
  date(2019, 5, 30) : '-',
  date(2019, 6, 3) : item("lectures", "lec25.pdf", "L25"),
  date(2019, 6, 4) : item("lectures", "bluetooth.pdf", "L26"),
  date(2019, 6, 5) : '-',
  date(2019, 6, 6) : '-',
}
