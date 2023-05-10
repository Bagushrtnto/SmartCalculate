import streamlit as st
st.set_page_config(page_title="SmartCalculate", page_icon=":cloud:", layout="wide")

from streamlit_option_menu import option_menu

# navigasi sidebaar
with st.sidebar :
    selected = option_menu ('Aplikasi Pembuatan Larutan',
    ['Home',
    'Perhitungan pengenceran',
    'Hitung gram dalam ppm',
    'Hitung gram dalam Normalitas',
    'Hitung gram dalam Molaritas'],
    default_index=0)

# halaman home
if (selected == "Home") :
    st.title("Home")
    st.subheader('Hi, I am Smart calculate :cloud: :wave:')
    st.title('__**APLIKASI PERHITUNGAN PEMBUATAN LARUTAN**__')

    st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    st.markdown('__**INTRO**__ - Sebuah aplikasi yang dibuat untuk memudahkan pengguna agar dapat menentukan bobot dan volume larutan dengan mudah.')
    st.header("Aplikasi ini dibuat dan dikembangkan oleh Kelompok 10 LPK, Kelas 1H Dual System D'HIRAETH 2023") 
    st.markdown('''1. Bagus Hartanto (2260010)''')
    st.markdown('''2. Hanna Hanifa (2260021)''')
    st.markdown('''3. Najla Nazhifah (2260032)''')
    st.markdown('''4. Reviza Fauziah (2260043)''')
    st.markdown('''5. Via Amalia Rahmah (2260054)''')

    st.header("Pengertian larutan") 
    st.markdown("Larutan adalah campuran homogen yang terdiri dari dua atau lebih zat. Zat yang jumlahnya lebih sedikit di dalam larutan disebut (zat) terlarut atau solut, sedangkan zat yang jumlahnya lebih banyak daripada zat-zat lain dalam larutan disebut pelarut atau solven. Komposisi zat terlarut dan pelarut dalam larutan dinyatakan dalam konsentrasi larutan, sedangkan proses pencampuran zat terlarut dan pelarut membentuk larutan disebut pelarutan atau solvasi.")

    st.header("Cara membuat larutan")
    st.markdown("Untuk membuat suatu larutan dengan konsentrasi tertentu dapat dilakukan dengan cara:")
    st.markdown('''1. Melarutkan zat terlarut yang berada dalam bentuk padatan.
    jika larutan yang diinginkan komponen terlarutnya pada suhu kamar berupa padatan, maka untuk membuat larutan tersebut, ditimbang sejumlah tertentu zat terlarut yang diperlukan.''')
    st.markdown('''2. Mengencerkan suatu larutan pekat.
    Untuk membuat jenis larutan semacam ini, sangat penting diketahui sifat-sifat dari larutan pekat yang tersedia dan konsentrasi awal dari larutan pekat tersebut. Untuk menentukan berapa banyak larutan pekat yang diperlukan untuk memmbuat sejumlah tertentu larutan dengan konsentrasi yang lebih encer. 
    persamaan yang lazim digunakan adalah V1 x C1 = V2 x C2''')

# halaman perhitungan pengenceran
if (selected == 'Perhitungan pengenceran') :
    st.title('Perhitungan pengenceran')

    volume_awal = st.number_input ("Masukkan nilai volume awal (mL)", min_value = 0)
    konsentrasi_awal = st.number_input ("Masukkan nilai konsentrasi awal (mg/L)", min_value = 0)
    volume_akhir = st.number_input ("Masukkan nilai volume akhir (mL)", min_value = 0)
    konsentrasi_akhir = st.number_input ("Masukkan nilai konsentrasi akhir (mg/L)", min_value = 0)
    hitung = st.button ("Perhitungan volume")

    if hitung :
        volume = (volume_akhir * konsentrasi_akhir) / konsentrasi_awal
        st.write ("Nilai volume pengenceran (mL) adalah = ", volume)
        st.success (f"Nilai volume pengenceran (mL) adalah = {volume}")
    
    hitung = st.button ("perhitungan konsentrasi")

    if hitung :
        konsentrasi = volume_akhir * konsentrasi_akhir / volume_awal
        st.write ("Nilai konsentrasi pengenceran (mg/mL) adalah = ", konsentrasi)
        st.success (f"Nilai konsentrasi pengenceran (mg/mL) adalah = {konsentrasi}")

# halaman hitung gram dalam ppm
if (selected == 'Hitung gram dalam ppm') :
    st.title('Hitung gram dalam ppm')

    ppm = st.number_input ("Masukkan nilai ppm (mg/L)", min_value = 0.0000)
    labu_takar = st.number_input ("Masukkan nilai labu takar (mL)", min_value = 0.00)
    hitung = st.button ("Hitung gram dalam ppm")

    if hitung :
        gram = ppm * labu_takar / 1000
        st.write ("Nilai gram dalam ppm (gram) adalah = ", gram)
        st.success (f"Nilai gram dalam ppm (gram) adalah = {gram}")

# halaman hitung gram dalam Normalitas
if (selected == 'Hitung gram dalam Normalitas') :
    st.title('Hitung gram dalam Normalitas')

    ppm = st.number_input ("Masukkan nilai Normalitas (grek/L)", min_value = 0.00000)
    labu_takar = st.number_input ("Masukkan nilai volume labu takar (L)", min_value = 0.0000)
    BE = st.number_input ("Masukkan nilai BE (g/grek)", min_value = 0.0000)
    hitung = st.button ("Hitung gram dalam Normalitas")

    if hitung :
        gram = Normalitas * labu_takar * BE
        st.write ("Nilai gram dalam Normalitas (gram) adalah = ", gram)
        st.success (f"Nilai gram dalam Normalitas (gram) adalah = {gram}")

# halaman hitung gram dalam Molaritas
if (selected == 'Hitung gram dalam Molaritas') :
    st.title('Hitung gram dalam Molaritas')

    Molaritas = st.number_input ("Masukkan nilai Molaritas (mol/L)", min_value = 0.00000)
    labu_takar = st.number_input ("Masukkan nilai volume labu takar (L)", min_value = 0.0000)
    BM = st.number_input ("Masukkan nilai BM (g/mol)", min_value = 0.0000)
    hitung = st.button ("Hitung gram dalam Molaritas")

    if hitung :
        gram = Molaritas * labu_takar * BM
        st.write ("Nilai gram dalam Molaritas (gram) adalah = ", gram)
        st.success (f"Nilai gram dalam Molaritas (gram) adalah = {gram}")