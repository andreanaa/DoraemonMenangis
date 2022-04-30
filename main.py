import os
import datetime

def isInteger(value):  # memeriksa apakah sebuah value merupakan integer
    # input  : value : unknown
    # output : bool
    
    # KAMUS LOKAL
    # test : integer
    # value : unknown

    # ALGORITMA
    try:
        # casting ke integer
        test = int(value)
        return True
    except ValueError:
        return False

def inputNomorValid(message, a, b):  # pengulangan input hingga didapat input nomor yang valid (merupakan integer dan berada di dalam range a sampai b)
    # input  : message : string
    #          a, b : integer
    # output : value : integer

    # KAMUS LOKAL
    # messge, value : string
    # valid : bool
    # a, b : integer

    # ALGORITMA
    value = ''  # value default
    valid = False
    while not valid:  # mengulang input sampai didapat nomor valid
        value = input(message)
        if isInteger(value):
            if int(value) in range(a, b + 1):
                valid = True
            else:
                print("input tidak valid, ulangi")
        else:
            print("input tidak valid, ulangi")
    return int(value)

def inputValidDate(message):  # pengulangan input hingga didapat value tanggal yang valid
    # input  : message : string
    # output : date : string

    # KAMUS LOKAL
    # message, date : string
    # valid : bool

    # ALGORITMA
    date = ''
    valid = False
    while not valid:
        date = input(message)
        if isValidDate(date):
            valid = True
            return date
        else:
            print("input tanggal tidak valid (DD/MM/YYYY)")

def isValidDate(string_date):  # memeriksa apakah sebuah value merupakan tanggal
    # input  : string_date : string
    # output : bool

    # KAMUS LOKAL
    # string_date : string
    # arr_date : array of integer

    # ALGORITMA
    if len(string_date) != 10:
        return False
    if (string_date[2] != '/') or (string_date[5] != '/'):
        return False
    if not (isInteger(string_date[0:2]) and (isInteger(string_date[3:5]))):
        return False
    try:
        arr_date = separate_date(string_date)
        datetime.datetime(arr_date[2], arr_date[1], arr_date[0])
        return True
    except ValueError:
        return False

def separate(list):  # memisahkan string menjadi list dengan delimiter titik koma menjadi list
    # input  : list : string
    # output : newlist : array of string

    # KAMUS LOKAL
    # newlist : array of string
    # a, i : integer
    # list : string

    # ALGORITMA
    newlist = []
    a = 0
    for i in range(len(list)):
        if list[i] == ';':
            newlist.append(list[a:i])
            a = i + 1
    newlist.append(list[a:])
    return newlist

def separate_date(list):  # memisahkan string menjadi list dengan delimiter forward slash menjadi list
    # input  : list : string
    # output : temp : array of integer

    # KAMUS LOKAL
    # temp : array of integer
    # a, i : integer
    # list : string

    # ALGORITMA
    temp = []
    a = 0
    for i in range(len(list)):
        if list[i] == '/':
            temp.append(int(list[a:i]))
            a = i + 1
    temp.append(int(list[a:]))
    return temp

