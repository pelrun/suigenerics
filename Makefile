
build: rz.bin

rz.bin: rotozoom.z80 syntax.z80 trig.z80
	pasmo -d rotozoom.z80 rz.bin rz.sym > rz.lst

syntax.z80: syntax.py
	python syntax.py > syntax.z80

trig.z80: trig.py
	python trig.py > trig.z80

debug: rz.bin
	./gnc100em -d -p rz.bin

trace: rz.bin
	./gnc100em -t -p rz.bin > trace.txt

run: rz.bin
	./gnc100em -p rz.bin
