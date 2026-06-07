TARIF_LISTRIK = {
    900: 1352,
    1300: 1444,
    2200: 1699,
}

PAJAK_RATE = 0.05
BATAS_PEMAKAIAN_TINGGI = 100
BATAS_PEMAKAIAN_RENDAH = 20
SURPLUS_RATE = 0.05
POTONGAN_HEMAT = 10000

def hitung_tagihan_listrik(nama_pelanggan, daya, pemakaian_kwh):
    tarif_per_kwh = TARIF_LISTRIK.get(daya, 0)
    total_tagihan = pemakaian_kwh * tarif_per_kwh

    if pemakaian_kwh > BATAS_PEMAKAIAN_TINGGI:
        print("Pemakaian tinggi, dikenakan biaya surplus 5%")
        total_tagihan = total_tagihan + (total_tagihan * SURPLUS_RATE)

    if pemakaian_kwh < BATAS_PEMAKAIAN_RENDAH:
        print("Pemakaian hemat, mendapat potongan 10000")
        total_tagihan = total_tagihan - POTONGAN_HEMAT

    pajak = total_tagihan * PAJAK_RATE
    total_tagihan = total_tagihan + pajak

    print("Nama pelanggan: " + nama_pelanggan)
    print("Total tagihan: " + str(total_tagihan))
    return total_tagihan

hitung_tagihan_listrik("Andi", 1300, 120)