def RealValue_gadget(array_data):  # mengubah data menjadi nilai sebenarnya (integer, float, dll)
    # input  : array_data : array of string
    # output : arr_cpy : array of (string and integer)

    # KAMUS LOKAL
    # array_data : array of string
    # i : integer
    # arr_cpy : (array of string) -> (array of (string and integer))

    # ALGORITMA
    arr_cpy = array_data[:]
    for i in range(6):
        if (i == 3):
            arr_cpy[i] = int(arr_cpy[i])
        elif (i == 5):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def RealValue_cons(array_data):  # mengubah data menjadi nilai sebenarnya (integer, float, dll)
    # input  : array_data : array of string
    # output : arr_cpy : array of (string and integer)

    # KAMUS LOKAL
    # array_data : array of string
    # i : integer
    # arr_cpy : (array of string) -> (array of (string and integer))

    # ALGORITMA
    arr_cpy = array_data[:]
    for i in range(5):
        if (i == 3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def RealValue_cons_history(array_data):  # mengubah data menjadi nilai sebenarnya (integer, float, dll)
    # input  : array_data : array of string
    # output : arr_cpy : array of (string and integer)

    # KAMUS LOKAL
    # array_data : array of string
    # i : integer
    # arr_cpy : (array of string) -> (array of (string and integer))

    # ALGORITMA
    arr_cpy = array_data[:]
    for i in range(5):
        if (i == 4):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def RealValue_gadget_borrow(array_data):  # mengubah data menjadi nilai sebenarnya (integer, float, dll)
    # input  : array_data : array of string
    # output : arr_cpy : array of (string, integer, and bool)

    # KAMUS LOKAL
    # array_data : array of string
    # i : integer
    # arr_cpy : (array of string) -> (array of (string, integer, and bool))

    # ALGORITMA
    arr_cpy = array_data[:]
    for i in range(7):
        if (i == 4):
            arr_cpy[i] = int(arr_cpy[i])
        elif (i == 5):
            if arr_cpy[i] == "True":
                arr_cpy[i] = True
            elif arr_cpy[i] == "False":
                arr_cpy[i] = False
        elif (i == 6):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def RealValue_gadget_return(array_data):  # mengubah data menjadi nilai sebenarnya (integer, float, dll)
    # input  : array_data : array of string
    # output : arr_cpy : array of (string and integer)

    # KAMUS LOKAL
    # array_data : array of string
    # i : integer
    # arr_cpy : (array of string) -> (array of (string and integer))

    # ALGORITMA
    arr_cpy = array_data[:]
    for i in range(4):
        if (i == 3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def LineToData(line):  # mengubah baris menjadi data yang bersih
    # input  : line : string
    # output : array_of_data : array of string

    # KAMUS LOKAL
    # raw_array_of_data, array of data : array of string

    # ALGORITMA
    raw_array_of_data = separate(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def show_datas():  # menampilkan isi variabel datas ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # datas, arr_cpy : array of (array of string)
    # header : array of string
    # i, j : integer

    # ALGORITMA
    print("-------------------datas-------------------")
    arr_cpy = datas[:]
    arr_cpy.insert(0, header)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def show_gadgets():  # menampilkan isi variabel gadgets ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # gadgets, arr_cpy : array of (array of (string and integer))
    # header_gadgets : array of string
    # i, j : integer

    # ALGORITMA
    print("-------------------gadgets-------------------")
    arr_cpy = gadgets[:]
    arr_cpy.insert(0, header_gadgets)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def show_cons():  # menampilkan isi variabel cons ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # cons, arr_cpy : array of (array of (string and integer))
    # header_cons : array of string
    # i, j : integer

    # ALGORITMA
    arr_cpy = cons[:]
    arr_cpy.insert(0, header_cons)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def show_cons_history():  # menampilkan isi variabel cons_history ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # cons_history, arr_cpy : array of (array of (string and integer))
    # header_cons_history : array of string
    # i, j : integer

    # ALGORITMA
    arr_cpy = cons_history[:]
    arr_cpy.insert(0, header_cons_history)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def show_gadget_borrow():  # menampilkan isi variabel gadget_borrow ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # gadget_borrow, arr_cpy : array of (array of (string, integer, and bool))
    # header_gadget_borrow : array of string
    # i, j : integer

    # ALGORITMA
    arr_cpy = gadget_borrow[:]
    arr_cpy.insert(0, header_gadget_borrow)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def show_gadget_return():  # menampilkan isi variabel gadget_return ke layar
    # input  : none
    # output : none

    # KAMUS LOKAL
    # gadget_return, arr_cpy = array of (array of (string and integer))
    # header_gadget_return = array of string
    # i, j : integer

    # ALGORITMA
    arr_cpy = gadget_return[:]
    arr_cpy.insert(0, header_gadget_return)
    for i in range(len(arr_cpy)):
        for j in arr_cpy[i]:
            print(j, end=' ')
        print('\r')

def convert_datas_to_string(temp_cpy, temp_header):  # mengubah data bersih (datas) menjadi file yang siap disimpan dalam csv
    # input  : temp_cpy : array of (array of string)
    #          temp_header : array of string
    # output : string

    # KAMUS LOKAL
    # string_data : string
    # arr_data, temp_header, arr_data_all_string : array of string
    # temp_cpy : array of (array of string)

    # ALGORITMA
    string_data = ";".join(temp_header) + "\n"
    for arr_data in temp_cpy:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def savefile(temp_datas, temp_header, filename):  # menyimpan data ke file
    # input  : temp_datas : array of (array of string)
    #          temp_header : array of string
    #          filename : string
    # output : none

    # KAMUS LOKAL
    # filename, newcsv, save_to_dir : string
    # temp_datas : array of (array of string)
    # temp_header : array of string

    # ALGORITMA
    newcsv = convert_datas_to_string(temp_datas, temp_header)
    f = open(save_to_dir + "\ ".strip() + filename, "w+")
    f.write(newcsv)
    f.close()

def loadfile(filename):  # meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel datas)
    # input  : filename : string
    # output : datas : array of (array of string)

    # KAMUS LOKAL
    # raw_line, filename, line, raw_header : string
    # raw_lines, lines, header, array_of_data : array of string
    # datas : array of (array of string)

    # ALGORITMA
    global header
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = LineToData(raw_header)
    for line in lines:
        array_of_data = LineToData(line)
        datas.append(array_of_data)
    return datas

def printdata(i):  # menampilkan indeks ke-i dari gadgets ke layar
    # input  : i : integer
    # output : none

    # KAMUS LOKAL
    # gadgets : array of (array of (string and integer))
    # i : integer

    # ALGORITMA
    print("\nNama              :",gadgets[i][1])
    print("Deskripsi         :",gadgets[i][2])
    print("ID gadget         :",gadgets[i][0])
    print("Jumlah            :",gadgets[i][3],"buah")
    print("Rarity            :",gadgets[i][4])
    print("Tahun Ditemukan   :",gadgets[i][5])

def loadfile_gadget(filename):  # meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel gadgets)
    # input  : filename : string
    # output : datas : array of (array of string)

    # KAMUS LOKAL
    # raw_header, line : string
    # header_gadgets, raw_lines, lines, raw_array : array of string
    # array_of_data : array of (string and integer)
    # datas : array of (array of string)

    # ALGORITMA
    global header_gadgets
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_gadgets = LineToData(raw_header)
    for line in lines:
        raw_array = LineToData(line)
        array_of_data = RealValue_gadget(raw_array)
        datas.append(array_of_data)
    return datas

def loadfile_cons(filename):  # fungsi yang meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel cons)
    # input  : filename : string
    # output : datas : array of (array of (string and integer))

    # KAMUS LOKAL
    # raw_header, raw_line, line, filename : string
    # header_cons, raw_lines, lines, raw_array : array of string
    # datas, array_of_data : array of (array of (string and integer))

    # ALGORITMA
    global header_cons
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_cons = LineToData(raw_header)
    for line in lines:
        raw_array = LineToData(line)
        array_of_data = RealValue_cons(raw_array)
        datas.append(array_of_data)
    return datas

def loadfile_cons_history(filename):  # fungsi yang meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel cons_history)
    # input  : filename : string
    # output : datas : array of (array of (string and integer))

    # KAMUS LOKAL
    # raw_header, raw_line, line, filename : string
    # header_cons_history, raw_lines, lines, raw_array : array of string
    # datas, array_of_data : array of (array of (string and integer))

    # ALGORITMA
    global header_cons_history
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_cons_history = LineToData(raw_header)
    for line in lines:
        raw_array = LineToData(line)
        array_of_data = RealValue_cons_history(raw_array)
        datas.append(array_of_data)
    return datas

def loadfile_gadget_borrow(filename):  # fungsi yang meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel gadget_borrow)
    global header_gadget_borrow
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_gadget_borrow = LineToData(raw_header)
    for line in lines:
        raw_array = LineToData(line)
        array_of_data = RealValue_gadget_borrow(raw_array)
        datas.append(array_of_data)
    return datas

def loadfile_gadget_return(filename):  # fungsi yang meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel gadget_return)
    global header_gadget_return
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_gadget_return = LineToData(raw_header)
    for line in lines:
        raw_array = LineToData(line)
        array_of_data = RealValue_gadget_return(raw_array)
        datas.append(array_of_data)
    return datas

def carinama_gadget(idx):  # menemukan nama dengan input indeks
    return (gadgets[idx][1])

def carinama_cons(idx):  # menemukan nama dengan input indeks
    return (cons[idx][1])

def cariindex_gadget(id):  # menemukan indeks (baris) dengan input id
    for i in range(len(gadgets)):
        if gadgets[i][0] == id:
            return i
    return "null"

def cariindex_datas(id):  # menemukan indeks (baris) dengan input id
    for i in range(len(datas)):
        if cons[i][0] == id:
            return i
    return "null"

def cariindex_cons(id):  # menemukan indeks (baris) dengan input id
    for i in range(len(cons)):
        if cons[i][0] == id:
            return i
    return "null"

def cariindex_cons_history(id):  # menemukan indeks (baris) dengan input id
    for i in range(len(cons_history)):
        if cons_history[i][0] == id:
            return i
    return "null"

def cariindex_borrow_history(id):  # menemukan indeks (baris) dengan input id
    for i in range(len(gadget_borrow)):
        if gadget_borrow[i][0] == id:
            return i
    return "null"

def cari_namauser(userid):  # menemukan nama user dengan input userid
    for i in range(len(datas)):
        if datas[i][0] == userid:
            nama = datas[i][2]
            return nama

def cari_namaconsumable(consid):  # menemmukan nama consumable dengan input consid
    for i in range(len(cons)):
        if cons[i][0] == consid:
            nama = cons[i][1]
            return nama

def cari_namagadget(gadgetid):  # menemukan nama gadget dengan input gadgetid
    for i in range(len(gadgets)):
        if gadgets[i][0] == gadgetid:
            nama = gadgets[i][1]
            return nama
    return ("ERROR(GADGET TIDAK DITEMUKAN)")

def cek_login(activeID):  #cek role login
    for i in range(len(datas)):
        if datas[i][0] == activeID:
            return datas[i][5]

def sort_cons_history():  #sort list berdasarkan entri terbaru
    lis = trueval(cons_history)
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][0] < lis[i][3][0]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][1] < lis[i][3][1]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][2] < lis[i][3][2]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    slashval(lis)
    return lis

def sort_gadget_borrow():  #sort list berdasarkan entri terbaru
    lis = trueval(gadget_borrow)
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][0] < lis[i][3][0]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][1] < lis[i][3][1]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][3][2] < lis[i][3][2]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    slashval(lis)
    return lis

def sort_gadget_return():  #sort list berdasarkan entri terbaru
    lis = trueval2(gadget_return)
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][2][0] < lis[i][2][0]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][2][1] < lis[i][2][1]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    for ran in range(len(lis)-1):
        imax = ran
        for i in range(ran+1,len(lis)):
            if lis[imax][2][2] < lis[i][2][2]:
                imax = i
        temp = lis[imax]
        lis[imax] = lis[ran]
        lis[ran] = temp
    slashval2(lis)
    return lis

def trueval(List):  # mengubah format DD/MM/YYYY menjadi list
    lis = List
    for i in range(len(List)):
        lis[i][3] = separate_date(List[i][3])
    return lis

def trueval2(List):  # mengubah format DD/MM/YYYY menjadi list
    lis = List
    for i in range(len(List)):
        lis[i][2] = separate_date(List[i][2])
    return lis

def slashval(List):  # mengubah format list menjadi DD/MM/YY
    lis = List
    for i in range(len(List)):
        lis[i][3] = str(List[i][3][0])+"/"+str(List[i][3][1])+"/"+str(List[i][3][2])
    return lis

def slashval2(List):  # mengubah format list menjadi DD/MM/YY
    lis = List
    for i in range(len(List)):
        lis[i][2] = str(List[i][2][0])+"/"+str(List[i][2][1])+"/"+str(List[i][2][2])
    return lis

def cekindex_cons(id):  # mencari consumable berdasarkan ID
    for i in range(len(cons)):
        if cons[i][0] == id:
            return True
    print("ID consumable tidak terdeteksi")
    print("ketik (cancel) untuk keluar")
    return False

def input_id():  # input id dengan validasi, cancel, dan rekurens
    indeks = False
    while indeks == False:
        id_cons = str(input("ID consumable (C_) ="))
        if id_cons == "cancel":
            id_cons = "cancel"
            return id_cons
        indeks = cekindex_cons(id_cons)
    return id_cons

