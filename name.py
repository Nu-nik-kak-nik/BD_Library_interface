BUTTONS_TABLE = {
    'lib_btn': 'library',
    'room_btn': 'room',
    'book_btn': 'books',
    'readers_btn': 'readers',
    'is_btn': 'issuance'
}

LIST_BUTTON = [
    'lib_btn',
    'room_btn',
    'book_btn',
    'readers_btn',
    'is_btn'
]

UPDATES_TABLE = {
    'lib_btn': "UPDATE library SET libtitle=%s, address=%s, city=%s WHERE idlibrary=%s",
    'room_btn': "UPDATE room SET nameroom=%s, idlibrary=%s, unitsliterature=%s, numberseats=%s, workinghours=%s, floor=%s, numberemployees=%s WHERE idroom=%s",
    'book_btn': "UPDATE books SET littitle=%s, lcategory=%s, authors=%s, publishing=%s, yearpublishing=%s, numpages=%s, idroom=%s WHERE idliterature=%s",
    'readers_btn': "UPDATE readers SET lastname=%s, firstname=%s, surname=%s, readercategory=%s, rplace=%s, birth=%s, rdate=%s WHERE idreader=%s",
    'is_btn': "UPDATE issuance SET idreader=%s, idliterature=%s, dateissue=%s, issueperiod=%s, typeissue=%s, collateral=%s WHERE idissuedlit=%s"
}
