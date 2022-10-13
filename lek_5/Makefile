CFALGS=-O3 -Werror -lm `pkg-config --cflags --libs opencv4` -fdiagnostics-color=always -g 
program: asbjorn.o
	g++ -o program asbjorn.o $(CFALGS)
asbjorn.o: asbjorn.cpp
	g++ -c -o asbjorn.o $< $(CFALGS) 