def cek_date(date):  # validasi tanggal
	if date[2] >= 0:
		if date[1] in (1,3,5,7,8,10,12):
			if date[0] <= 31:
				return True
		elif date[1] in (4,6,9,11):
			if date[0] <= 30:
				return True
		elif date[1] == 2:
			if (date[2]%4) == 0:
				if date[0] <= 29:
					return True
			elif (date[2]%4) != 0:
				if date[0] <= 28:
					return True
	return False

def input_date():  # input date dengan rekurens dan validasi
	indeks = False
	while indeks == False:
		print("Format tanggal (DD/MM/YY)")
		date = (str(input("tanggal = ")))
		indeks = cek_date(separate_date(date)) #validasi
	return date

def validRegister(username):  # mengetes apakah user yang diregister valid (belum ada)
    for i in range(len(datas)):
        if datas[i][1] == username:
            return False
    return True

# F01: prosedur untuk menambahkan data user
def register():
    if (activerole != "Admin"):  # perlu role admin
        print("Untuk akses fungsi register diperlukan role ADMIN")
        return  # kembali ke program utama
    array = []
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    if not validRegister(username):
        print("Register gagal, username sudah dipakai")
        return  # kembali ke program utama
    password = input("Masukkan password: ")
    password = hash_pass(password)
    alamat = input("Masukkan alamat: ")
    id = "U" + str(len(datas) + 1)
    role = "User"
    array.append(id)
    array.append(username)
    array.append(nama.title())
    array.append(alamat)
    array.append(password)

    array.append(role)
    datas.append(array)
    print("User " + datas[-1][2] + " telah berhasil register ke dalam Kantong Ajaib.")

# F02: prosedur untuk login
def login():
    global activeID
    global activerole
    valid = False
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for i in range(len(datas)):
        if datas[i][1] == username:
            idx = i
            if datas[idx][4] == hash_pass(password):
                valid = True
    if valid:
        print("Halo " + datas[idx][2] + " selamat datang di Kantong Ajaib.")
        activeID = datas[idx][0]
        activerole = datas[idx][5]

    else:
        print("Gagal login")  # Gagal

# F03: prosedur mencari item berdasarkan rarity
def carirarity():
    if (activerole != "Admin") and (activerole != "User"):  # perlu login
        print("Silakan login terlebih dahulu")
        return  # kembali ke program utama
    R = input("Masukkan rarity gadget: ")

    empty = True
    for i in range(len(gadgets)):
        if (R == gadgets[i][4]) :
            empty = False
            printdata(i)
    if empty:
        print("Tidak ada item dengan rarity ", R)

# F04: mencari item berdasarkan tahun
def caritahun() :
    if (activerole != "Admin") and (activerole != "User"):  # perlu login
        print("Silakan login terlebih dahulu")
        return  # kembali ke program utama
    tahun = inputNomorValid("Masukkan tahun: ", 0, 9999)
    kategori = ''
    valid = False
    while not valid:
        kategori = input("Masukkan kategori: ")
        if (kategori == '>') or (kategori == '>=') or (kategori == '=') or (kategori == '<') or (kategori == '<='):  # validasi input
            valid = True
        else:
            print("input tidak valid")

    count = 0
    for i in range(len(gadgets)):
        if (kategori == '>') and ((gadgets)[i][5] > tahun):
            count+=1
            printdata(i)
        elif (kategori == '>=') and ((gadgets)[i][5] >= tahun):
            count+=1
            printdata(i)
        elif (kategori == '<') and ((gadgets)[i][5] < tahun):
            count+=1
            printdata(i)
        elif (kategori == '<=') and ((gadgets)[i][5] <= tahun):
            count+=1
            printdata(i)
        elif (kategori == '=') and ((gadgets)[i][5] == tahun):
            count+=1
            printdata(i)

    #  jika tidak ada data
    if count == 0:
        print("Tidak ada data yang sesuai")

# F05: prosedur melakukan penambahan item pada inventory
def tambahitem():
    if (activerole != "Admin"):  # hanya admin yang bisa akses
        print("Fitur ini memerlukan role admin")
        return  # kembali ke program utama
    print("-------------------TAMBAH ITEM-------------------")
    id = input("Masukkan ID: ")

    # validasi ID
    if (id[0] != 'G') and (id[0] != 'C'):
        print("Penambahan item gagal, input ID tidak sesuai. (ID diawali 'C' untuk consumable atau 'G' untuk gadget)")
        return  # kembali ke program utama

    if id[0] == 'G':
        for i in range(len(gadgets)):
            if gadgets[i][0] == id:
                print("Penambahan item gagal, id sudah ada dalam inventory gadget")
                return  # kembali ke program utama
    elif id[0] == 'C':
        for i in range(len(cons)):
            if cons[i][0] == id:
                print("Penambahan item gagal, id sudah ada dalam inventory consumable")
                return  # kembali ke program utama
    nama = input("Masukkan nama: ")
    deskripsi = input("Masukkan deskripsi: ")
    jumlah = inputNomorValid("Masukkan jumlah: ", 1, 99999999)



    #  validasi rarity
    valid = False
    while not valid:
        rarity = input("Masukkan rarity (S/A/B/C): ")
        if (rarity != 'S') and (rarity != 'A') and (rarity != 'B') and (rarity != 'C'):
            print("Input rarity tidak sesuai")
        else:
            valid = True


    # penambahan item sukses
    if id[0] == 'G':
        tahun = inputNomorValid("Masukkan tahun ditemukan: ", 0, 9999)

    # memasukkan data baru
    temp_data = []
    temp_data.append(id)
    temp_data.append(nama)
    temp_data.append(deskripsi)
    temp_data.append(jumlah)
    temp_data.append(rarity)
    if id[0] == 'G':
        temp_data.append(tahun)
        gadgets.append(temp_data)
        # output
        print("Gadget " + str(nama) + " dengan id(" + str(id) + ") telah berhasil ditambahkan ke kantong ajaib")
    elif id[0] == 'C':
        cons.append(temp_data)
        print("Consumable " + str(nama) + " dengan id(" + str(id) + ") telah berhasil ditambahkan ke kantong ajaib")

# F06: prosedur melakukan hapus item dari inventory
def hapusitem():
    if (activerole != "Admin"):  # hanya admin yang bisa akses
        print("Fitur ini memerlukan role admin")
        return  # kembali ke program utama
    print("-------------------HAPUS ITEM-------------------")

    id = input("Masukkan id: ")
    if id[0] == 'G':
        idx = cariindex_gadget(id)
    elif id[0] == 'C':
        idx = cariindex_cons(id)
    else:
        print("ID tidak sesuai")
        return  # kembali k eprogram utama

    if idx != "null":
        if id[0] == 'G':  # gadget
            nama = carinama_gadget(idx)
            valid = False
            while not valid:
                conf = input("Apakah anda yakin ingin menghapus " + str(nama) + " (Y/N): ")
                if (conf == 'Y') or (conf == 'N'):
                    valid = True
                else:
                    print("Input tidak sesuai")
            if conf == 'Y':
                del gadgets[idx]
                print("Item telah berhasil dihapus")
            else:
                print("Item batal dihapus")
        if id[0] == 'C':  # consumable
            nama = carinama_cons(idx)
            valid = False
            while not valid:
                conf = input("Apakah anda yakin ingin menghapus consumable " + str(nama) + " (Y/N): ")
                if (conf == 'Y') or (conf == 'N'):
                    valid = True
                else:
                    print("Input tidak sesuai")
            if conf == 'Y':
                del cons[idx]
                print("Consumable telah berhasil dihapus")
            else:
                print("Consumable batal dihapus")

    else:
        print("ID tidak ada dalam database")

# F07: prosedur melakukan pengubahan jumlah item pada inventory
def ubahjumlah():
    if (activerole != "Admin"):  # hanya admin yang bisa akses
        print("Fitur ini memerlukan role admin")
        return  # kembali ke program utama
    id = input("Masukkan id: ")
    if id[0] == 'G':
        idx = cariindex_gadget(id)
    elif id[0] == 'C':
        idx = cariindex_cons(id)
    else:
        print("Input id tidak sesuai")
        return  # kembali ke program utama
    if idx != "null":
        if id[0] == 'G':
            jumlah = inputNomorValid("Masukkan jumlah: ", -99999999, 99999999)
            ganti_jumlah_gadget(idx, jumlah)
        elif id[0] == 'C':
            jumlah = inputNomorValid("Masukkan jumlah: ", -99999999, 99999999)
            ganti_jumlah_cons(idx, jumlah)

    else:
        print("ID tidak ada dalam database")

