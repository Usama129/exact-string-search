PYTHON=C:\Program Files\Python39\python.exe
SRC=hw2.py

run:
	$(PYTHON) ./$(SRC) -i T.fa -p P.fa

clean:
	rm -rf *.pyc
