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
    'lib_btn': "UPDATE library SET libtitle='{row_data[1]}', address='{row_data[2]}', city='{row_data[3]}' WHERE idlibrary='{primary_key_value}'",
    'room_btn': "UPDATE room SET nameroom='{row_data[1]}', idlibrary='{row_data[2]}', unitsliterature='{row_data[3]}', numberseats='{row_data[4]}', workinghours='{row_data[5]}', floor='{row_data[6]}', numberemployees='{row_data[7]}' WHERE idroom='{row_data[0]}'",
    'book_btn': "UPDATE books SET littitle='{row_data[1]}', lcategory='{row_data[2]}', authors='{row_data[3]}', publishing='{row_data[4]}', yearpublishing='{row_data[5]}', numpages='{row_data[6]}', idroom='{row_data[7]}' WHERE idliterature='{row_data[0]}'",
    'readers_btn': "UPDATE readers SET lastname='{row_data[1]}', firstname='{row_data[2]}', surname='{row_data[3]}', readercategory='{row_data[4]}', rplace='{row_data[5]}', birth='{row_data[6]}', rdate='{row_data[7]}' WHERE idreader='{row_data[0]}'",
    'is_btn': "UPDATE issuance SET idreader='{row_data[1]}', idliterature='{row_data[2]}', dateissue='{row_data[3]}', issueperiod='{row_data[4]}', typeissue='{row_data[5]}', collateral='{row_data[6]}' WHERE idissuedlit='{row_data[0]}'"
}