def ganti_jumlah_gadget(idx, jumlah):  # mengubah jumlah item pada variabel gadgets
    if jumlah == 0:
        print("Jumlah " + str(gadgets[idx][1]) + " tidak berubah. Stok sekarang: " + str(gadgets[idx][3]))
    elif jumlah > 0:
        gadgets[idx][3] += jumlah
        print(str(jumlah) + ' ' + str(carinama_gadget(idx)) + " berhasil ditambah. Stok sekarang: " + str(gadgets[idx][3]))
    else:
        jumlah_baru = gadgets[idx][3] + jumlah
        if jumlah_baru < 0:
            print(str(abs(jumlah)) + ' ' + str(carinama_gadget(idx)) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(gadgets[idx][3]))
        else:
            gadgets[idx][3] = jumlah_baru
            print(str(abs(jumlah)) + ' ' + str(carinama_gadget(idx)) + " berhasil dibuang. Stok sekarang: " + str(gadgets[idx][3]))

def ganti_jumlah_cons(idx, jumlah):  # mengubah jumlah item pada variabel cons
    if jumlah == 0:
        print("Jumlah " + str(cons[idx][1]) + " tidak berubah. Stok sekarang: " + str(cons[idx][3]))
    elif jumlah > 0:
        cons[idx][3] += jumlah
        print(str(jumlah) + ' ' + str(carinama_cons(idx)) + " berhasil ditambah. Stok sekarang: " + str(cons[idx][3]))
    else:
        jumlah_baru = cons[idx][3] + jumlah
        if jumlah_baru < 0:
            print(str(abs(jumlah)) + ' ' + str(carinama_cons(idx)) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(cons[idx][3]))
        else:
            cons[idx][3] = jumlah_baru
            print(str(abs(jumlah)) + ' ' + str(carinama_cons(idx)) + " berhasil dibuang. Stok sekarang: " + str(cons[idx][3]))

# F08: prosedur untuk melakukan peminjaman gadget
def pinjam():
    if (activerole != "User") and (activerole != "Admin"):  # hanya boleh masuk ketika sudah login
        print("Silakan login terlebih dahulu")
        return  # kembali ke program utama
    print("-------------------PINJAM GADGET-------------------")
    id_gadget = input("ID gadget: ")
    idx = cariindex_gadget(id_gadget)

    if idx == "null":  # id tidak ditemukan
        print("Peminjaman gagal, ID gadget tidak ada dalam inventory")
        return  # kembali ke program utama
    nama = cari_namagadget(id_gadget)

    ### VERIFIKASI PENGAMBILAN GADGET SAMA
    for i in range(len(gadget_borrow)):  # mencari data peminjaman
        if (gadget_borrow[i][1] == activeID) and (gadget_borrow[i][2] == id_gadget) and (gadget_borrow[i][5] == False):  # ada peminjaman aktif
            print("Peminjaman gagal, anda sedang meminjam gadget tersebut (" + nama + ")")
            return  # kembali ke program utama


    jumlah = inputNomorValid("Jumlah gadget yang dipinjam: ", 1, 99999999)

    if gadgets[idx][3] - jumlah < 0:  # stok tidak cukup
        print("Peminjaman gagal, tidak tersedia cukup gadget")
        print("Stok saat ini, " + nama + " = " + str(gadgets[idx][3]))
        return  # kembali ke program utama

    tanggal = inputValidDate("Tanggal peminjaman (DD/MM/YYYY): ")


    # peminjaman berhasil
    id_pinjam = "GB" + str(len(gadget_borrow) + 2)  # membuat id pinjam
    gadgets[idx][3] -= jumlah  # mengubah jumlah
    print("Selamat, anda telah berhasil meminjam " + nama + " (" + str(jumlah) + "). Lakukan pengembalian saat sudah selesai")

    # memasukan ke data riwayat pinjam
    newdata = []
    newdata.append(id_pinjam)
    newdata.append(activeID)
    newdata.append(id_gadget)
    newdata.append(tanggal)
    newdata.append(jumlah)
    newdata.append(False)
    newdata.append(jumlah)
    gadget_borrow.append(newdata)

# F09: prosedur untuk mengembalikan gadget yang sudah dipinjam
def kembalikan():
    if (activerole != "User") and (activerole != "Admin"):  # hanya boleh masuk ketika sudah login
        print("Silakan login terlebih dahulu")
        return  # kembali ke program utama
    print("-------------------PENGEMBALIAN GADGET-------------------")
    datapinjam = []  # berisi data peminjaman (berbentuk indeks dalam variabel gadget_borrow) yang masih berlangsung

    for i in range(len(gadget_borrow)):  # mencari di data peminjaman gadget
        if (gadget_borrow[i][1] == activeID) and (gadget_borrow[i][5] == False):
            datapinjam.append(i)

    if datapinjam == []:  # data pinjam kosong
        print("Tidak ada peminjaman yang sedang berlangsung")
        return  # kembali ke program utama

    # menampilkan peminjaman yang berlangsung
    print("Berikut adalah daftar peminjaman yang masih berlangsung")
    print("*ketik 0 untuk batal")
    for i in range(len(datapinjam)):
        sisa_pinjam = gadget_borrow[datapinjam[i]][6]
        temp_id_gadget = gadget_borrow[datapinjam[i]][2]
        temp_nama_gadget = cari_namagadget(temp_id_gadget)
        print(str(i+1) + ") " + temp_nama_gadget + " (" + str(sisa_pinjam) + ")")
    print("")

    nomor = inputNomorValid("Nomor peminjaman :", 0, len(datapinjam))
    if nomor == 0:
        print("Pengemalian dibatalkan")
        return  # kembali ke program utama


    # pilih opsi pengembalian
    print("Pilih opsi pengembalian")
    print("1) Kembalikan seluruhnya")
    print("2) Kembalikan dengan jumlah tertentu")
    opt = inputNomorValid("Masukkan pilihan: ", 1, 2)
    # pengisian dan pengubahan data
    idx_pinjam = datapinjam[nomor-1]
    id_pinjam = gadget_borrow[idx_pinjam][0]
    id_gadget = gadget_borrow[idx_pinjam][2]
    idx_gadget = cariindex_gadget(id_gadget)
    nama_gadget = carinama_gadget(idx_gadget)

    if opt == 1:
        jumlah_kembali = gadget_borrow[idx_pinjam][6]

    elif opt == 2:
        jumlah_kembali = inputNomorValid("Masukkan jumlah yang ingin dikembalikan: ", 1, gadget_borrow[idx_pinjam][6])
    tanggal = inputValidDate("Masukkan tanggal pengembalian (DD/MM/YYYY): ")


    gadgets[idx_gadget][3] = gadgets[idx_gadget][3] + jumlah_kembali  # mengubah jumlah gadget
    gadget_borrow[idx_pinjam][6] = gadget_borrow[idx_pinjam][6] - jumlah_kembali # mengubah sisa pinjam
    if gadget_borrow[idx_pinjam][6] == 0: # mengubah status pinjam bila seluruhnya dikembalikan
        gadget_borrow[idx_pinjam][5] = True

    # menambahkan riwayat pengembalian
    newline = []
    id_return = "RT" + str(len(gadget_return) + 1)
    newline.append(id_return)
    newline.append(id_pinjam)
    newline.append(tanggal)
    newline.append(jumlah_kembali)
    gadget_return.append(newline)

    # output
    print("")
    print("Pengembalian " + nama_gadget + " (" + str(jumlah_kembali) + ") telah berhasil")

# F10: prosedur untuk meminta consumable
def minta():
    if (activerole == "Admin") or (activerole == "User"): #cek role ID
        id_cons = input_id()
        if id_cons == "cancel":
            return
        jumlah = int(input("jumlah consumable = "))
        if (cons[cariindex_cons(id_cons)][3]) >=jumlah:
            temp_data = []
            id_his = "PC" + str(len(cons_history)+1) #generator ID transaksi
        else:
            print("Jumlah consumable tidak memenuhi")
            print(id_cons," tersisa ",cons[cariindex_cons(id_cons)][3])
            return
        date = inputValidDate("Masukkan tanggal (DD/MM/YYYY): ")
        cons_idx = cariindex_cons(id_cons)

        #ubah jumlah
        cons[cons_idx][3] = cons[cons_idx][3] - jumlah

        print(cons[cariindex_cons(id_cons)][1] + " (" + str(jumlah) + ") berhasil diminta " + "stok sekarang = " + str(cons[cons_idx][3]))

        temp_data.append(id_his)
        temp_data.append(activeID)
        temp_data.append(id_cons)
        temp_data.append(date)
        temp_data.append(jumlah)
        cons_history.append(temp_data)
    else:
        print("Silakan login terlebih dahulu")
        return

