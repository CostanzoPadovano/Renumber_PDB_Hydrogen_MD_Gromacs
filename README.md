# Renumber_PDB_Hydrogen_Molecular_Dynamics_GROMACS
When we start Gromacs program to generate the file gro with pdb2gmx, sometimes appers an error about the numbers of hydrogen like HB3, HD3 etc.
This script is useful to change the specific number of hydrogens in file pdb for amber force field and resolve this problem. 

Use this command on terminal(linux): sed -i -f renumber_pdb_amber.txt file.pdb 

NOTE: if warnings appear in gromacs obout HIS, you have to change it with HIP, HIE or HID. Use a tool like PDB2PQR (https://server.poissonboltzmann.org/pdb2pqr) to protonate the protein. 
