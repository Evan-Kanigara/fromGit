import datetime as dt
now=dt.datetime.now()
class Sekarang:
    time=now
    tahun=now.year
    jam=now.strftime('%I')
    menit=now.strftime('%M')
    detik=now.strftime('%S')    
    hari2=now.strftime('%A')
    if hari2=='Monday':
        hari='Senin'
    elif hari2=='Tuesday':
        hari='Selasa'
    elif hari2=='Wednesday':
        hari='Rabu'
    elif hari2=='Thursday':
        hari='Kamis'
    elif hari2=='Friday':
        hari='Jumat'
    elif hari2=='Saturday':
        hari='Sabtu'
    else:
        hari='Minggu'
    hari
    bulan2=now.strftime('%B')
    if bulan2=='January':
        bulan='Januari'
    if bulan2=='February':
        bulan='Februari'
    if bulan2=='March':
        bulan='Maret'
    if bulan2=='April':
        bulan='April'
    if bulan2=='May':
        bulan='Mei'
    if bulan2=='June':
        bulan='Jani'
    if bulan2=='July':
        bulan='Juli'
    if bulan2=='August':
        bulan='Agustus'
    if bulan2=='November':
        bulan='November'
    if bulan2=='December':
        bulan='Desember'
    bulan