# F11: prosedur untuk menampilkan riwayat peminjaman gadget
def riwayatpinjam():
    if activerole == "Admin": #cek role ID
        List = sort_gadget_borrow() #sort dari entri terbaru
        i = 0
        indeks = 0
        while i < 5:
            if indeks < len(List):
                print("ID Peminjaman   : ",List[indeks][0])
                print("Nama peminjam   : ",cari_namauser(List[indeks][1]))
                print("Nama gadget     : ",cari_namagadget(List[indeks][2]))
                print("Tanggal         : ",List[indeks][3])
                print("Jumlah          : ",List[indeks][4])
                print("--------------------------------------")
                i += 1
                indeks += 1
            else:
                print('')
                print('Akhir dari riwayat')
                return
        while indeks < len(List): #rekurens jika data lebih dari 5
            loop = True
            while loop:
                opt = input("Tunjukkan Lebih (Y/N) = ")
                if opt == 'Y':
                    loop = False
                    i = 0
                    while i < 5:
                        if indeks < len(List):
                            print("ID Peminjaman   : ",List[indeks][0])
                            print("Nama peminjam   : ",cari_namauser(List[indeks][1]))
                            print("Nama gadget     : ",cari_namagadget(List[indeks][2]))
                            print("Tanggal         : ",List[indeks][3])
                            print("Jumlah          : ",List[indeks][4])
                            print("--------------------------------------")
                            i += 1
                            indeks += 1
                        else:
                            print('')
                            print('Akhir dari riwayat')
                            return
                elif opt == 'N':
                    return
                else:
                    print("input tidak valid")
    elif activerole == "User":
        print("Untuk akses fungsi riwayat pinjam diperlukan role ADMIN")
    else:
    	print("Silakan login terlebih dahulu")
    	return

# F12: prosedur untuk menampilkan riwayat pengembalian gadget
def riwayatkembali():
    if activerole == "Admin": #cek role ID
        List = sort_gadget_return() #sort dari entri terbaru
        i = 0
        indeks = 0
        while i < 5:
            if indeks < len(List):
                gadget_borrow_indeks = cariindex_borrow_history((List[indeks][1]))
                total_pinjam = gadget_borrow[gadget_borrow_indeks][4]
                sisa_pinjam = gadget_borrow[gadget_borrow_indeks][6]
                total_kembali = total_pinjam - sisa_pinjam
                print("ID Pengembalian   : ",List[indeks][0])
                print("Nama peminjam     : ",cari_namauser(gadget_borrow[gadget_borrow_indeks][1]))
                print("Nama gadget       : ",cari_namagadget(gadget_borrow[gadget_borrow_indeks][2]))
                print("Tanggal           : ",List[indeks][2])
                print("Jumlah kembali    :  " + str(List[indeks][3]) + " (" + str(total_kembali) + "/" + str(total_pinjam) + ")", end=' ')
                if (sisa_pinjam == 0):
                    print("peminjaman selesai")
                else:
                    print("")
                print("--------------------------------------")
                i += 1
                indeks += 1
            else:
                print('')
                print('Akhir dari riwayat')
                return
        while indeks < len(List): #rekurens jika data lebih dari 5
            loop = True
            while loop:
                opt = input("Tunjukkan Lebih (Y/N) = ")
                if opt == 'Y':
                    loop = False
                    i = 0
                    while i < 5:
                        if indeks < len(List):
                            gadget_borrow_indeks = cariindex_borrow_history((List[indeks][1]))
                            total_pinjam = gadget_borrow[gadget_borrow_indeks][4]
                            sisa_pinjam = gadget_borrow[gadget_borrow_indeks][6]
                            total_kembali = total_pinjam - sisa_pinjam
                            print("ID Pengembalian   : ", List[indeks][0])
                            print("Nama peminjam     : ", cari_namauser(gadget_borrow[gadget_borrow_indeks][1]))
                            print("Nama gadget       : ", cari_namagadget(gadget_borrow[gadget_borrow_indeks][2]))
                            print("Tanggal           : ", List[indeks][2])
                            print(
                                "Jumlah kembali    :  " + str(List[indeks][3]) + " (" + str(total_kembali) + "/" + str(total_pinjam) + ")", end=' ')
                            if (sisa_pinjam == 0):
                                print("*peminjaman selesai")
                            else:
                                print("")
                            print("--------------------------------------")
                            i += 1
                            indeks += 1
                        else:
                            print('')
                            print('Akhir dari riwayat')
                            return
                elif opt == 'N':
                    return
                else:
                    print("input tidak valid")
    elif activerole == "User":
        print("Untuk akses fungsi riwayat pinjam diperlukan role ADMIN")
    else:
    	print("Silakan login terlebih dahulu")
    	return

# F13: prosedur untuk menampilkan riwayat pengambilan consumable
def riwayatambil():
    if activerole == "Admin": #cek Role ID
        List = sort_cons_history() #sort dari entri terbaru
        i = 0
        indeks = 0
        while i < 5:
            if indeks < len(List):
                print("ID Pengambilan   : ",List[indeks][0])
                print("Nama Pengambil   : ",cari_namauser(List[indeks][1]))
                print("Nama consumable  : ",cari_namaconsumable(List[indeks][2]))
                print("Tanggal          : ",List[indeks][3])
                print("Jumlah           : ",List[indeks][4])
                print("--------------------------------------")
                i += 1
                indeks += 1
            else:
                print('')
                print('Akhir dari riwayat')
                return
        while indeks < len(List): #rekurens jika data lebih dari 5
            loop = True
            while loop:
                opt = input("Tunjukkan Lebih (Y/N) = ")
                if opt == 'Y':
                    i = 0
                    while i < 5:
                        if indeks < len(List):
                            print("ID Pengambilan   : ",List[indeks][0])
                            print("Nama Pengambil   : ",cari_namauser(List[indeks][1]))
                            print("Nama consumable  : ",cari_namaconsumable(List[indeks][2]))
                            print("Tanggal          : ",List[indeks][3])
                            print("Jumlah           : ",List[indeks][4])
                            print("--------------------------------------")
                            i += 1
                            indeks += 1
                        else:
                            print('')
                            print('Akhir dari riwayat')
                            return
                elif opt == 'N':
                    return
                else:
                    print("input tidak valid")
    elif activerole == "User":
        print("Untuk akses fungsi riwayat pinjam diperlukan role ADMIN")
    else:
    	print("Silakan login terlebih dahulu")
    	return

# FB1: melakukan hashing pada password
def hash_pass(password):
    hashed = []
    for i in range(len(password)):
        k = ord(password[i])
        k = round((k*k)/(len(password))+len(password))
        k = str(k)
        hashed.append(k)
    hashed = ''.join(hashed)
    return hashed

def back_dir(my_dir):  # kembali ke directory di atasnya
    temp = my_dir.split("\ ".strip())
    temp.pop(-1)
    return ("\ ".strip()).join(temp)

