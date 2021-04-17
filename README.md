EN:
simple tool that acquires data from a raspberry pi connected with a GY-521 sensor (MPU-6000)

python scripts (rpi_zero_files folder) should be executed at rpi boot

network absence is handled using files on raspberry and only the previous file is uploaded each reboot to prevent both script working on the same file

the main idea is to place rpi+sensor on a motorcycle so you can get banking angle 

IT:
semplicissimo tool che si interfaccia con una raspberry pi e rileva i dati del sensore GY-521 (MPU-6000)

sulla raspberry devono essere eseguiti allo startup i due script python (cartella rpi_zero_files)

è gestita la mancanza di rete sulla rpi utilizzando dei file come cache, viene caricato sempre il file di rilevazione precendete ad ogni riavvio per evitare che i due script lavorino sullo stesso file

l'idea è di inserire la rpi e sensore sulla moto in modo da rilevare gli angoli di piega


