import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung nilai re
def calculate_re( Rb2, Vcc, Rb1, Vbe):
    # Menghitung besar nilai re
    Vb = (Rb2 * Vcc) / (Rb1 + Rb2)
    Ve = (Vb - Vbe)
    IE = (Ve/Re)
    re = (0.26/IE)

    return re 

# Fungsi untuk menghitung penguatan tegangan
def calculate_voltage_gain(vin,Rc,re):
    # Menghitung penguatan tegangan pada tingkat pertama
    voltage_gain = - Rc / re    
    
    # Menghitung tegangan output
    vout = vin * voltage_gain
    
    return voltage_gain, vout

# Fungsi untuk menghitung impedansi input
def calculate_input_impedance(Rb1, Rb2, beta):
    Rq = ((Rb1 * Rb2) / (Rb1 + Rb2))
    input_impedance = ((Rq * beta * re) / (Rq + (beta * re)))
    
    return input_impedance

# Fungsi untuk menghitung impedansi output
def calculate_output_impedance(Rc):
    output_impedance = Rc
    
    return output_impedance

# Fungsi untuk menghitung sinyal output
def calculate_output_signal(input_signal, voltage_gain):
    output_signal = input_signal * voltage_gain
    
    return output_signal

# Fungsi untuk menampilkan tampilan sinyal input dan output
def plot_signals(input_signal, output_signal):
    time = np.linspace(0, 1, len(input_signal))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    ax1.plot(time, input_signal, label='Sinyal Input')
    ax1.set_xlabel('Waktu (detik)')
    ax1.set_ylabel('Amplitudo (Volt)')
    ax1.legend()
    
    ax2.plot(time, output_signal, label='Sinyal Output')
    ax2.set_xlabel('Waktu (detik)')
    ax2.set_ylabel('Amplitudo (Volt)')
    ax2.legend()
    
    plt.tight_layout()
    st.pyplot(fig)

# Judul aplikasi
st.header('TUGAS BESAR ELEKTRONIKA ANALOG')
st.header('Institut Teknologi Nasional Bandung')
st.header('Dosen : Ir. Rustamaji, M.T')
st.header('Emanuel Ekin Esmanta Purba(11-2021-042) dan Hendy Eka Pratama(112021034)')

#judul aplikasi 2
st.title('Analisis Penguatan Rangkaian BJT')

# Input nilai komponen tingkat pertama
Rb1 = st.number_input('Resistor Base 1 (ohm)')
Rb2 = st.number_input('Resistor Base 2 (ohm)')
Rc = st.number_input('Resistor Kolektor (ohm)')
Re = st.number_input('Resistor Emitter (ohm)')
beta = st.number_input('beta')
Vcc = st.number_input('Vcc (volt)')
Vbe =st.number_input('Vbe (volt)')
coupling1 = st.number_input('Kapasitor Base (Farad)')
coupling2 = st.number_input('Kapasitor Emitter (Farad)')

# Input tegangan input
st.header('Input Tegangan Input')
vin = st.number_input('Tegangan Input (V)')

# input sinyal frekuensi
input_signal_frequency = st.number_input('Frekuensi Sinyal Input (Hz)')

# Tombol untuk menghitung
if st.button('Hitung'):
    
    # Menghitung penguatan arus
    re = calculate_re( Rb2, Vcc, Rb1, Vbe)
    
    # Menghitung penguatan tegangan
    voltage_gain, vout = calculate_voltage_gain(vin,Rc,re)

    # Menghitung impedansi input
    input_impedance1 = calculate_input_impedance(Rb1, Rb2, beta)
    
    # Menghitung impedansi output
    output_impedance2 = calculate_output_impedance(Rc)
    
    # Menghitung sinyal input
    time = np.linspace(0, 1, 5000)
    input_signal = vin * np.sin(2 * np.pi * input_signal_frequency * time)
    
    # Menghitung sinyal output
    output_signal = calculate_output_signal(input_signal, voltage_gain)
    
    # Menampilkan hasil analisis
    st.header('Hasil Analisis')
    st.subheader('Penguatan Tegangan')
    st.write('Penguatan Tegangan :', voltage_gain)
        
    st.subheader('Impedansi Input')
    st.write('Impedansi Input (ohm):', input_impedance1)
    
    st.subheader('Impedansi Output')
    st.write('Impedansi Output (ohm):', output_impedance2)
    
    st.subheader('Tampilan Sinyal')
    plot_signals(input_signal, output_signal)