def is_right_dir(my_dir):  # mengecek apakah directory valid
    if not(os.path.exists(my_dir + "\{}".format("consumable_history.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("consumable.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("gadget_borrow_history.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("gadget_return_history.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("gadget.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("user.csv"))):
        return False
    elif not(os.path.exists(my_dir + "\{}".format("item_upgrade.csv"))):
        return False
    else:
        return True

def get_missing_file(my_dir):  # menampilkan file-file yang tidak terdapat pada directory yang tidak valid
    missing_file = []
    if not(os.path.exists(my_dir + "\{}".format("consumable_history.csv"))):
        missing_file += ["consumable_history.csv"]
    if not(os.path.exists(my_dir + "\{}".format("consumable.csv"))):
        missing_file += ["consumable.csv"]
    if not(os.path.exists(my_dir + "\{}".format("gadget_borrow_history.csv"))):
        missing_file += ["gadget_borrow_history.csv"]
    if not(os.path.exists(my_dir + "\{}".format("gadget_return_history.csv"))):
        missing_file += ["gadget_return_history.csv"]
    if not(os.path.exists(my_dir + "\{}".format("gadget.csv"))):
        missing_file += ["gadget.csv"]
    if not(os.path.exists(my_dir + "\{}".format("user.csv"))):
        missing_file += ["user.csv"]
    if not(os.path.exists(my_dir + "\{}".format("item_upgrade.csv"))):
        missing_file += ["item_upgrade.csv"]
    return missing_file

def select_load_dir():  # prosedur untuk memilih load directory
    my_dir = current_dir
    print("\nSilakan memilih directory penyimpanan")
    IsStop = False
    while IsStop == False:
        print("Directory saat ini:", my_dir)
        walk_dir = str(input("Lanjutkan ke directory: (Tuliskan HELP! untuk menampilkan petunjuk)\n>> "))
        if walk_dir == "HELP!":
            print("=" * 10, "PETUNJUK", "=" * 10)
            print("BACK!      -- Menuju directory di atasnya")
            print("CHOOSE!    -- Memilih directory saat ini")
            print("HELP!      -- Menampilkan petunjuk")
            print("SHOW_FILE! -- Menampilkan file yang tersedia")
            print("SHOW_SDIR! -- Menampilkan sub directory yang tersedia")
            print()
        elif walk_dir == "BACK!":
            my_dir = back_dir(my_dir)    
        elif walk_dir == "CHOOSE!":
            print("Anda memilih directory {}".format(my_dir))
            IsStop = True
        elif walk_dir == "SHOW_SDIR!":
            print("Sub directory yang tersedia:")
            i = 1
            for dir in (next(os.walk(my_dir + ("\ ").strip()))[1]):
                print(i, dir)
                i += 1
            print()
        elif walk_dir == "SHOW_FILE!":
            print("File yang tersedia:")
            i = 1
            for dir in (next(os.walk(my_dir + ("\ ").strip()))[2]):
                print(i, dir)
                i += 1
            print()
        else:
            if os.path.exists(my_dir + "\{}".format(walk_dir)) and os.path.isdir(my_dir + "\{}".format(walk_dir)):
                my_dir = my_dir + "\{}".format(walk_dir)
            elif os.path.exists(my_dir + walk_dir) and os.path.isdir(my_dir + walk_dir):
                my_dir = my_dir + walk_dir
            elif os.path.exists(my_dir + "\{}".format(walk_dir)) and os.path.isfile(my_dir + "\{}".format(walk_dir)):
                print("File tidak dapat dipilih sebagai directory")
            else:
                print("Directory {} tidak ditemukan".format(my_dir + "\{}".format(walk_dir)))
            print()

    if is_right_dir(my_dir):
        print("Directory Kantong Ajaib Valid.")
        return (my_dir + "\ ".strip())
    else:
        print("Directory tidak valid. File-file berikut tidak ditemukan:")
        print(get_missing_file(my_dir))

# F14: prosedur untuk meload data
def load_kantong_ajaib_data():
    global current_dir, datas, gadgets, cons, cons_history, gadget_borrow, gadget_return, upgrades
    my_dir = None
    while my_dir == None:
        my_dir = select_load_dir()
    current_dir = my_dir
    datas = loadfile(my_dir + "user.csv") 
    gadgets = loadfile_gadget(my_dir + "gadget.csv")
    cons = loadfile_cons(my_dir + "consumable.csv")
    cons_history = loadfile_cons_history(my_dir + "consumable_history.csv")
    gadget_borrow = loadfile_gadget_borrow(my_dir + "gadget_borrow_history.csv")
    gadget_return = loadfile_gadget_return(my_dir + "gadget_return_history.csv")
    upgrades = loadfile_upgrades(my_dir + "item_upgrade.csv")

def select_save_dir():  # memilih save directory
    my_dir = current_dir
    print("\nSilakan memilih directory penyimpanan")
    IsStop = False
    while IsStop == False:
        print("Directory saat ini:", my_dir)
        walk_dir = str(input("Lanjutkan ke directory: (Tuliskan HELP! untuk menampilkan petunjuk)\n>> "))
        if walk_dir == "HELP!":
            print("=" * 10, "PETUNJUK", "=" * 10)
            print("BACK!      -- Menuju directory di atasnya")
            print("CHOOSE!    -- Memilih directory saat ini")
            print("HELP!      -- Menampilkan petunjuk")
            print("SHOW_FILE! -- Menampilkan file yang tersedia")
            print("SHOW_SDIR! -- Menampilkan sub directory yang tersedia")
            print()
        elif walk_dir == "BACK!":
            my_dir = back_dir(my_dir)    
        elif walk_dir == "CHOOSE!":
            print("Anda memilih directory {}".format(my_dir))
            IsStop = True
        elif walk_dir == "SHOW_SDIR!":
            print("Sub directory yang tersedia:")
            i = 1
            for dir in (next(os.walk(my_dir + ("\ ").strip()))[1]):
                print(i, dir)
                i += 1
            print()
        elif walk_dir == "SHOW_FILE!":
            print("File yang tersedia:")
            i = 1
            for dir in (next(os.walk(my_dir + ("\ ").strip()))[2]):
                print(i, dir)
                i += 1
            print()
        else:
            if os.path.exists(my_dir + "\{}".format(walk_dir)) and os.path.isdir(my_dir + "\{}".format(walk_dir)):
                my_dir = my_dir + "\{}".format(walk_dir)
            elif os.path.exists(my_dir + walk_dir) and os.path.isdir(my_dir + walk_dir):
                my_dir = my_dir + walk_dir
            elif os.path.exists(my_dir + "\{}".format(walk_dir)) and os.path.isfile(my_dir + "\{}".format(walk_dir)):
                print("File tidak dapat dipilih sebagai directory")
            else:
                print("Directory {} tidak ditemukan".format(my_dir + "\{}".format(walk_dir)))
            print()
    return (my_dir + "\ ".strip())

# F14: prosedur untuk menyimpan data
def save_kantong_ajaib_data():
    global save_to_dir
    save_to_dir = current_dir
    is_change_dir = "Y"
    while is_change_dir == "y" or is_change_dir == "Y":
        confirm_save = input("Anda akan menyimpan file ke directory {}, lanjutkan? (Y/N)\n>> ".format(save_to_dir))
        if confirm_save == "y" or confirm_save == "Y":
            savefile(datas, header,"user.csv")
            savefile(gadgets, header_gadgets, "gadget.csv")
            savefile(cons, header_cons, "consumable.csv")
            savefile(cons_history, header_cons_history, "consumable_history.csv")
            savefile(gadget_borrow, header_gadget_borrow, "gadget_borrow_history.csv")
            savefile(gadget_return, header_gadget_return, "gadget_return_history.csv")
            print("Perubahan pada data telah disimpan pada directory {}".format(save_to_dir))
            is_change_dir = "N"
        else:
            is_change_dir = input("Apakah Anda ingin mengganti directory penyimpanan? (Y/N)\n>> ")
            if is_change_dir == "y" or is_change_dir == "Y":
                save_to_dir = select_save_dir()
            else:
                print("Perubahan pada data tidak disimpan")

# F16: prosedur untuk menampilkan help
def help_me():
    print("=" * 20, "DAFTAR PERINTAH", "=" * 20)
    print("1) Register -- Mendaftarkan pengguna baru (khusus admin)")
    print("2) Login -- Masuk ke sistem sebagai user atau admin")
    print("3) Cari gadget -- Mencari gadget tertentu berdasarkan tahun atau rarity")
    print("4) Request Item -- Berisi fitur untuk meminjam gadget, megembalikan gadget, atau meminta consumable")
    print("   Pinjam Gadget -- Meminjam gadget")
    print("   Kembalikan Gagdet -- Mengembalikan gadget")
    print("   Minta Consumable -- Meminta consumable")
    print("   Upgrade Item - NEW! -- Mengupgrade item")
    print("5) Inventory Manager -- Berisi fitur-fitur untuk mengubah data inventory (khusus admin)")
    print("   Hapus Item -- Menghapus item dari inventory (khusus admin)")
    print("   Ubah Jumlah -- Menambahkan atau mengurangi jumlah item (khusus admin)")
    print("6) Riwayat inventory -- Fitur untuk melihat riwayat-riwayat pada inventory (khusus admin)")
    print("   Riwayat pinjam -- melihat riwayat peminjaman gadget")
    print("   Riwayat kembali -- melihat riwayat pengembalian gadget")
    print("   Riwayat consumable -- melihat riwayat permintaan consumable")
    print("7) Save data -- Menyimpan perubahan pada data")
    print("8) Load data -- Meload data dalam folder")
    print("9) help -- Menampilkan petunjuk penggunaan sistem")
    print("10) exit -- Keluar dari kantong ajaib")

# F17: prosedur untuk keluar dari program
def exit_program():
    is_save = input("Apakah Anda ingin menyimpan perubahan pada data? (Y/N)\n>> ")
    if is_save == "y" or is_save == "Y":
        save_kantong_ajaib_data()
        print("Anda telah keluar dari kantong ajaib. Doremonangis mengucapkan terima kasih. :)")
        exit()
    else:
        exit()

def loadfile_upgrades(filename):  # meload data "filename" dan mengembalikan data bersih berupa array (untuk variabel upgrades)
    global header_upgrades
    datas = []
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header_upgrades = LineToData(raw_header)
    for line in lines:
        array_of_data = LineToData(line)
        datas.append(array_of_data)
    return datas

def show_inventory():  # menampilkan ringkasan inventory
    print("-------------------Ringkasan Inventory-------------------")
    for line in cons:
        print("{}) {} (Rarity {}) ({})".format(line[0], line[1], line[4], line[3]))
        
def show_upgrades():  # menampilkan kemungkinan upgrade
    print("-------------------Kemungkinan Upgrade-------------------")
    print("\n-------------------Item dengan Rarity S-------------------\n")
    for upgrades in filter_upgrade_rarity("S"):
        print("Nama: {}".format(upgrades[0]))
        print("Deskripsi: {}\n".format(upgrades[1]))
    print("\n-------------------Item dengan Rarity A-------------------\n")
    for upgrades in filter_upgrade_rarity("A"):
        print("Nama: {}".format(upgrades[0]))
        print("Deskripsi: {}\n".format(upgrades[1]))
    print("\n-------------------Item dengan Rarity B-------------------\n")
    for upgrades in filter_upgrade_rarity("B"):
        print("Nama: {}".format(upgrades[0]))
        print("Deskripsi: {}\n".format(upgrades[1]))
    print("\n-------------------Item dengan Rarity C-------------------\n")
    for upgrades in filter_upgrade_rarity("C"):
        print("Nama: {}".format(upgrades[0]))
        print("Deskripsi: {}\n".format(upgrades[1]))

def show_materials():  # menampilkan material yang akan digunakan untuk upgrade
    print("-------------------Material untuk Upgrade-------------------")
    for line in materials:
        if line[3] != 0:
            print("{}) {} (Rarity {}) ({})".format(line[0], line[1], line[4], line[3]))
    print("-----------------------------------------------------------")
    print()

def filter_upgrade_rarity(item_rarity):  # memfilter kemungkinan upgrade berdasarkan rarity
    filtered_item = []
    for item in upgrades:
        if item[2] == item_rarity:
            filtered_item.append(item)
    return filtered_item

def get_item_indeks():  # mendapatkan indeks item
    while True:
        indeks = input("Masukkan ID item yang ingin dijadikan material:\n>> ")
        for line in cons:
            if line[0] == indeks:
                return indeks
        print("Item dengan indeks {} tidak ditemukan".format(indeks))

def get_material_indeks():  # mendapatkan indeks material
    while True:
        indeks = input("Masukkan ID material yang ingin dikurangi:\n>> ")
        for line in materials:
            if line[0] == indeks:
                return indeks
        print("Item dengan indeks {} tidak ditemukan".format(indeks))

def get_item_value(item_indeks):  # mendapatkan jumlah item yang akan dijadikan material
    for line in cons:
        if line[0] == item_indeks:
            print("Terdapat {} item {} (Rarity {})".format(line[3], line[1], line[4]))
            while True:
                value = input("Masukkan banyaknya item yang ingin dijadikan material:\n>> ")
                if isInteger(value):
                    if int(value) >= 0:
                        if int(value) <= line[3]:
                            return int(value)
                        else:
                            print("Hanya terdapat {} item {} (Rarity {})".format(line[3], line[1], line[4]))
                    else:
                        print("Masukan harus berupa bilangan bulat positif atau nol")
                else:
                    print("Masukan harus berupa bilangan bulat positif atau nol")

def get_material_value(item_indeks):  # mendapatkan jumlah item yang akan dikembalikan dari material
    for line in materials:
        if line[0] == item_indeks:
            print("Terdapat {} item {} (Rarity {}) yang dijadikan material".format(line[3], line[1], line[4]))
            while True:
                value = input("Masukkan banyaknya item yang ingin dikurangi dari material:\n>> ")
                if isInteger(value):
                    if int(value) >= 0:
                        if int(value) <= line[3]:
                            return int(value)
                        else:
                            print("Hanya terdapat {} item {} (Rarity {})".format(line[3], line[1], line[4]))
                    else:
                        print("Masukan harus berupa bilangan bulat positif atau nol")
                else:
                    print("Masukan harus berupa bilangan bulat positif atau nol")

def get_item_name(item_indeks):  # mendapatkan nama item dari indeks
    for line in cons:
        if line[0] == item_indeks:
            name = line[1]
            return name

def get_item_rarity(item_indeks):  # mendapatkan rarity item dari indeks
    for line in cons:
        if line[0] == item_indeks:
            rarity = line[4]
            return rarity

def tambahkan_material():  # menambahkan material untuk upgrade
    is_stop = "N"
    while is_stop != "Y" and is_stop != "y":
        item_indeks = get_item_indeks()
        item_name = get_item_name(item_indeks)
        item_rarity = get_item_rarity(item_indeks)
        item_value = get_item_value(item_indeks)
        for line in cons:
            if line[0] == item_indeks:
                line[3] = line[3] - item_value
        is_added = False
        for line in materials:
            if line[0] == item_indeks:
                line[3] = line[3] + item_value
                is_added = True
        if is_added == False:
            for line in cons:
                if line[0] == item_indeks:
                    line_cpy = line[:]
                    line_cpy[3] = item_value
                    materials.append(line_cpy)
        print("{} {} (Rarity {}) berhasil ditambahkan sebagai material".format(item_value, item_name, item_rarity))
        is_stop = input("Apakah material yang ditambahkan sudah cukup? (Y/N)\n>> ")

def kurangi_material():  # mengembalikan material upgrade ke inventory
    is_stop = "N"
    while is_stop != "Y" and is_stop != "y":
        item_indeks = get_material_indeks()
        item_name = get_item_name(item_indeks)
        item_rarity = get_item_rarity(item_indeks)
        item_value = get_material_value(item_indeks)
        for line in cons:
            if line[0] == item_indeks:
                line[3] = line[3] + item_value
        is_added = False
        for line in materials:
            if line[0] == item_indeks:
                line[3] = line[3] - item_value
        print("{} {} (Rarity {}) berhasil dikembalikan ke inventory".format(item_value, item_name, item_rarity))
        is_stop = input("Apakah material yang dikurangi sudah cukup? (Y/N))\n>> ")

def calculate_number_for_rarity():  # menghitung peluang mendapatkan masing-masing rarity item
    global rarity_S_number, rarity_A_number, rarity_B_number, rarity_C_number, divider
    count_S = hitung_material_dengan_rarity("S")
    count_A = hitung_material_dengan_rarity("A")
    count_B = hitung_material_dengan_rarity("B")
    count_C = hitung_material_dengan_rarity("C")
    if count_S != 0:
        rarity_S_number = base_rarity_S_number + 2000*count_S + 200*count_A + 20*count_B + 2*count_C
        rarity_A_number = base_rarity_A_number
        rarity_B_number = base_rarity_B_number
        rarity_C_number = base_rarity_C_number
    elif count_A != 0:
        rarity_S_number = base_rarity_S_number + 2000*count_A + 200*count_B + 20*count_C
        rarity_A_number = base_rarity_A_number + 1000*count_A + 100*count_B + 10*count_C
        rarity_B_number = base_rarity_B_number
        rarity_C_number = base_rarity_C_number
    elif count_B != 0:
        rarity_S_number = base_rarity_S_number + 200*count_B + 20*count_C
        rarity_A_number = base_rarity_A_number + 2000*count_B + 200*count_C
        rarity_B_number = base_rarity_B_number + 1000*count_B + 100*count_C
        rarity_C_number = base_rarity_C_number
    elif count_C != 0:
        rarity_S_number = base_rarity_S_number + 20*count_C
        rarity_A_number = base_rarity_A_number + 200*count_C
        rarity_B_number = base_rarity_B_number + 2000*count_C
        rarity_C_number = base_rarity_C_number + 1000*count_C
    else:
        rarity_S_number = 0
        rarity_A_number = 0
        rarity_B_number = 0
        rarity_C_number = 0
    divider = fail_number + rarity_S_number + rarity_A_number + rarity_B_number + rarity_C_number

def show_rarity_chance():  # menampilkan kemungkinan mendapatkan masing-masing rarity
    calculate_number_for_rarity()
    print("Peluang rarity S: {} %".format(round(100 * rarity_S_number/divider, 2)))
    print("Peluang rarity A: {} %".format(round(100 * rarity_A_number/divider, 2)))
    print("Peluang rarity B: {} %".format(round(100 * rarity_B_number/divider, 2)))
    print("Peluang rarity C: {} %".format(round(100 * rarity_C_number/divider, 2)))
    print("Peluang gagal: {} %".format(round(100 * fail_number/divider, 2)))

def hitung_material_dengan_rarity(nilai_rarity):  # menghitung banyaknya item dengan rarity tertentu yang akan dijadikan material
    count = 0
    for line in materials:
        if line[4] == nilai_rarity:
            count += int(line[3])
    return count

def get_gacha_number():  # mendapatkan nomor gacha
    gacha_number = ""
    for num in str(datetime.datetime.now()):
        if isInteger(num):
            gacha_number += str(num)
    gacha_number = int(gacha_number)
    for i in range (100):
        gacha_number = (2 * gacha_number) % divider
    return gacha_number

def get_gacha_rarity(gacha_number): # mendapatkan rarity item dari nomor gacha
    if gacha_number > rarity_S_number:
        gacha_number = gacha_number - rarity_S_number
        if gacha_number > rarity_A_number:
            gacha_number = gacha_number - rarity_A_number
            if gacha_number > rarity_B_number:
                gacha_number = gacha_number - rarity_B_number
                if gacha_number > rarity_C_number:
                    return "Fail"
                else:
                    return "C"
            else:
                return "B"
        else:
            return "A"
    else:
        return "S"

def get_gacha_item(gacha_number, item_rarity):  # mendapatkan item spesifik dengan rarity terentu
    if item_rarity != "Fail":
        item_count = len(filter_upgrade_rarity(item_rarity))
        item_number = gacha_number % item_count
        upgraded_item = filter_upgrade_rarity(item_rarity)[item_number]
        print("Selamat, Anda mendapatkan {} (Rarity {})".format(upgraded_item[0], upgraded_item[2]))
        is_added = False
        for line in cons:
            if line[1] == upgraded_item[0]:
                line[3] += 1
                is_added = True
        if is_added == False:
            new_ID = "C" + str(len(cons) + 1)
            temp_data = []
            temp_data.append(new_ID, upgraded_item[0], upgraded_item[1], 1, upgraded_item[2])
        return upgraded_item
    else:
        print("Yah, upgrade gagal dan semua material telah hilang")

def reset_gacha():  # mereset variabel-variabel gacha yang perlu direset
    global rarity_S_number, rarity_A_number, rarity_B_number, rarity_C_number, divider, materials
    rarity_S_number = base_rarity_S_number
    rarity_A_number = base_rarity_A_number
    rarity_B_number = base_rarity_B_number
    rarity_C_number = base_rarity_C_number
    divider = fail_number
    materials = []

def do_gacha():  # menjalankan mesin upgrade
    gacha_number = get_gacha_number()
    gacha_rarity = get_gacha_rarity(gacha_number)
    gacha_item = get_gacha_item(gacha_number, gacha_rarity)
    reset_gacha()

# FB3: prosedur untuk melakukan upgrade item
def play_gacha():
    if (activerole != "Admin") and (activerole != "User"):
        print("Silakan login terlebih dahulu")
        return
    is_stop = False
    while is_stop != True:
        print("-------------------Upgrade-------------------")
        print("1) Tampilkan Ringkasan Inventory")
        print("2) Tampilkan Kemungkinan Upgrade")
        print("3) Tambahkan Material")
        print("4) Kurangi Material")
        print("5) Tampilkan Material dan Peluang")
        print("6) Jalankan Mesin Upgrade")
        print("7) Kembali ke Main Menu")
        gacha_opt = input("Masukkan pilihan:\n>> ")
        if gacha_opt == "1":
            show_inventory()
        if gacha_opt == "2":
            show_upgrades()
        if gacha_opt == "3":
            tambahkan_material()
            calculate_number_for_rarity()
        if gacha_opt == "4":
            kurangi_material()
            calculate_number_for_rarity()
        if gacha_opt == "5":
            show_materials()
            show_rarity_chance()
        if gacha_opt == "6":
            do_gacha()
        if gacha_opt == "7":
            is_stop = True

# Inisialisasi variabel pada program
activeID = ()
activerole = ()
current_dir = os.getcwd()
materials = []
fail_number = 30000
base_rarity_S_number = 1000
base_rarity_A_number = 2000
base_rarity_B_number = 3000
base_rarity_C_number = 4000
calculate_number_for_rarity()
load_kantong_ajaib_data()

# PROGRAM UTAMA
loop = True
while loop:
    print("")
    print("-------------------KANTONG AJAIB-------------------")
    if activeID != ():
        print(cari_namauser(activeID) + " (" + activerole + ")")
    else:
        print("Belum login")
    print("1) Register")
    print("2) Login")
    print("3) Cari gadget")
    print("4) Request item")
    print("5) Inventory manager")
    print("6) Riwayat inventory")
    print("7) Save data")
    print("8) Load data")
    print("9) Help")
    print("10) Exit")
    opt = inputNomorValid("Pilih opsi: ", 1, 10)
    if opt == 1:
        register()
    elif opt == 2:
        login()
    elif opt == 3:
        print("")
        print("-------------------Cari Gadget-------------------")
        print("1) Cari gadget berdasarkan rarity")
        print("2) Cari gadget berdasarkan tahun")
        print("3) Kembali ke main menu")
        opt = inputNomorValid("Pilih opsi:", 1, 3)
        if opt == 1:
            carirarity()
        elif opt == 2:
            caritahun()
        # opt 3 kembali ke menu utama
    elif opt == 4:
        print("")
        print("-------------------Request Item-------------------")
        print("1) Pinjam Gadget")
        print("2) Kembalikan Gadget")
        print("3) Minta consumable")
        print("4) Upgrade Item - NEW!")
        print("5) Kembali ke main menu")
        opt = inputNomorValid("Pilih opsi:", 1, 5)
        if opt == 1:
            pinjam()
        elif opt == 2:
            kembalikan()
        elif opt == 3:
            minta()
        elif opt == 4:
            play_gacha()
        # opt 5 kembali ke main menu
    elif opt == 5:
        print("")
        print("-------------------Inventory Manager-------------------")
        print("1) Menambah item baru")
        print("2) Menghapus item")
        print("3) Mengubah jumlah item")
        print("4) Kembali ke main menu")
        opt = inputNomorValid("Pilih opsi:", 1, 4)
        if opt == 1:
            tambahitem()
        elif opt == 2:
            hapusitem()
        elif opt == 3:
            ubahjumlah()
        # opt 4 kembali ke menu utama
    elif opt == 6:
        print("")
        print("-------------------Riwayat Inventory-------------------")
        print("1) Riwayat peminjaman gadget")
        print("2) Riwayat pengembalian gadget")
        print("3) Riwayat pengambilan consumable")
        print("4) Kembali ke main menu")
        opt = inputNomorValid("Pilih opsi:", 1, 4)
        if opt == 1:
            riwayatpinjam()
        elif opt == 2:
            riwayatkembali()
        elif opt == 3:
            riwayatambil()
        # opt 4 kembali ke menu utama
    elif opt == 7:
        save_kantong_ajaib_data()
    elif opt == 8:
        load_kantong_ajaib_data()
    elif opt == 9:
        help_me()
    elif opt == 10:
        exit_program()