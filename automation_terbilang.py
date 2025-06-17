
# Definisikan fungsi terbilang di dalam server action
def terbilang(n):
    angka = [
        'Nol', 'Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Delapan', 'Sembilan',
        'Sepuluh', 'Sebelas', 'Dua Belas', 'Tiga Belas', 'Empat Belas', 'Lima Belas', 'Enam Belas',
        'Tujuh Belas', 'Delapan Belas', 'Sembilan Belas', 'Dua Puluh', 'Tiga Puluh', 'Empat Puluh',
        'Lima Puluh', 'Enam Puluh', 'Tujuh Puluh', 'Delapan Puluh', 'Sembilan Puluh'
    ]
    
    if n < 0:
        return 'Angka negatif tidak dapat diterjemahkan.'
    
    n = int(n)
    
    if n < 20:
        return angka[n]
    if n < 100:
        tens = n // 10
        ones = n % 10
        return angka[18 + tens] + (' ' + angka[ones] if ones != 0 else '')
    if n < 1000:
        hundreds = n // 100
        remainder = n % 100
        return angka[hundreds] + ' Ratus' + (' ' + terbilang(remainder) if remainder != 0 else '')
    if n < 1000000:
        thousands = n // 1000
        remainder = n % 1000
        return terbilang(thousands) + ' Ribu' + (' ' + terbilang(remainder) if remainder != 0 else '')
    if n < 1000000000:
        millions = n // 1000000
        remainder = n % 1000000
        return terbilang(millions) + ' Juta' + (' ' + terbilang(remainder) if remainder != 0 else '')
    return 'Angka terlalu besar'

# Mulai proses untuk setiap record
for rec in records:
    if rec.amount_total < 0:
        rec['x_studio_terbilang'] = 'Angka negatif tidak dapat diterjemahkan.'
    else:
        amount_total = int(rec.amount_total)
        rec['x_studio_terbilang'] = terbilang(amount_total) + ' Rupiah'
