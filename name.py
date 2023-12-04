BUTTONS_TABLE = {
    'lib_btn': 'library',
    'room_btn': 'room',
    'book_btn': 'books',
    'readers_btn': 'readers',
    'is_btn': 'issuance'
}

LIST_BUTTON_TABLE = [
    'lib_btn',
    'room_btn',
    'book_btn',
    'readers_btn',
    'is_btn'
]

LIST_BUTTON_MANAGEMENT = [
    'safe_btn',
    'new_btn',
    'editing_btn',
    'del_btn'
]

BUTTON_MANAGEMENT = {
    'safe_btn': 'save_changes',
    'new_btn': 'new_row_interface',
    'editing_btn': 'editing',
    'del_btn': 'delete_row'
}

UPDATES_TABLE = {
    'lib_btn': "UPDATE library SET libtitle=%s, address=%s, city=%s WHERE idlibrary=%s",
    'room_btn': "UPDATE room SET nameroom=%s, idlibrary=%s, unitsliterature=%s, numberseats=%s, workinghours=%s, floor=%s, numberemployees=%s WHERE idroom=%s",
    'book_btn': "UPDATE books SET littitle=%s, lcategory=%s, authors=%s, publishing=%s, yearpublishing=%s, numpages=%s, idroom=%s WHERE idliterature=%s",
    'readers_btn': "UPDATE readers SET lastname=%s, firstname=%s, surname=%s, readercategory=%s, rplace=%s, birth=%s, rdate=%s WHERE idreader=%s",
    'is_btn': "UPDATE issuance SET idreader=%s, idliterature=%s, dateissue=%s, issueperiod=%s, typeissue=%s, collateral=%s WHERE idissuedlit=%s"
}

INSERT_TABLE = {
    'lib_btn': "INSERT INTO library (idlibrary, libtitle, address, city) VALUES (%s, %s, %s, %s)",
    'room_btn': "INSERT INTO room (idroom, nameroom, idlibrary, unitsliterature, numberseats, workinghours, floor, numberemployees) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    'book_btn': "INSERT INTO  books (idliterature, littitle, lcategory, authors, publishing, yearpublishing, numpages, idroom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    'readers_btn': "INSERT INTO  readers (idreader, lastname, firstname, surname, readercategory, rplace, birth, rdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    'is_btn': "INSERT INTO issuance (idissuedlit, idreader, idliterature, dateissue, issueperiod, typeissue, collateral) VALUES (%s, %s, %s, %s, %s, %s, %s)"
}

DELETE_TABLE = {
    'lib_btn': "DELETE from library WHERE idlibrary=%s",
    'room_btn': "DELETE from room WHERE idroom=%s",
    'book_btn': "DELETE from books WHERE idliterature=%s",
    'readers_btn': "DELETE from readers WHERE idreader=%s",
    'is_btn': "DELETE from issuance WHERE idissuedlit=%s"
}

