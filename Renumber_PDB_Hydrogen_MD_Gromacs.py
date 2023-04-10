import streamlit as st
import os

# Imposta il percorso dello script renumber_pdb_amber.txt
script_path = "renumber_pdb_amber.txt"

# Aggiungi un titolo all'app
st.title("Renumber PDB for AMBER")

# Aggiungi un'introduzione all'app
st.write("Questa applicazione rinumera i numeri degli atomi idrogeno in un file PDB utilizzando lo script renumber_pdb_amber.txt.")

# Aggiungi un'interfaccia utente per selezionare il file PDB
pdb_file = st.file_uploader("Seleziona un file PDB:", type="pdb")

# Aggiungi un pulsante per eseguire lo script
if st.button("Esegui lo script renumber_pdb_amber.txt"):
    # Verifica che sia stato selezionato un file PDB
    if pdb_file is None:
        st.warning("Seleziona un file PDB.")
    else:
        # Salva il file PDB in una directory temporanea
        with open(os.path.join("temp", pdb_file.name), "wb") as f:
            f.write(pdb_file.getvalue())
            
        # Costruisci il comando per eseguire lo script
        cmd = f"sed -i -f {script_path} temp/{pdb_file.name}"
        
        # Esegui lo script
        os.system(cmd)
        
        # Leggi il file PDB rinumerato
        with open(os.path.join("temp", pdb_file.name), "r") as f:
            pdb_contents = f.read()
        
        # Mostra il file PDB rinumerato
        st.write("File PDB rinumerato:")
        st.code(pdb_contents)
